# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_select_lda.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Lda(object):
    def setupUi(self, Lda):
        Lda.setObjectName("Lda")
        Lda.resize(800, 601)
        Lda.setStyleSheet("background-color: rgb(170, 255, 255);\n"
"font: 12pt \"楷体\";")
        self.centralwidget = QtWidgets.QWidget(Lda)
        self.centralwidget.setObjectName("centralwidget")
        self.journalLabel = QtWidgets.QLabel(self.centralwidget)
        self.journalLabel.setGeometry(QtCore.QRect(70, 160, 81, 21))
        self.journalLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.journalLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.journalLabel.setObjectName("journalLabel")
        self.journalComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.journalComboBox.setGeometry(QtCore.QRect(160, 160, 231, 22))
        self.journalComboBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.journalComboBox.setObjectName("journalComboBox")
        self.journalComboBox.addItem("")
        self.yearLabel = QtWidgets.QLabel(self.centralwidget)
        self.yearLabel.setGeometry(QtCore.QRect(430, 160, 41, 21))
        self.yearLabel.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.yearLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.yearLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearLabel.setObjectName("yearLabel")
        self.yearComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.yearComboBox.setGeometry(QtCore.QRect(480, 160, 69, 22))
        self.yearComboBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.yearComboBox.setObjectName("yearComboBox")
        self.yearComboBox.addItem("")
        self.numpaperLabel = QtWidgets.QLabel(self.centralwidget)
        self.numpaperLabel.setGeometry(QtCore.QRect(560, 160, 161, 21))
        self.numpaperLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.numpaperLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.numpaperLabel.setObjectName("numpaperLabel")
        self.upperLabel = QtWidgets.QLabel(self.centralwidget)
        self.upperLabel.setGeometry(QtCore.QRect(170, 290, 41, 21))
        self.upperLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.upperLabel.setObjectName("upperLabel")
        self.lowerLabel = QtWidgets.QLabel(self.centralwidget)
        self.lowerLabel.setGeometry(QtCore.QRect(170, 330, 41, 21))
        self.lowerLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.lowerLabel.setObjectName("lowerLabel")
        self.stepLabel = QtWidgets.QLabel(self.centralwidget)
        self.stepLabel.setGeometry(QtCore.QRect(170, 370, 41, 21))
        self.stepLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.stepLabel.setObjectName("stepLabel")
        self.traintestButton = QtWidgets.QPushButton(self.centralwidget)
        self.traintestButton.setGeometry(QtCore.QRect(180, 420, 91, 31))
        self.traintestButton.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);\n"
