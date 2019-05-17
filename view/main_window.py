# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(280, 60, 211, 411))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(20, 0, 20, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.journalButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.journalButton.setFont(font)
        self.journalButton.setObjectName("journalButton")
        self.verticalLayout.addWidget(self.journalButton)
        self.yearButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.yearButton.setFont(font)
        self.yearButton.setObjectName("yearButton")
        self.verticalLayout.addWidget(self.yearButton)
        self.ldaButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.ldaButton.setFont(font)
        self.ldaButton.setObjectName("ldaButton")
        self.verticalLayout.addWidget(self.ldaButton)
        self.apButton = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setFamily("Adobe Arabic")
        font.setPointSize(14)
        self.apButton.setFont(font)
        self.apButton.setObjectName("apButton")
        self.verticalLayout.addWidget(self.apButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.journalButton.setText(_translate("MainWindow", "期刊信息获取"))
        self.yearButton.setText(_translate("MainWindow", "按年信息抽取"))
        self.ldaButton.setText(_translate("MainWindow", "主题词提取"))
        self.apButton.setText(_translate("MainWindow", "主题词聚类"))

