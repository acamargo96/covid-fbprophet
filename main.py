import numpy as np
import pandas as pd
from fbprophet import Prophet

import matplotlib.pyplot as plt
from matplotlib.dates import AutoDateFormatter, AutoDateLocator

from random import choice
import os
import gzip

import warnings
import logging

from time import perf_counter

# módulo de download dos dados em .csv
import file_operations as f_op

# conversão de caracteres UTF-8
from utf8_char_correction import UTF8_dict

warnings.filterwarnings('ignore')
logging.getLogger('fbprophet').setLevel(logging.WARNING)

# caminho do script 
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

class CovidData():

    def __init__(self, download_new=False, dialog=None, messagebox=None, splash_screen=None):
        
        self.dialog = dialog
        self.messagebox = messagebox
        self.splash_screen = splash_screen

        # acompanhamento de progresso p/ o usuário
        if self.dialog is not None: 
            self.dialog.update_title('Criando DataFrames')
            self.dialog._update('Criando DataFrame para dados do Ministério da Saúde...', 8)

        if self.splash_screen is not None: self.splash_screen.update_text('Criando DataFrame para dados do Ministério da Saúde...')

        self.df_min_saude = self.create_df('Ministério da Saúde', download_new)
        
        if self.dialog is not None: self.dialog._update('Criando DataFrame para dados do Brasil.io...', 24)
        if self.splash_screen is not None: self.splash_screen.update_text('Criando DataFrame para dados do Brasil.io...')

        self.df_brasil_io = self.create_df('Brasil.io', download_new)

        self.correct_col_name = { 
            
            'Brasil.io' : {
                'date' : 'Data',
                'last_available_confirmed' : 'last_available_confirmed',
                'last_available_confirmed_per_100k_inhabitants' : 'last_available_confirmed_per_100k_inhabitants',
                'last_available_death_rate' : 'last_available_death_rate',
                'last_available_deaths' : 'last_available_deaths',
                'new_confirmed' : 'new_confirmed',
                'new_deaths' : 'new_deaths'
                           },

            'Ministério da Saúde' : {
                'date' : 'Data',
                'casosAcumulado' : 'Casos Acumulados',
                'casosNovos' : 'Casos Novos',
                'obitosAcumulado' : 'Óbitos Acumulados',
                'obitosNovos' : 'Óbitos Novos',
                'log(casosAcumulado)' : 'log(Casos Acumulados)',
                'log(obitosAcumulado)' : 'log(Óbitos Acumulados)',
                'Recuperadosnovos' : 'Recuperados Novos'}
        }
    
    # -------------------------------------------------------------------------------------------------------
    def create_df(self, data_source, download_new):

        if data_source == 'Brasil.io':
            if (not os.path.isfile(os.path.join(SCRIPT_PATH, 'data.csv.gz'))) or download_new:
                # Arquivo .csv não foi baixado ou o usuário especificou um novo download
                #if self.dialog is not None: self.dialog._update('Baixando arquivo do Brasil.io...', 32)
                if self.splash_screen is not None: self.splash_screen.update_text('Baixando arquivo do Brasil.io...')
                f_op.download_file_brasil_io()

            # Abre o arquivo e carrega o dataframe
            if self.dialog is not None: self.dialog._update('Lendo .csv do Brasil.io...', 40)
            if self.splash_screen is not None: self.splash_screen.update_text('Lendo arquivo do Brasil.io...')

            with gzip.open('data.csv.gz', 'rt', encoding='latin') as f:
                df = pd.read_csv(f, delimiter=',', encoding='latin', lineterminator='\n')

            # Corrige caracteres errados por conta do UTF-8
            if self.dialog is not None: self.dialog._update('Corrigindo erros de UTF-8...', 48)
            if self.splash_screen is not None: self.splash_screen.update_text('Corrigindo erros de UTF-8...')

            for k in UTF8_dict:
                df['city'] = df['city'].str.replace(k, UTF8_dict[k])

        elif data_source == 'Ministério da Saúde':

            if (not os.path.isfile(os.path.join(SCRIPT_PATH, 'raw.csv'))) or download_new:
                # Arquivo .xlsx não foi baixado ou convertido ou usuário quer baixar novo
                # Baixa, move e converte para .csv
                if self.dialog is not None: self.dialog._update('Baixando arquivo do Ministério da Saúde...', 16)
                if self.splash_screen is not None: self.splash_screen.update_text('Baixando do Ministério da Saúde...')

                f_op.download_file_min_saude()
                f_op.move_xlsx_to(SCRIPT_PATH)

            if self.dialog is not None: self.dialog._update('Lendo .csv do Ministério da Saúde...', 24)
            if self.splash_screen is not None: self.splash_screen.update_text('Lendo .csv do Ministério da Saúde...')

            df = pd.read_csv('raw.csv', delimiter=',', encoding='latin', lineterminator='\n')
            
            df.columns = ['region', 'state', 'city', 'coduf', 'codmun', 'codRegiaoSaude',
                          'nomeRegiaoSaude', 'date', 'semanaEpi', 'populacaoTCU2019',
                          'casosAcumulado', 'casosNovos', 'obitosAcumulado', 'obitosNovos',
                          'Recuperadosnovos', 'emAcompanhamentoNovos', 'interior/metropolitana']
           
        else:
            return None
        
        return df

    # -------------------------------------------------------------------------------------------------------

    def query_df(self, region, state, city, data_source):
        
        '''
        (String, string, string) -> Dataframe
        Faz uma query ao dataframe de dados brutos para uma região, estado e cidade e retorna o resultado. '''
        
        if data_source == 'Ministério da Saúde':
            df = self.df_min_saude
        elif data_source == 'Brasil.io':
            df = self.df_brasil_io

        query_terms = []

        if 'region' in df.columns:
            # dados do min. da saude
            query_terms.append('region == "%s"' % region)

        if state == '':
            query_terms.append('state.isnull()')
        else:
            query_terms.append('state == "%s"' % state)
        
        if city == '':
            if 'codmun' in df.columns:
                query_terms.append('city.isnull() and codmun.isnull()')
            else:
                query_terms.append('city.isnull()')

        else:
            query_terms.append('city == "%s"' % city)

        query_string = ' and '.join(query_terms)
  
        return df.query(query_string, engine='python')
        
    # -------------------------------------------------------------------------------------------------------

    def get_df(self, region, state, city, data_source):
        
        ''' None -> Dataframe (ou None)
        Retorna uma cópia do Dataframe do local selecionado com as colunas "data" e a inserida pelo usuário '''
        df = self.query_df(region, state, city, data_source)

        # corrige o formato de leitura das datas
        df['date'] = pd.to_datetime(df['date']) #, dayfirst=True)

        # cria colunas de dados log-transformados
        if 'casosAcumulado' in df.columns:
            df['log(casosAcumulado)'] = np.log(df['casosAcumulado'])
            df['log(obitosAcumulado)'] = np.log(df['obitosAcumulado'])
        else:
            df['log(last_available_confirmed)'] = np.log(df['last_available_confirmed'])
            df['log(last_available_deaths)'] = np.log(df['last_available_deaths'])

        # substitui possíveis np.inf por np.nan
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        
        return df

    # -------------------------------------------------------------------------------------------------------

    def plot_column(self, column, region='', state='', city='', ax=None, data_source='Ministério da Saúde',
                    add_moving_average=False):

        '''(String, String, String, String) -> None
        Plota o gráfico de uma métrica em um local selecionado'''

        if self.valid_col(column, data_source):    

            df = self.get_df(region, state, city, data_source)

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
                ax.plot(df['date'], df[column], label='%s | %s' % (self.correct_col_name[data_source][column], self.format_location( [region, state, city] ) ) )

                if add_moving_average:
                    ax.plot(df['date'], df[column].expanding(min_periods=60).mean(), \
                            label='Média Móvel | %s | %s' % (self.correct_col_name[data_source][column], self.format_location( [region, state, city] ) ) )
                
                if show:
                    fig.legend()
                    plt.show()
            else:
                self.messagebox.show_message(self.not_found_msg(region, state, city), type='Erro')

        else:
            valid_vals = [k for k in self.correct_col_name[data_source] if k != 'date']
            self.messagebox.show_message('''\nO nome %s não corresponde a uma coluna válida para dados do %s. 
            Os nomes válidos para colunas do conjunto atual são:\n- %s \n''' % (data_source, column, '\n- '.join(valid_vals) ))

    # -------------------------------------------------------------------------------------------------------

    def plot_compare(self, column, location_list, data_source='Ministério da Saúde', add_moving_average=False):
        '''
        location_list é uma lista com tuples (region, state, city) '''

        if self.valid_col(column, data_source):
            fig = plt.figure(facecolor='w', figsize=(10,6))
            ax = fig.add_subplot(111)

            for location in location_list:
                self.plot_column(column, location[0], location[1], location[2], ax=ax, 
                                data_source=data_source, add_moving_average=add_moving_average)
            
            fig.legend()
            plt.show()   
        
        else:
            valid_vals = [k for k in self.correct_col_name[data_source] if k != 'date']
            self.messagebox.show_message('''\nO nome %s não corresponde a uma coluna válida para dados do %s. 
            Os nomes válidos para colunas do conjunto atual são:\n- %s \n''' % (data_source, column, '\n- '.join(valid_vals) ))

    # -------------------------------------------------------------------------------------------------------

    def format_location(self, loc_list):
        
        location_terms = []
        for loc in loc_list:
            if loc != '': location_terms.append(loc)
        
        return ' - '.join(location_terms)

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

    def fit(self, column, region='', state='', city='', pred_periods=30, 
            seasonality_mode='additive', data_source='Ministério da Saúde'):
        
        '''(String, String, String, String, Int) -> None
        Usa o Prophet para prever n dias e plotar o gráfico de uma métrica em um local selecionado'''

        # checa validade do período
        message_list = []
        if pred_periods == 0: 
            message_list.append('Períodos de previsão muito curtos corrigidos de %d para 30 dias.' % pred_periods)
            pred_periods = 30

        if self.valid_col(column, data_source):

            if self.dialog is not None: 
                self.dialog.update_title('Realizando previsão')
                self.dialog.show()
                self.dialog._update('Consultando DataFrame...', 0)

            df = self.get_df(region, state, city, data_source)
            if self.dialog is not None: self.dialog._update('Consultando DataFrame...', 25)
            df = df[['date', column]]
            if self.dialog is not None: self.dialog._update('Consultando DataFrame...', 50)
            df.columns = ['ds', 'y']

            if not df.empty:
                if self.dialog is not None: self.dialog._update('Criando modelo...', 75)
                m = self.get_model(column, df, seasonality_mode=seasonality_mode)
                m.plot(self.forecast(df, column, pred_periods, m))
                if self.dialog is not None: 
                    self.dialog._update('Previsão feita!', 100)
                    self.dialog.close()

                plt.show()
                if len(message_list) != 0: self.messagebox.show_message(message_list[0])

            else:
                if self.dialog is not None: self.dialog.close()
                self.messagebox.show_message(self.not_found_msg(region, state, city), type='Erro')
        
        else:
            valid_vals = [k for k in self.correct_col_name[data_source] if k != 'date']
            self.messagebox.show_message('''\nO nome %s não corresponde a uma coluna válida para dados do %s. 
            Os nomes válidos para colunas do conjunto atual são:\n- %s \n''' % (data_source, column, '\n- '.join(valid_vals) ))

    # -------------------------------------------------------------------------------------------------------
       
    def fit_compare(self, column, region='', state='', city='', compare_periods=60, 
                    pred_periods=30, seasonality_mode='additive', data_source='Ministério da Saúde'):
        
        ''' (String, String, String, String, Int, Int) -> None
        Faz previsões usando intervalos do dataframe e as plota em um mesmo gráfico
        '''

        # checa validade dos períodos
        message_list = []
        if pred_periods == 0: 
            message_list.append('Períodos de previsão muito curtos corrigidos de %d para 30 dias.' % pred_periods)
            pred_periods = 30
        if compare_periods < 20: 
            message_list.append('Períodos de comparação muito curtos corrigidos de %d para 60 dias.' % compare_periods)
            compare_periods = 60

        if self.valid_col(column, data_source):
            
            if self.dialog is not None:
                self.dialog.update_title('Realizando previsões') 
                self.dialog.show()
                self.dialog._update('Consultando DataFrame...', 0)

            df = self.get_df(region, state, city, data_source)
            if self.dialog is not None: self.dialog._update('Consultando DataFrame...', 15)
            df = df[['date', column]]
            if self.dialog is not None: self.dialog._update('Consultando DataFrame...', 30)
            # garante que os dados descontinuos do Brasil.io não façam pular indices
            df.reset_index(drop=True, inplace=True)
            if self.dialog is not None: self.dialog._update('Consultando DataFrame...', 45)
            df.columns = ['ds', 'y']

            if not df.empty:

                if self.dialog is not None: self.dialog._update('Configurando gráfico...', 60)
                indexes = list(range(0, df.last_valid_index(), compare_periods))
                last_index = df.last_valid_index()
                indexes[-1] = last_index

                fig = plt.figure(facecolor='w', figsize=(10,6))
                ax = fig.add_subplot(111)
                plot_actual = False

                colors = ['#0072B2', '#F90909', '#D48888', '#BD9446', '#63FF14', '#B056EF',
                        '#FF9C09', '#669677', '#8F6696', '#EEAD0E']

                line_count = 1

                for i in indexes:
                    if self.dialog is not None: self.dialog._update('Criando modelo %d de %d...' % (line_count, len(indexes)), 60 + 40 * (line_count - 1) / len(indexes))
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
                                    label='Usando %d períodos' % len(sub_df))

                    line_count += 1
                
                if self.dialog is not None: 
                    self.dialog._update('Previsões criadas!', 100)
                    self.dialog.close()

                fig.legend()
                plt.show()

                if len(message_list) != 0: self.messagebox.show_message('\n\n'.join(message_list))

            else: # df está vazio
                if self.dialog is not None: self.dialog.close()
                self.messagebox.show_message(self.not_found_msg(region, state, city), type='Erro')
        
        else: # coluna inválida
            valid_vals = [k for k in self.correct_col_name[data_source] if k != 'date']
            self.messagebox.show_message('''\nO nome %s não corresponde a uma coluna válida para dados do %s. 
            Os nomes válidos para colunas do conjunto atual são:\n- %s \n''' % (data_source, column, '\n- '.join(valid_vals) ))

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

        str_out = 'Nenhum dado foi encontrado para região = "%s"' % region
        if state != '':
            str_out += ' e estado = "%s"' % state
        if city != '':
            str_out += ' e cidade = "%s"' % city

        return str_out

    # -------------------------------------------------------------------------------------------------------

    def valid_col(self, column, data_source):

        return column in self.correct_col_name[data_source] and column != 'date'


