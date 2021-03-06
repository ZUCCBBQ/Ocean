# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_extract_year.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Year(object):
    def setupUi(self, Year):
        Year.setObjectName("Year")
        Year.resize(810, 600)
        Year.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 12pt \"楷体\";")
        self.centralwidget = QtWidgets.QWidget(Year)
        self.centralwidget.setObjectName("centralwidget")
        self.Journallabel = QtWidgets.QLabel(self.centralwidget)
        self.Journallabel.setGeometry(QtCore.QRect(160, 160, 91, 21))
        self.Journallabel.setStyleSheet("font: 14pt \"楷体\";")
        self.Journallabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Journallabel.setObjectName("Journallabel")
        self.yearComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.yearComboBox.setGeometry(QtCore.QRect(560, 160, 69, 22))
        self.yearComboBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.yearComboBox.setObjectName("yearComboBox")
        self.yearComboBox.addItem("")
        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(490, 160, 61, 21))
        self.yearLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.yearLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearLabel.setObjectName("yearLabel")
        self.extractButton = QtWidgets.QPushButton(self.centralwidget)
        self.extractButton.setGeometry(QtCore.QRect(360, 410, 91, 31))
        self.extractButton.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);\n"
"")
        self.extractButton.setObjectName("extractButton")
        self.borderLabel = QtWidgets.QLabel(self.centralwidget)
        self.borderLabel.setGeometry(QtCore.QRect(140, 120, 531, 361))
        self.borderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.borderLabel.setText("")
        self.borderLabel.setObjectName("borderLabel")
        self.uiLabel = QtWidgets.QLabel(self.centralwidget)
        self.uiLabel.setGeometry(QtCore.QRect(320, 50, 171, 31))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.uiLabel.setFont(font)
        self.uiLabel.setStyleSheet("font: 18pt \"楷体\";")
        self.uiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uiLabel.setObjectName("uiLabel")
        self.journalComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.journalComboBox.setGeometry(QtCore.QRect(260, 160, 221, 21))
        self.journalComboBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.journalComboBox.setObjectName("journalComboBox")
        self.journalComboBox.addItem("")
        self.promptLabel = QtWidgets.QLabel(self.centralwidget)
        self.promptLabel.setGeometry(QtCore.QRect(190, 210, 431, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setStyleSheet("font: 13pt \"楷体\";")
        self.promptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.promptLabel.setWordWrap(True)
        self.promptLabel.setObjectName("promptLabel")
        self.borderLabel.raise_()
        self.Journallabel.raise_()
        self.yearComboBox.raise_()
        self.yearLabel.raise_()
        self.extractButton.raise_()
        self.uiLabel.raise_()
        self.journalComboBox.raise_()
        self.promptLabel.raise_()
        Year.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Year)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 810, 22))
        self.menubar.setObjectName("menubar")
        Year.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Year)
        self.statusbar.setObjectName("statusbar")
        Year.setStatusBar(self.statusbar)

        self.retranslateUi(Year)
        QtCore.QMetaObject.connectSlotsByName(Year)

    def retranslateUi(self, Year):
        _translate = QtCore.QCoreApplication.translate
        Year.setWindowTitle(_translate("Year", "按年信息抽取"))
        self.Journallabel.setText(_translate("Year", "期刊名称"))
        self.yearComboBox.setItemText(0, _translate("Year", "2018"))
        self.yearLabel.setText(_translate("Year", "年份"))
        self.extractButton.setText(_translate("Year", "抽取"))
        self.uiLabel.setText(_translate("Year", "按年信息抽取"))
        self.journalComboBox.setItemText(0, _translate("Year", "AICHE_JOURNAL"))
        self.promptLabel.setText(_translate("Year", "<html><head/><body><p>正在抽取如下期刊相应年份的信息,请稍后...</p><p>（或请选择一个期刊和年份以抽取信息）</p></body></html>"))

