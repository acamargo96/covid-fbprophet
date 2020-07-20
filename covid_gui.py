# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covid2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 396)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(400, 40, 190, 81))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.radio_MinSaude = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_MinSaude.setObjectName("radio_MinSaude")
        self.verticalLayout_2.addWidget(self.radio_MinSaude)
        self.radio_Brasil_io = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.radio_Brasil_io.setObjectName("radio_Brasil_io")
        self.verticalLayout_2.addWidget(self.radio_Brasil_io)
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(400, 140, 191, 86))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_chart_type = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_chart_type.setObjectName("label_chart_type")
        self.verticalLayout_3.addWidget(self.label_chart_type)
        self.comboBox_chart_type = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_chart_type.setObjectName("comboBox_chart_type")
        self.verticalLayout_3.addWidget(self.comboBox_chart_type)
        self.label_metric = QtWidgets.QLabel(self.verticalLayoutWidget_3)
        self.label_metric.setObjectName("label_metric")
        self.verticalLayout_3.addWidget(self.label_metric)
        self.comboBox_metric = QtWidgets.QComboBox(self.verticalLayoutWidget_3)
        self.comboBox_metric.setObjectName("comboBox_metric")
        self.verticalLayout_3.addWidget(self.comboBox_metric)
        self.pushButton_execute = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_execute.setGeometry(QtCore.QRect(430, 260, 121, 51))
        self.pushButton_execute.setObjectName("pushButton_execute")
        self.tableWidget_locations = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_locations.setGeometry(QtCore.QRect(20, 30, 351, 311))
        self.tableWidget_locations.setRowCount(100)
        self.tableWidget_locations.setObjectName("tableWidget_locations")
        self.tableWidget_locations.setColumnCount(3)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_locations.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_locations.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_locations.setHorizontalHeaderItem(2, item)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName("menubar")
        self.menuArquivo = QtWidgets.QMenu(self.menubar)
        self.menuArquivo.setObjectName("menuArquivo")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_UpdateMinSaude = QtWidgets.QAction(MainWindow)
        self.action_UpdateMinSaude.setObjectName("action_UpdateMinSaude")
        self.action_UpdateBrasil_io = QtWidgets.QAction(MainWindow)
        self.action_UpdateBrasil_io.setObjectName("action_UpdateBrasil_io")
        self.menuArquivo.addAction(self.action_UpdateMinSaude)
        self.menuArquivo.addAction(self.action_UpdateBrasil_io)
        self.menubar.addAction(self.menuArquivo.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Covid-19 com FBProphet"))
        self.radio_MinSaude.setText(_translate("MainWindow", "Usar dados do Ministério da Saúde"))
        self.radio_Brasil_io.setText(_translate("MainWindow", "Usar Dados do Brasil.io"))
        self.label_chart_type.setText(_translate("MainWindow", "Tipo de Gráfico"))
        self.label_metric.setText(_translate("MainWindow", "Métrica"))
        self.pushButton_execute.setText(_translate("MainWindow", "Executar"))
        item = self.tableWidget_locations.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Região"))
        item = self.tableWidget_locations.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Estado"))
        item = self.tableWidget_locations.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Cidade"))
        self.menuArquivo.setTitle(_translate("MainWindow", "Arquivo"))
        self.action_UpdateMinSaude.setText(_translate("MainWindow", "Atualizar dados - Min Saúde"))
        self.action_UpdateBrasil_io.setText(_translate("MainWindow", "Atualizar dados - Brasil.io"))

class Ui_Dialog_Progress(object):
    def setupUi(self, Dialog_Progress):
        Dialog_Progress.setObjectName("Dialog_Progress")
        Dialog_Progress.resize(300, 100)
        Dialog_Progress.setMaximumSize(QtCore.QSize(300, 100))
        self.progressBar = QtWidgets.QProgressBar(Dialog_Progress)
        self.progressBar.setGeometry(QtCore.QRect(20, 10, 261, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_dialog = QtWidgets.QLabel(Dialog_Progress)
        self.label_dialog.setGeometry(QtCore.QRect(20, 40, 251, 51))
        self.label_dialog.setObjectName("label_dialog")

        self.retranslateUi(Dialog_Progress)
        QtCore.QMetaObject.connectSlotsByName(Dialog_Progress)

    def retranslateUi(self, Dialog_Progress):
        _translate = QtCore.QCoreApplication.translate
        Dialog_Progress.setWindowTitle(_translate("Dialog_Progress", "TITLE"))
        self.label_dialog.setText(_translate("Dialog_Progress", "TextLabel"))

class Ui_Messagebox(object):
    def setupUi(self, Messagebox):
        Messagebox.setObjectName("Messagebox")
        Messagebox.resize(300, 200)
        Messagebox.setMinimumSize(QtCore.QSize(300, 200))
        Messagebox.setMaximumSize(QtCore.QSize(300, 200))
        self.buttonBox = QtWidgets.QDialogButtonBox(Messagebox)
        self.buttonBox.setGeometry(QtCore.QRect(30, 150, 251, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_msgbox_text = QtWidgets.QLabel(Messagebox)
        self.label_msgbox_text.setGeometry(QtCore.QRect(30, 30, 241, 101))
        self.label_msgbox_text.setObjectName("label_msgbox_text")

        self.retranslateUi(Messagebox)
        self.buttonBox.accepted.connect(Messagebox.accept)
        self.buttonBox.rejected.connect(Messagebox.reject)
        QtCore.QMetaObject.connectSlotsByName(Messagebox)

    def retranslateUi(self, Messagebox):
        _translate = QtCore.QCoreApplication.translate
        Messagebox.setWindowTitle(_translate("Messagebox", "TITLE"))
        self.label_msgbox_text.setText(_translate("Messagebox", "TextLabel"))

