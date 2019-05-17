# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'obtain_journal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(646, 435)
        self.obtainButton = QtWidgets.QPushButton(Form)
        self.obtainButton.setGeometry(QtCore.QRect(290, 340, 75, 23))
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(10)
        self.obtainButton.setFont(font)
        self.obtainButton.setObjectName("obtainButton")
        self.topic = QtWidgets.QLabel(Form)
        self.topic.setGeometry(QtCore.QRect(280, 40, 111, 31))
        self.topic.setAlignment(QtCore.Qt.AlignCenter)
        self.topic.setObjectName("topic")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.obtainButton.setText(_translate("Form", "获取"))
        self.topic.setText(_translate("Form", "期刊信息获取"))

