import numpy as np
import pandas as pd
from fbprophet import Prophet

import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator

from random import choice
import os

import warnings
import logging

warnings.filterwarnings('ignore')
logging.getLogger('fbprophet').setLevel(logging.WARNING)

# script folder 
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

class CovidData():

    def __init__(self):

        # cria Dataframe de dados brutos
        self.raw_df = pd.read_csv(filepath_or_buffer=os.path.join(SCRIPT_PATH, 'raw.csv'), delimiter=';')

        self.correct_col_name = {'data' : 'Data',
                                 'casosAcumulado' : 'Casos Acumulados',
                                 'casosNovos' : 'Casos Novos',
                                 'obitosAcumulado' : 'Óbitos Acumulados',
                                 'obitosNovos' : 'Óbitos Novos',
                                 'log(casosAcumulado)' : 'log(Casos Acumulados)',
                                 'log(obitosAcumulado)' : 'log(Óbitos Acumulados)',
                                 'Recuperadosnovos' : 'Recuperados Novos'}
    
    # -------------------------------------------------------------------------------------------------------

    def query_df(self, region, state, city):
        
        '''
        (String, string, string) -> Dataframe
        Faz uma query ao dataframe de dados brutos para uma região, estado e cidade e retorna o resultado. '''

        query_string = 'regiao == "%s"' % region
        
        if state == '':
            query_string += ' and estado.isnull()'
        else:
            query_string += ' and estado == "%s"' % state
        
        if city == '':
            query_string += ' and municipio.isnull() and codmun.isnull()'
        else:
            query_string += ' and municipio == "%s"' % city

        return self.raw_df.query(query_string)
        
    # -------------------------------------------------------------------------------------------------------

    def get_df(self, region, state, city):
        
        ''' None -> Dataframe (ou None)
        Retorna uma cópia do Dataframe do local selecionado com as colunas "data" e a inserida pelo usuário '''
        df = self.query_df(region, state, city)

        # corrige o formato de leitura das datas
        df['data'] = pd.to_datetime(df['data'], dayfirst=True)

        # cria colunas de dados log-transformados
        df['log(casosAcumulado)'] = np.log(df['casosAcumulado'])
        df['log(obitosAcumulado)'] = np.log(df['obitosAcumulado'])

        # substitui possíveis np.inf por np.nan
        df.replace([np.inf, -np.inf], np.nan, inplace=True)

        return df

    # -------------------------------------------------------------------------------------------------------

    def plot_column(self, column, region, state='', city='', ax=None):

        '''(String, String, String, String) -> None
        Plota o gráfico de uma métrica em um local selecionado'''

        df = self.get_df(region, state, city)

        if not df.empty:
            if ax is None:
                fig = plt.figure(facecolor='w', figsize=(10,6))
                ax = fig.add_subplot(111)
                show = True
            else:
                fig = ax.get_figure()
                show = False
        
            locator = AutoDateLocator(interval_multiples=False)
            formatter = AutoDateFormatter(locator)
            ax.xaxis.set_major_locator(locator)
            ax.xaxis.set_major_formatter(formatter)
            ax.plot(df['data'], df[column], label='%s | %s' % (self.correct_col_name[column], self.format_location(region, state, city)))
            
            if show:
                fig.legend()
                plt.show()
        else:
            print(self.not_found_msg(region, state, city))

    # -------------------------------------------------------------------------------------------------------

    def plot_compare(self, column, location_list):
        '''
        location_list é uma lista com tuples (region, state, city) '''

        fig = plt.figure(facecolor='w', figsize=(10,6))
        ax = fig.add_subplot(111)

        for location in location_list:
            self.plot_column(column, location[0], location[1], location[2], ax=ax)
        
        fig.legend()
        plt.show()   
    
    # -------------------------------------------------------------------------------------------------------

    def format_location(self, region, state, city):

        formatted_location = region
        if state != '': formatted_location += ' - %s' % state
        if city != '': formatted_location += ' - %s' % city
        return formatted_location

    # -------------------------------------------------------------------------------------------------------

    def get_model(self, column, df, seasonality_mode):

        '''
        TODO: modificar o Cap
        if column == 'casosAcumulado' or column=='obitosAcumulado':
            df['cap'] = 600000
            return Prophet(growth='logistic')
        else:
            return Prophet(daily_seasonality=True,
                           weekly_seasonality=True)'''

        return Prophet(daily_seasonality=True, weekly_seasonality=True, seasonality_mode=seasonality_mode)

    # -------------------------------------------------------------------------------------------------------

    def forecast(self, df, column, pred_periods, m):
        '''(Dataframe, String, Int) -> None
        Usa o Prophet para prever n dias e plotar o gráfico de uma métrica em um local selecionado'''
   
        m.add_country_holidays(country_name='BR')
        m.fit(df)
        future = m.make_future_dataframe(periods=pred_periods)
        #if column == 'casosAcumulado' or column=='obitosAcumulado': future['cap'] = 600000
        return m.predict(future)

    # -------------------------------------------------------------------------------------------------------

    def fit(self, column, region, state='', city='', pred_periods=30, seasonality_mode='additive', **kwargs):
        
        '''(String, String, String, String, Int) -> None
        Usa o Prophet para prever n dias e plotar o gráfico de uma métrica em um local selecionado'''
        
        df = self.get_df(region, state, city)
        df = df[['data', column]]
        df.columns = ['ds', 'y']

        if not df.empty:
            m = self.get_model(column, df, seasonality_mode=seasonality_mode)
            m.plot(self.forecast(df, column, pred_periods, m))
            plt.show()

        else:
            print(self.not_found_msg(region, state, city))

    # -------------------------------------------------------------------------------------------------------
       
    def fit_compare(self, column, region, state='', city='', compare_periods=60, pred_periods=30, seasonality_mode='additive'):
        
        ''' (String, String, String, String, Int, Int) -> None
        Faz previsões usando intervalos do dataframe e as plota em um mesmo gráfico
        '''
        
        df = self.get_df(region, state, city)
        df = df[['data', column]]
        df.columns = ['ds', 'y']

        if not df.empty:
            indexes = list(range(0, df.last_valid_index(), compare_periods))
            last_index = df.last_valid_index()
            indexes[-1] = last_index

            fig = plt.figure(facecolor='w', figsize=(10,6))
            ax = fig.add_subplot(111)
            plot_actual = False

            colors = ['#0072B2', '#F90909', '#D48888', '#BD9446', '#63FF14', '#B056EF',
                    '#FF9C09', '#669677', '#8F6696', '#EEAD0E']

            for i in indexes:
                # plots actual data on last value
                if i == indexes[-1]: 
                    plot_actual = True
                    sub_df = df.iloc[ : ]
                    num_forecasts = pred_periods
                else:
                    sub_df = df.iloc[ : i + compare_periods]
                    num_forecasts = last_index + pred_periods - (i + compare_periods)
                
                m = self.get_model(column, sub_df, seasonality_mode=seasonality_mode)
                
                plot_color = choice(colors)
                colors.remove(plot_color)

                self.prophet_plot(m, self.forecast(sub_df, column, num_forecasts, m), ax=ax,
                                plot_color=plot_color, plot_actual=plot_actual, 
                                label='Using %d periods' % len(sub_df))
            
            fig.legend()
            plt.show()

        else: # df is empty
            print(self.not_found_msg(region, state, city))

    # -------------------------------------------------------------------------------------------------------
        
    def prophet_plot(self, m, fcst, ax=None, uncertainty=True, plot_cap=True, xlabel='ds', ylabel='y',
    plot_color='#0072B2', plot_actual=True, label='N Periods', figsize=(10, 6)):
       
        # Método adaptado do .plot do Prophet. 

        if ax is None:
            fig = plt.figure(facecolor='w', figsize=figsize)
            ax = fig.add_subplot(111)
        else:
            fig = ax.get_figure()

        fcst_t = fcst['ds'].dt.to_pydatetime()

        if plot_actual:    
            ax.plot(m.history['ds'].dt.to_pydatetime(), m.history['y'], 'k.')
        
        ax.plot(fcst_t, fcst['yhat'], ls='-', c=plot_color, label=label)
        
        if 'cap' in fcst and plot_cap:
            ax.plot(fcst_t, fcst['cap'], ls='--', c='k')
        if m.logistic_floor and 'floor' in fcst and plot_cap:
            ax.plot(fcst_t, fcst['floor'], ls='--', c='k')
        if uncertainty and m.uncertainty_samples:
            ax.fill_between(fcst_t, fcst['yhat_lower'], fcst['yhat_upper'],
                            color=plot_color, alpha=0.2)

        # Specify formatting to workaround matplotlib issue #12925
        locator = AutoDateLocator(interval_multiples=False)
        formatter = AutoDateFormatter(locator)
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(formatter)
        ax.grid(True, which='major', c='gray', ls='-', lw=1, alpha=0.2)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        fig.tight_layout()

        return fig

    # -------------------------------------------------------------------------------------------------------

    def not_found_msg(self, region, state, city):

        # Retorna uma mensagem de qual local não foi encontrado no dataframe de dados brutos

        str_out = 'No data found for region = "%s"' % region
        if state != '':
            str_out += ' and region = "%s"' % state
        if city != '':
            str_out += ' and city = "%s"' % city

        return str_out

def main():

    data = CovidData()

    #data.plot_column('casosNovos', region='Brasil')
    data.plot_compare('log(casosAcumulado)', [('Brasil','',''), ('Sudeste', 'SP', ''), ('Sudeste', 'SP', 'Santo André')])
    #data.fit(column='obitosNovos', region='Brasil', pred_periods=120, seasonality_mode='multiplicative')
    #data.fit_compare(column='log(casosAcumulado)', region='Brasil', state='', city='', pred_periods=100)

main()