# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'covid_faq.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_FAQBox(object):
    def setupUi(self, FAQBox):
        FAQBox.setObjectName("FAQBox")
        FAQBox.resize(660, 550)
        FAQBox.setMinimumSize(QtCore.QSize(660, 550))
        FAQBox.setMaximumSize(QtCore.QSize(660, 550))
        self.listWidget_FAQ = QtWidgets.QListWidget(FAQBox)
        self.listWidget_FAQ.setGeometry(QtCore.QRect(20, 20, 291, 131))
        self.listWidget_FAQ.setObjectName("listWidget_FAQ")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_FAQ.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_FAQ.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_FAQ.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_FAQ.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_FAQ.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_FAQ.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_FAQ.addItem(item)
        self.textBrowser_FAQ = QtWidgets.QTextBrowser(FAQBox)
        self.textBrowser_FAQ.setGeometry(QtCore.QRect(20, 160, 621, 371))
        self.textBrowser_FAQ.setObjectName("textBrowser_FAQ")

        self.retranslateUi(FAQBox)
        QtCore.QMetaObject.connectSlotsByName(FAQBox)

    def retranslateUi(self, FAQBox):
        _translate = QtCore.QCoreApplication.translate
        FAQBox.setWindowTitle(_translate("FAQBox", "FAQ"))
        __sortingEnabled = self.listWidget_FAQ.isSortingEnabled()
        self.listWidget_FAQ.setSortingEnabled(False)
        item = self.listWidget_FAQ.item(0)
        item.setText(_translate("FAQBox", "Como o programa faz previsões?"))
        item = self.listWidget_FAQ.item(1)
        item.setText(_translate("FAQBox", "De onde vêm os dados?"))
        item = self.listWidget_FAQ.item(2)
        item.setText(_translate("FAQBox", "Como os dados são organizados no programa?"))
        item = self.listWidget_FAQ.item(3)
        item.setText(_translate("FAQBox", "Como o programa atualiza os dados?"))
        item = self.listWidget_FAQ.item(4)
        item.setText(_translate("FAQBox", "Como a interface gráfica foi criada?"))
        item = self.listWidget_FAQ.item(5)
        item.setText(_translate("FAQBox", "O que significam as \"Opções\" do Prophet?"))
        item = self.listWidget_FAQ.item(6)
        item.setText(_translate("FAQBox", "Por que o programa não encontra o local que digitei?"))
        self.listWidget_FAQ.setSortingEnabled(__sortingEnabled)
        self.textBrowser_FAQ.setHtml(_translate("FAQBox", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"justify\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:12pt;\"><br /></p></body></html>"))

