from PyQt5 import QtWidgets, QtGui, QtCore
from covid_gui import Ui_MainWindow, Ui_Dialog_Progress, Ui_Messagebox

import sys
import os
from time import sleep
from pandas import to_datetime

from main import CovidData
import file_operations as f_op

SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        self.progressbar_box = ProgressBarBox()
        self.messagebox = MessageBox()
        self.splash_screen = SplashScreen()

        self.splash_screen.update_text('Carregando dados...')

        # Carrega dados
        self.covid_data = CovidData(dialog=self.progressbar_box, messagebox=self.messagebox, splash_screen=self.splash_screen)

        self.splash_screen.update_text('Configurando Interface...')

        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # associa os botões a métodos relevantes
        self.ui.pushButton_execute.clicked.connect(self.execute)

        # tipos de gráfico
        self.ui.comboBox_chart_type.addItems(['Dados observados','Previsão','Previsões Comparadas'])

        # modos de sazonalidade
        self.ui.comboBox_seasonality_mode.addItems(['Aditiva', 'Multiplicativa'])

        self.ui.radio_MinSaude.toggled.connect(self.change_metric_list)
        self.ui.radio_Brasil_io.toggled.connect(self.change_metric_list)

        self.ui.radio_MinSaude.setChecked(True)

        self.ui.action_UpdateBrasil_io.triggered.connect(self.update_data)
        self.ui.action_UpdateMinSaude.triggered.connect(self.update_data)

        self.splash_screen.close()

    # -------------------------------------------------------------------------------------------------------
    def execute(self):

        # método principal
        location_list = self.get_inputs()
        metric = self.ui.comboBox_metric.currentText()
        chart_type = self.ui.comboBox_chart_type.currentText()
        data_source = self.get_data_source()
        add_moving_average = self.ui.checkBox_moving_avg.isChecked()
        
        start_date = to_datetime(self.ui.dateEdit_initial.date().toPyDate())
        end_date = to_datetime(self.ui.dateEdit_end.date().toPyDate())
        pred_periods = self.ui.spinBox_pred_periods.value()
        comp_periods = self.ui.spinBox_comp_periods.value()

        dict_seas = {'Aditiva' : 'additive', 'Multiplicativa' : 'multiplicative'}

        # parâmetros do prophet
        seasonality_mode = dict_seas[self.ui.comboBox_seasonality_mode.currentText()]
        changepoint_prior_scale = self.ui.doubleSpinBox_cps.value()
        holidays_prior_scale = self.ui.doubleSpinBox_hps.value()
        seasonality_prior_scale = self.ui.doubleSpinBox_sps.value()

        if changepoint_prior_scale == 0: changepoint_prior_scale = 0.05
        if holidays_prior_scale == 0: holidays_prior_scale=10.0
        if seasonality_prior_scale == 0: seasonality_prior_scale=10.0
            
        # checa datas
        if start_date > end_date:
            # necessário trocar valores
            aux_date = start_date
            start_date = end_date
            end_date = aux_date

        if len(location_list) == 0: 
            self.messagebox.show_message('Nenhum local inserido!', type='Aviso')
        
        else:
            if len(location_list) == 1:
                
                # primeira e única localidade
                location = location_list[0]

                if chart_type == 'Dados observados':
                    # Mostrar dados observados de 1 só
                    self.covid_data.plot_column(metric, region=location[0], state=location[1], city=location[2], 
                                                data_source=data_source, add_moving_average=add_moving_average,
                                                start_date=start_date, end_date=end_date)
                    
                elif chart_type == 'Previsão':
                    # Mostrar previsão
                    self.covid_data.fit(metric, region=location[0], state=location[1], city=location[2], 
                                        pred_periods=pred_periods, seasonality_mode=seasonality_mode,
                                        seasonality_prior_scale=seasonality_prior_scale,
                                        holidays_prior_scale=holidays_prior_scale,
                                        changepoint_prior_scale=changepoint_prior_scale,
                                        data_source=data_source, start_date=start_date, end_date=end_date) 
                                        

                else:
                    # Comparar previsões
                    self.covid_data.fit_compare(metric, region=location[0], state=location[1], city=location[2], 
                                                compare_periods=comp_periods, pred_periods=pred_periods, seasonality_mode=seasonality_mode,
                                                seasonality_prior_scale=seasonality_prior_scale,
                                                holidays_prior_scale=holidays_prior_scale,
                                                changepoint_prior_scale=changepoint_prior_scale,
                                                data_source=data_source, start_date=start_date, end_date=end_date)

            else:
                if chart_type == 'Dados observados':
                    # Mostrar dados observados de mais de um
                    self.covid_data.plot_compare(metric, location_list, data_source=data_source, add_moving_average=add_moving_average,
                                                 start_date=start_date, end_date=end_date)
                else:
                    self.messagebox.show_message('Nâo é possivel obter gráficos de %s para mais de um local. Tente individualmente!' % metric, \
                                                 type='Erro')

    # -------------------------------------------------------------------------------------------------------
    def get_data_source(self):
        
        if self.ui.radio_Brasil_io.isChecked():
            return 'Brasil.io'
        else:
            return 'Ministério da Saúde'
    
    # -------------------------------------------------------------------------------------------------------
    def get_inputs(self):

        table = self.ui.tableWidget_locations
        location_list = []
        i = 0

        while i <= table.rowCount() and self.valid_row(i, table):
            
            location = []
            for j in range(3):
                cell = table.item(i,j)
                if cell is None:
                    location.append('')
                else:
                    location.append(cell.text())
            
            location_list.append(tuple(location))
            i += 1
            
        return location_list
    
    # -------------------------------------------------------------------------------------------------------
    def valid_row(self, i, table):

        # pelo menos um valor preenchido
        return table.item(i,0) is not None or table.item(i,1) is not None or table.item(i,2) is not None

    # -------------------------------------------------------------------------------------------------------
    def change_metric_list(self):
        
        # muda as métricas exibidas com base na fonte de dados selecionada
        btn = self.sender()
        self.ui.comboBox_metric.clear()
        
        if btn.isChecked():
            if btn.text() == 'Usar dados do Ministério da Saúde':
                self.ui.comboBox_metric.addItems(['casosAcumulado', 'casosNovos','obitosAcumulado',
                                                  'obitosNovos', 'log(casosAcumulado)',
                                                  'log(obitosAcumulado)', 'Recuperadosnovos'])
                
                self.config_dates(self.covid_data.df_min_saude)

            else:
                self.ui.comboBox_metric.addItems(['last_available_confirmed', 'last_available_confirmed_per_100k_inhabitants',
                                                  'last_available_death_rate', 'last_available_deaths',
                                                  'new_confirmed', 'new_deaths'])
                self.config_dates(self.covid_data.df_brasil_io)


    # -------------------------------------------------------------------------------------------------------
    def config_dates(self, df):
        
        min_date = to_datetime(df['date']).min()
        max_date = to_datetime(df['date']).max()

        for dateEdit in [self.ui.dateEdit_initial, self.ui.dateEdit_end]:
            dateEdit.setMinimumDate(min_date)
            dateEdit.setMaximumDate(max_date)

        self.ui.dateEdit_end.setDate(max_date)
        
    # -------------------------------------------------------------------------------------------------------
    def update_data(self):

        btn = self.sender()
        self.progressbar_box.update_title('Baixando arquivos')
        
        if 'Brasil.io' in btn.text():
            
            self.progressbar_box.show()
            f_op.download_file_brasil_io(dialog=self.progressbar_box)
            self.progressbar_box._update('Dados atualizados!', 100)

            self.covid_data = CovidData(dialog=self.progressbar_box)

            self.progressbar_box.close()

            self.messagebox.show_message('Dados do Brasil.io atualizados com sucesso!')

        else:

            self.progressbar_box.show()
            f_op.download_file_min_saude(dialog=self.progressbar_box)
            self.progressbar_box._update('Movendo e convertendo arquivo...', 75)
            f_op.move_xlsx_to(SCRIPT_PATH)
            self.progressbar_box._update('Dados atualizados!', 100)

            self.covid_data = CovidData(dialog=self.progressbar_box)
            
            self.progressbar_box.close()
            
            self.messagebox.show_message('Dados do Ministério da Saúde atualizados com sucesso!')
            

