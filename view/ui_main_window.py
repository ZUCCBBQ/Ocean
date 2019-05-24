# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainUi(object):
    def setupUi(self, MainUi):
        MainUi.setObjectName("MainUi")
        MainUi.resize(800, 600)
        MainUi.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 12pt \"楷体\";")
        self.centralwidget = QtWidgets.QWidget(MainUi)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(280, 130, 251, 371))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout.setSpacing(40)
        self.verticalLayout.setObjectName("verticalLayout")
        self.journalButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.journalButton.sizePolicy().hasHeightForWidth())
        self.journalButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.journalButton.setFont(font)
        self.journalButton.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.journalButton.setObjectName("journalButton")
        self.verticalLayout.addWidget(self.journalButton)
        self.yearButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearButton.sizePolicy().hasHeightForWidth())
        self.yearButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.yearButton.setFont(font)
        self.yearButton.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.yearButton.setObjectName("yearButton")
        self.verticalLayout.addWidget(self.yearButton)
        self.ldaButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.ldaButton.sizePolicy().hasHeightForWidth())
        self.ldaButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.ldaButton.setFont(font)
        self.ldaButton.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.ldaButton.setObjectName("ldaButton")
        self.verticalLayout.addWidget(self.ldaButton)
        self.apButton = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.apButton.sizePolicy().hasHeightForWidth())
        self.apButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.apButton.setFont(font)
        self.apButton.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);")
        self.apButton.setObjectName("apButton")
        self.verticalLayout.addWidget(self.apButton)
        self.uiLabel = QtWidgets.QLabel(self.centralwidget)
        self.uiLabel.setGeometry(QtCore.QRect(280, 60, 251, 31))
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
        MainUi.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainUi)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainUi.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainUi)
        self.statusbar.setObjectName("statusbar")
        MainUi.setStatusBar(self.statusbar)

        self.retranslateUi(MainUi)
        QtCore.QMetaObject.connectSlotsByName(MainUi)

    def retranslateUi(self, MainUi):
        _translate = QtCore.QCoreApplication.translate
        MainUi.setWindowTitle(_translate("MainUi", "期刊主题分析程序"))
        self.journalButton.setText(_translate("MainUi", "期刊信息获取"))
        self.yearButton.setText(_translate("MainUi", "按年信息抽取"))
        self.ldaButton.setText(_translate("MainUi", "主题词提取"))
        self.apButton.setText(_translate("MainUi", "主题词聚类"))
        self.uiLabel.setText(_translate("MainUi", "期刊主题分析程序"))

