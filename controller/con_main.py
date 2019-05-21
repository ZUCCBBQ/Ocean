from PyQt5.QtWidgets import QMainWindow
import os

from view.ui_main_window import Ui_MainUi
from .con_obtain_journal import JournalController
from .con_extract_year import YearController

class MainController():


    def __init__(self):
        # 主窗体初始化
        self.main_window = QMainWindow()
        self.main_ui = Ui_MainUi()
        self.main_ui.setupUi(self.main_window)

        # 从控制器初始化
        self.journal_controller = JournalController()
        self.year_controller = YearController()

        # 以下是信号与槽的连接
        self.main_ui.journalButton.clicked.connect(self.journal_controller.show_ui)
        self.main_ui.yearButton.clicked.connect(self.year_controller.show_ui)
        self.journal_controller.obtain_over_msg.connect(self.year_controller.update_journals)


    def show_ui(self):
        self.main_window.show()


