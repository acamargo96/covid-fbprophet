# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covid3.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

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

