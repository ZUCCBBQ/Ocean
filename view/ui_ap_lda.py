# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_ap_lda.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Ap(object):
    def setupUi(self, Ap):
        Ap.setObjectName("Ap")
        Ap.resize(800, 600)
        Ap.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 12pt \"楷体\";")
        self.centralwidget = QtWidgets.QWidget(Ap)
        self.centralwidget.setObjectName("centralwidget")
        self.numTopicLabel = QtWidgets.QLabel(self.centralwidget)
        self.numTopicLabel.setGeometry(QtCore.QRect(560, 160, 161, 20))
        self.numTopicLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.numTopicLabel.setObjectName("numTopicLabel")
        self.apButton = QtWidgets.QPushButton(self.centralwidget)
        self.apButton.setGeometry(QtCore.QRect(350, 410, 91, 31))
        self.apButton.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);\n"
"")
        self.apButton.setObjectName("apButton")
        self.uiLabel = QtWidgets.QLabel(self.centralwidget)
        self.uiLabel.setGeometry(QtCore.QRect(310, 50, 171, 31))
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
        self.yearComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.yearComboBox.setGeometry(QtCore.QRect(470, 160, 69, 22))
        self.yearComboBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.yearComboBox.setObjectName("yearComboBox")
        self.yearComboBox.addItem("")
        self.borderLabel = QtWidgets.QLabel(self.centralwidget)
        self.borderLabel.setGeometry(QtCore.QRect(60, 120, 671, 361))
        self.borderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.borderLabel.setText("")
        self.borderLabel.setObjectName("borderLabel")
        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(400, 160, 61, 21))
        self.yearLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.yearLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearLabel.setObjectName("yearLabel")
        self.promptLabel = QtWidgets.QLabel(self.centralwidget)
        self.promptLabel.setGeometry(QtCore.QRect(120, 210, 551, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setStyleSheet("font: 13pt \"楷体\";")
        self.promptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.promptLabel.setWordWrap(True)
        self.promptLabel.setObjectName("promptLabel")
        self.Journallabel = QtWidgets.QLabel(self.centralwidget)
        self.Journallabel.setGeometry(QtCore.QRect(70, 160, 91, 21))
        self.Journallabel.setStyleSheet("font: 14pt \"楷体\";")
        self.Journallabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.Journallabel.setObjectName("Journallabel")
        self.journalComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.journalComboBox.setGeometry(QtCore.QRect(170, 160, 231, 21))
        self.journalComboBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.journalComboBox.setObjectName("journalComboBox")
        self.journalComboBox.addItem("")
        self.borderLabel.raise_()
        self.promptLabel.raise_()
        self.numTopicLabel.raise_()
        self.apButton.raise_()
        self.uiLabel.raise_()
        self.yearComboBox.raise_()
        self.yearLabel.raise_()
        self.Journallabel.raise_()
        self.journalComboBox.raise_()
        Ap.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ap)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Ap.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ap)
        self.statusbar.setObjectName("statusbar")
        Ap.setStatusBar(self.statusbar)

        self.retranslateUi(Ap)
        QtCore.QMetaObject.connectSlotsByName(Ap)

    def retranslateUi(self, Ap):
        _translate = QtCore.QCoreApplication.translate
        Ap.setWindowTitle(_translate("Ap", "主题词聚类"))
        self.numTopicLabel.setText(_translate("Ap", "主题词个数：48"))
        self.apButton.setText(_translate("Ap", "聚类"))
        self.uiLabel.setText(_translate("Ap", "主题词聚类"))
        self.yearComboBox.setItemText(0, _translate("Ap", "2018"))
        self.yearLabel.setText(_translate("Ap", "年份"))
        self.promptLabel.setText(_translate("Ap", "<html><head/><body><p>正在抽取如下期刊相应年份的信息,请稍后...</p><p>（或请选择一个期刊和年份以抽取信息）</p></body></html>"))
        self.Journallabel.setText(_translate("Ap", "期刊名称"))
        self.journalComboBox.setItemText(0, _translate("Ap", "AICHE_JOURNAL"))

