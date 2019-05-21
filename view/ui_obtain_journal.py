# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_obtain_journal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Journal(object):
    def setupUi(self, Journal):
        Journal.setObjectName("Journal")
        Journal.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(Journal)
        self.centralwidget.setObjectName("centralwidget")
        self.obtainButton = QtWidgets.QPushButton(self.centralwidget)
        self.obtainButton.setGeometry(QtCore.QRect(370, 410, 71, 21))
        self.obtainButton.setStyleSheet("font: 11pt \"黑体\";\n"
"")
        self.obtainButton.setObjectName("obtainButton")
        self.journalLabel = QtWidgets.QLabel(self.centralwidget)
        self.journalLabel.setGeometry(QtCore.QRect(270, 170, 71, 21))
        self.journalLabel.setStyleSheet("font: 11pt \"黑体\";")
        self.journalLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.journalLabel.setObjectName("journalLabel")
        self.jounralComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.jounralComboBox.setGeometry(QtCore.QRect(360, 170, 181, 21))
        self.jounralComboBox.setStyleSheet("font: 11pt \"黑体\";")
        self.jounralComboBox.setObjectName("jounralComboBox")
        self.jounralComboBox.addItem("")
        self.uiLabel = QtWidgets.QLabel(self.centralwidget)
        self.uiLabel.setGeometry(QtCore.QRect(310, 50, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.uiLabel.setFont(font)
        self.uiLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.uiLabel.setObjectName("uiLabel")
        self.borderLabel = QtWidgets.QLabel(self.centralwidget)
        self.borderLabel.setGeometry(QtCore.QRect(140, 120, 531, 361))
        self.borderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.borderLabel.setText("")
        self.borderLabel.setObjectName("borderLabel")
        self.promptLabel = QtWidgets.QLabel(self.centralwidget)
        self.promptLabel.setGeometry(QtCore.QRect(240, 210, 331, 181))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setStyleSheet("font: 11pt \"黑体\";")
        self.promptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.promptLabel.setWordWrap(True)
        self.promptLabel.setObjectName("promptLabel")
        self.borderLabel.raise_()
        self.obtainButton.raise_()
        self.journalLabel.raise_()
        self.jounralComboBox.raise_()
        self.uiLabel.raise_()
        self.promptLabel.raise_()
        Journal.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Journal)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        Journal.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Journal)
        self.statusbar.setObjectName("statusbar")
        Journal.setStatusBar(self.statusbar)

        self.retranslateUi(Journal)
        QtCore.QMetaObject.connectSlotsByName(Journal)

    def retranslateUi(self, Journal):
        _translate = QtCore.QCoreApplication.translate
        Journal.setWindowTitle(_translate("Journal", "期刊信息获取"))
        self.obtainButton.setText(_translate("Journal", "获取"))
        self.journalLabel.setText(_translate("Journal", "期刊名称"))
        self.jounralComboBox.setItemText(0, _translate("Journal", "AICHE_JOURNAL"))
        self.uiLabel.setText(_translate("Journal", "期刊信息获取"))
        self.promptLabel.setText(_translate("Journal", "正在获取如下期刊的信息,请稍后...\n"
"（或请选择一个期刊以获取信息）"))