'''
def main():

    data = CovidData()

    # Brasil.io
    #data.plot_column('new_deaths', state='SP', city='São Paulo', data_source='Brasil.io')
    #data.plot_compare('new_confirmed', [('','SP','São Paulo'), ('', 'SP', 'Santo André'), ('', 'SP', 'São Caetano do Sul')], data_source='Brasil.io')
    #data.fit(column='new_confirmed', state='SP', city='São Paulo', pred_periods=120, seasonality_mode='multiplicative', data_source='Brasil.io')
    #data.fit_compare(column='new_confirmed', state='SP', city='São Paulo', pred_periods=100, seasonality_mode='multiplicative', data_source='Brasil.io')

    # Min. da Saúde
    #data.plot_column('casosAcumulado', region='Sudeste', state='SP', city='São Paulo', data_source='Ministério da Saúde')
    #data.plot_compare('casosAcumulado', [('Sudeste','SP','São Paulo'), ('Sudeste', 'SP', 'Santo André'), ('Sudeste', 'SP', 'São Caetano do Sul')], data_source='Ministério da Saúde')
    #data.fit(column='casosAcumulado', region='Sudeste', state='SP', city='São Paulo', pred_periods=120, seasonality_mode='multiplicative', data_source='Ministério da Saúde')
    #data.fit_compare(column='casosAcumulado', region='Sudeste', state='SP', city='São Paulo', pred_periods=100, seasonality_mode='multiplicative', data_source='Ministério da Saúde')

main()
'''