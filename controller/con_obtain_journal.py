from PyQt5.QtWidgets import QWidget

from model.scrapy import aiche, Applied_Mechanics, china_OE
from view.obtain_journal import Ui_Form


class JournalController():
    def __init__(self):
        self.widget = QWidget()
        self.journal_ui = Ui_Form()
        self.journal_ui.setupUi(self.widget)

        # 以下是信号与槽的连接
        self.journal_ui.obtainButton.clicked.connect(self.obtain_journal_info)
        self.journal_ui.backButton.clicked.connect(self.hide_ui)

    def show_ui(self):
        self.widget.show()

    def hide_ui(self):
        self.widget.hide()

    def obtain_journal_info(self):
        # 获取期刊下拉选择框的值
        print("begin get func")
        joural_name = "AICHE_JOURNAL"
        get_func = {
            "AICHE_JOURNAL": aiche.obtain_info,
            "Applied_Mechanics": Applied_Mechanics.obtain_info,
            "China_OE": china_OE.obtain_info
        }

        try:
            print("before obtain_info")
            get_func[joural_name]()
        except KeyError:
            pass

