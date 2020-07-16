from PyQt5 import QtWidgets
from covid_gui import Ui_MainWindow
import sys
from main import CovidData

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        # Carrega dados
        self.covid_data = CovidData()

        super(Window, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # associa os botões a métodos relevantes
        self.ui.pushButton_execute.clicked.connect(self.execute)

        # tipos de gráfico
        self.ui.comboBox_chart_type.addItems(['Dados observados','Previsão','Previsões Comparadas'])
        
        self.ui.radio_MinSaude.toggled.connect(self.change_metric_list)
        self.ui.radio_Brasil_io.toggled.connect(self.change_metric_list)

        self.ui.radio_MinSaude.setChecked(True)

    # -------------------------------------------------------------------------------------------------------

    def execute(self):
        # método principal
        location_list = self.get_inputs()
        metric = self.ui.comboBox_metric.currentText()
        chart_type = self.ui.comboBox_chart_type.currentText()
        data_source = self.get_data_source()

        if len(location_list) == 0:
            print('Nenhum local inserido!')
        
        else:
            if len(location_list) == 1:
                
                # primeira e única localidade
                location = location_list[0]

                if chart_type == 'Dados observados':
                    # Mostrar dados observados de 1 só
                    self.covid_data.plot_column(metric, region=location[0], state=location[1], city=location[2], data_source=data_source)
                    
                elif chart_type == 'Previsão':
                    # Mostrar previsão
                    self.covid_data.fit(metric, region=location[0], state=location[1], city=location[2], data_source=data_source) 
                    # TODO: colocar algum local na gui p/ os pred_periods

                else:
                    # Comparar previsões
                    self.covid_data.fit_compare(metric, region=location[0], state=location[1], city=location[2], data_source=data_source)

            else:
                if chart_type == 'Dados observados':
                    # Mostrar dados observados de mais de um
                    self.covid_data.plot_compare(metric, location_list, data_source=data_source)
                else:
                    print('Nâo é possivel obter gráficos de %s para mais de uma métrica. Tente individualmente!' % metric)


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
        return table.item(i,0) is not None or table.item(i,1) is not None or table.item(i,1) is not None

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

            else:
                self.ui.comboBox_metric.addItems(['last_available_confirmed', 'last_available_confirmed_per_100k_inhabitants',
                                                  'last_available_death_rate', 'last_available_deaths',
                                                  'new_confirmed', 'new_deaths'])
        

app = QtWidgets.QApplication([])

application = Window()

application.show()

sys.exit(app.exec())