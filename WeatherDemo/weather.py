# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'weather.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(543, 320)
        self.queryButton = QtWidgets.QPushButton(Dialog)
        self.queryButton.setGeometry(QtCore.QRect(110, 270, 75, 23))
        self.queryButton.setObjectName("queryButton")
        self.clearButton = QtWidgets.QPushButton(Dialog)
        self.clearButton.setGeometry(QtCore.QRect(310, 270, 75, 23))
        self.clearButton.setObjectName("clearButton")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 30, 481, 231))
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(100, 20, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(40, 20, 61, 21))
        self.label.setObjectName("label")
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(10, 50, 451, 171))
        self.textEdit.setObjectName("textEdit")
        self.groupBox.raise_()
        self.queryButton.raise_()
        self.clearButton.raise_()

        self.retranslateUi(Dialog)
        self.queryButton.clicked.connect(Dialog.queryWeather)
        self.clearButton.clicked.connect(Dialog.clearText)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.groupBox.setTitle(_translate("Dialog", "城市天气预报"))
        self.comboBox.setItemText(0, _translate("Dialog", "北京"))
        self.comboBox.setItemText(1, _translate("Dialog", "上海"))
        self.comboBox.setItemText(2, _translate("Dialog", "天津"))
        self.label.setText(_translate("Dialog", "城市"))
        self.queryButton.setText(_translate("Dialog", "查询"))
        self.clearButton.setText(_translate("Dialog", "清空"))
