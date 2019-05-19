from PyQt5.QtWidgets import QMainWindow

from view.main_window import Ui_MainWindow
from .con_obtain_journal import JournalController

class MainController():
    def __init__(self):
        # 主窗体初始化
        self.main_window = QMainWindow()
        self.main_ui = Ui_MainWindow()
        self.main_ui.setupUi(self.main_window)

        # 从控制器初始化
        self.journal_controller = JournalController()

        # 以下是信号与槽的连接
        self.main_ui.journalButton.clicked.connect(self.journal_controller.show_ui)
        self.main_ui.journalButton.clicked.connect(self.hide_ui)
        self.journal_controller.journal_ui.backButton.clicked.connect(self.show_ui)

    def show_ui(self):
        self.main_window.show()

    def hide_ui(self):
        self.main_window.hide()