"")
        self.traintestButton.setObjectName("traintestButton")
        self.numldaLabel = QtWidgets.QLabel(self.centralwidget)
        self.numldaLabel.setGeometry(QtCore.QRect(470, 330, 101, 21))
        self.numldaLabel.setStyleSheet("font: 14pt \"楷体\";")
        self.numldaLabel.setObjectName("numldaLabel")
        self.selectButton = QtWidgets.QPushButton(self.centralwidget)
        self.selectButton.setGeometry(QtCore.QRect(520, 420, 81, 31))
        self.selectButton.setStyleSheet("font: 14pt \"楷体\";\n"
"background-color: rgb(0, 170, 255);\n"
"")
        self.selectButton.setObjectName("selectButton")
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
        self.borderLabel = QtWidgets.QLabel(self.centralwidget)
        self.borderLabel.setGeometry(QtCore.QRect(60, 120, 671, 361))
        self.borderLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.borderLabel.setText("")
        self.borderLabel.setObjectName("borderLabel")
        self.hline = QtWidgets.QFrame(self.centralwidget)
        self.hline.setGeometry(QtCore.QRect(70, 240, 651, 21))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.hline.setFont(font)
        self.hline.setFrameShape(QtWidgets.QFrame.HLine)
        self.hline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.hline.setObjectName("hline")
        self.vline = QtWidgets.QFrame(self.centralwidget)
        self.vline.setGeometry(QtCore.QRect(385, 250, 21, 221))
        self.vline.setFrameShape(QtWidgets.QFrame.VLine)
        self.vline.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.vline.setObjectName("vline")
        self.promptLabel = QtWidgets.QLabel(self.centralwidget)
        self.promptLabel.setGeometry(QtCore.QRect(120, 200, 551, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.promptLabel.sizePolicy().hasHeightForWidth())
        self.promptLabel.setSizePolicy(sizePolicy)
        self.promptLabel.setStyleSheet("font: 13pt \"楷体\";")
        self.promptLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.promptLabel.setWordWrap(True)
        self.promptLabel.setObjectName("promptLabel")
        self.upperSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.upperSpinBox.setGeometry(QtCore.QRect(230, 290, 61, 22))
        self.upperSpinBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.upperSpinBox.setMinimum(1)
        self.upperSpinBox.setMaximum(10000)
        self.upperSpinBox.setObjectName("upperSpinBox")
        self.lowerSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.lowerSpinBox.setGeometry(QtCore.QRect(230, 330, 61, 22))
        self.lowerSpinBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.lowerSpinBox.setMinimum(1)
        self.lowerSpinBox.setMaximum(10000)
        self.lowerSpinBox.setObjectName("lowerSpinBox")
        self.stepSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.stepSpinBox.setGeometry(QtCore.QRect(230, 370, 61, 22))
        self.stepSpinBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.stepSpinBox.setMinimum(1)
        self.stepSpinBox.setMaximum(1000)
        self.stepSpinBox.setObjectName("stepSpinBox")
        self.numldaSpinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.numldaSpinBox.setGeometry(QtCore.QRect(590, 330, 61, 22))
        self.numldaSpinBox.setStyleSheet("font: 75 11pt \"Times New Roman\";\n"
"background-color: rgb(152, 255, 185);")
        self.numldaSpinBox.setMinimum(1)
        self.numldaSpinBox.setObjectName("numldaSpinBox")
        self.borderLabel.raise_()
        self.journalLabel.raise_()
        self.journalComboBox.raise_()
        self.yearLabel.raise_()
        self.yearComboBox.raise_()
        self.numpaperLabel.raise_()
        self.upperLabel.raise_()
        self.lowerLabel.raise_()
        self.stepLabel.raise_()
        self.traintestButton.raise_()
        self.numldaLabel.raise_()
        self.selectButton.raise_()
        self.uiLabel.raise_()
        self.hline.raise_()
        self.vline.raise_()
        self.promptLabel.raise_()
        self.upperSpinBox.raise_()
        self.lowerSpinBox.raise_()
        self.stepSpinBox.raise_()
        self.numldaSpinBox.raise_()
        Lda.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Lda)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        Lda.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Lda)
        self.statusbar.setObjectName("statusbar")
        Lda.setStatusBar(self.statusbar)

        self.retranslateUi(Lda)
        QtCore.QMetaObject.connectSlotsByName(Lda)

    def retranslateUi(self, Lda):
        _translate = QtCore.QCoreApplication.translate
        Lda.setWindowTitle(_translate("Lda", "主题词提取"))
        self.journalLabel.setText(_translate("Lda", "期刊名称"))
        self.journalComboBox.setItemText(0, _translate("Lda", "AICHE_JOURNAL"))
        self.yearLabel.setText(_translate("Lda", "年份"))
        self.yearComboBox.setItemText(0, _translate("Lda", "2018"))
        self.numpaperLabel.setText(_translate("Lda", "文章篇数：200"))
        self.upperLabel.setText(_translate("Lda", "上界"))
        self.lowerLabel.setText(_translate("Lda", "下界"))
        self.stepLabel.setText(_translate("Lda", "步长"))
        self.traintestButton.setText(_translate("Lda", "训练测试"))
        self.numldaLabel.setText(_translate("Lda", "主题个数"))
        self.selectButton.setText(_translate("Lda", "提取"))
        self.uiLabel.setText(_translate("Lda", "主题词提取"))
        self.promptLabel.setText(_translate("Lda", "<html><head/><body><p>程序运行提示信息</p></body></html>"))