# -------------------------------------------------------------------------------------------------------
class ProgressBarBox(QtWidgets.QDialog):

    def __init__(self):

        super(ProgressBarBox, self).__init__()
        self.ui = Ui_Dialog_Progress()
        self.ui.setupUi(self)

    def _update(self, text, percentage=None):

        self.ui.label_dialog.setText(text)
        self.ui.progressBar.setValue(percentage)
        QtWidgets.qApp.processEvents()

    def update_title(self, title):

        self.setWindowTitle(title)
        QtWidgets.qApp.processEvents()

# -------------------------------------------------------------------------------------------------------
class MessageBox(QtWidgets.QDialog):

    def __init__(self):

        super(MessageBox, self).__init__()
        self.ui = Ui_Messagebox()
        self.ui.setupUi(self)

    def show_message(self, text, type='Mensagem'):

        self.ui.label_msgbox_text.setText(text)
        self.setWindowTitle('%s do programa!' % type)

        if type == 'Mensagem':
            # fonte: https://www.flaticon.com/br/icone-gratis/consultando_1260416?term=dialog&page=1&position=73
            self.setWindowIcon(QtGui.QIcon(os.path.join(SCRIPT_PATH, 'mensagem.png')))
            
        elif type == 'Aviso':
            # fonte: https://www.flaticon.com/br/icone-gratis/aviso_595067?term=warning&page=1&position=3
            self.setWindowIcon(QtGui.QIcon(os.path.join(SCRIPT_PATH, 'aviso.png')))

        elif type == 'Erro':
            # fonte: https://www.flaticon.com/br/icone-gratis/cancelar_753345?term=error&page=1&position=5
            self.setWindowIcon(QtGui.QIcon(os.path.join(SCRIPT_PATH, 'erro.png')))
        
        QtWidgets.qApp.processEvents()
        self.ui.label_msgbox_text.setWordWrap(True)
        
        self.show()

class SplashScreen():
    def __init__(self):
        self.splash = QtWidgets.QSplashScreen(QtGui.QPixmap('logo.png')) 
        self.splash.show()

    def update_text(self, text):
        self.splash.showMessage(text, QtCore.Qt.AlignBottom | QtCore.Qt.AlignLeft)
        QtWidgets.qApp.processEvents()

    def close(self):
        self.splash.close()


app = QtWidgets.QApplication([])

application = Window()

application.show()

sys.exit(app.exec())