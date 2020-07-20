# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covid_messagebox.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Messagebox(object):
    def setupUi(self, Messagebox):
        Messagebox.setObjectName("Messagebox")
        Messagebox.resize(300, 300)
        Messagebox.setMinimumSize(QtCore.QSize(300, 300))
        Messagebox.setMaximumSize(QtCore.QSize(300, 300))
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

