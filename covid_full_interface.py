# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covid2_2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1060, 472)
        MainWindow.setMinimumSize(QtCore.QSize(1060, 472))
        MainWindow.setMaximumSize(QtCore.QSize(1060, 472))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_execute = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_execute.setGeometry(QtCore.QRect(410, 360, 151, 51))
        self.pushButton_execute.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_execute.setObjectName("pushButton_execute")
        self.tableWidget_locations = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_locations.setGeometry(QtCore.QRect(20, 30, 351, 381))
        self.tableWidget_locations.setRowCount(100)
        self.tableWidget_locations.setObjectName("tableWidget_locations")
        self.tableWidget_locations.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_locations.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_locations.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_locations.setHorizontalHeaderItem(2, item)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(390, 30, 211, 111))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setObjectName("groupBox")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 191, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_MinSaude = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_MinSaude.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radio_MinSaude.setObjectName("radio_MinSaude")
        self.verticalLayout_2.addWidget(self.radio_MinSaude)
        self.radio_Brasil_io = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_Brasil_io.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.radio_Brasil_io.setObjectName("radio_Brasil_io")
        self.verticalLayout_2.addWidget(self.radio_Brasil_io)
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 150, 211, 201))
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_2)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 191, 161))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_chart_type = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_chart_type.setObjectName("label_chart_type")
        self.verticalLayout_3.addWidget(self.label_chart_type)
        self.comboBox_chart_type = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_chart_type.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_chart_type.setObjectName("comboBox_chart_type")
        self.verticalLayout_3.addWidget(self.comboBox_chart_type)
        self.label_metric = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_metric.setObjectName("label_metric")
        self.verticalLayout_3.addWidget(self.label_metric)
        self.comboBox_metric = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_metric.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.comboBox_metric.setObjectName("comboBox_metric")
        self.verticalLayout_3.addWidget(self.comboBox_metric)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        self.checkBox_moving_avg = QtWidgets.QCheckBox(self.verticalLayoutWidget_3)
        self.checkBox_moving_avg.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_moving_avg.setObjectName("checkBox_moving_avg")
        self.verticalLayout_3.addWidget(self.checkBox_moving_avg)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(620, 30, 201, 321))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_3)
        self.verticalLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 181, 231))
        self.verticalLayoutWidget_4.setObjectName("verticalLayoutWidget_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label.setObjectName("label")
        self.verticalLayout_4.addWidget(self.label)
        self.dateEdit_initial = QtWidgets.QDateEdit(self.verticalLayoutWidget_4)
        self.dateEdit_initial.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_initial.setObjectName("dateEdit_initial")
        self.verticalLayout_4.addWidget(self.dateEdit_initial)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.dateEdit_end = QtWidgets.QDateEdit(self.verticalLayoutWidget_4)
        self.dateEdit_end.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.dateEdit_end.setObjectName("dateEdit_end")
        self.verticalLayout_4.addWidget(self.dateEdit_end)
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.spinBox_pred_periods = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox_pred_periods.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox_pred_periods.setObjectName("spinBox_pred_periods")
        self.verticalLayout_4.addWidget(self.spinBox_pred_periods)
        self.label_4 = QtWidgets.QLabel(self.verticalLayoutWidget_4)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_4.addWidget(self.label_4)
        self.spinBox_comp_periods = QtWidgets.QSpinBox(self.verticalLayoutWidget_4)
        self.spinBox_comp_periods.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.spinBox_comp_periods.setObjectName("spinBox_comp_periods")
        self.verticalLayout_4.addWidget(self.spinBox_comp_periods)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(840, 30, 201, 321))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.groupBox_4)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 20, 181, 231))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.comboBox_seasonality_mode = QtWidgets.QComboBox(self.verticalLayoutWidget)
        self.comboBox_seasonality_mode.setObjectName("comboBox_seasonality_mode")
        self.verticalLayout.addWidget(self.comboBox_seasonality_mode)
        self.label_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.doubleSpinBox_sps = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_sps.setObjectName("doubleSpinBox_sps")
        self.verticalLayout.addWidget(self.doubleSpinBox_sps)
        self.label_7 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.doubleSpinBox_hps = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_hps.setObjectName("doubleSpinBox_hps")
        self.verticalLayout.addWidget(self.doubleSpinBox_hps)
        self.label_8 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout.addWidget(self.label_8)
        self.doubleSpinBox_cps = QtWidgets.QDoubleSpinBox(self.verticalLayoutWidget)
        self.doubleSpinBox_cps.setObjectName("doubleSpinBox_cps")
        self.verticalLayout.addWidget(self.doubleSpinBox_cps)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1060, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        self.menuAjuda = QtWidgets.QMenu(self.menubar)
        self.menuAjuda.setObjectName("menuAjuda")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_UpdateMinSaude = QtWidgets.QAction(MainWindow)
        self.action_UpdateMinSaude.setObjectName("action_UpdateMinSaude")
        self.action_UpdateBrasil_io = QtWidgets.QAction(MainWindow)
        self.action_UpdateBrasil_io.setObjectName("action_UpdateBrasil_io")
        self.actionFAQ = QtWidgets.QAction(MainWindow)
        self.actionFAQ.setObjectName("actionFAQ")
        self.menuArquivo.addAction(self.action_UpdateMinSaude)
        self.menuArquivo.addAction(self.action_UpdateBrasil_io)
        self.menuAjuda.addAction(self.actionFAQ)
        self.menubar.addAction(self.menuArquivo.menuAction())
        self.menubar.addAction(self.menuAjuda.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid-19 com FBProphet"))
        self.pushButton_execute.setText(_translate("MainWindow", "Executar"))
        item = self.tableWidget_locations.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Região"))
        item = self.tableWidget_locations.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Estado"))
        item = self.tableWidget_locations.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cidade"))
        self.groupBox.setTitle(_translate("MainWindow", "Tipo de Dado"))
        self.radio_MinSaude.setText(_translate("MainWindow", "Usar dados do Ministério da Saúde"))
        self.radio_Brasil_io.setText(_translate("MainWindow", "Usar Dados do Brasil.io"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Opções de Gráfico"))
        self.label_chart_type.setText(_translate("MainWindow", "Tipo de Gráfico"))
        self.label_metric.setText(_translate("MainWindow", "Métrica"))
        self.checkBox_moving_avg.setText(_translate("MainWindow", "Incluir Média Móvel"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Opções de Data"))
        self.label.setText(_translate("MainWindow", "Data Inicial "))
        self.label_2.setText(_translate("MainWindow", "Data Final"))
        self.label_3.setText(_translate("MainWindow", "Períodos para Prever"))
        self.label_4.setText(_translate("MainWindow", "Períodos para Comparar Previsões"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Opções do Prophet"))
        self.label_5.setText(_translate("MainWindow", "Tipo de Sazonalidade"))
        self.label_6.setText(_translate("MainWindow", "Seasonality Prior Scale"))
        self.label_7.setText(_translate("MainWindow", "Holidays Prior Scale"))
        self.label_8.setText(_translate("MainWindow", "Changepoint Prior Scale"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.menuAjuda.setTitle(_translate("MainWindow", "Ajuda"))
        self.action_UpdateMinSaude.setText(_translate("MainWindow", "Atualizar dados - Min Saúde"))
        self.action_UpdateBrasil_io.setText(_translate("MainWindow", "Atualizar dados - Brasil.io"))
        self.actionFAQ.setText(_translate("MainWindow", "FAQ"))

