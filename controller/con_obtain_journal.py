from PyQt5.QtWidgets import QWidget

from model.scrapy import aiche, Applied_Mechanics, china_OE
from view.obtain_journal import Ui_Journal
import threading


class JournalController():


    def __init__(self):
        # 窗口初始化
        self.widget = QWidget()
        self.journal_ui = Ui_Journal()
        self.journal_ui.setupUi(self.widget)

        # 部件初始化
        journals = ["AICHE_JOURNAL", "Applied_Mechanics", "China_OE"]
        self.journal_ui.journalBox.addItems(journals)

        # 以下是信号与槽的连接
        self.journal_ui.obtainButton.clicked.connect(self.obtain_journal_info)
        self.journal_ui.backButton.clicked.connect(self.hide_ui)

    def show_ui(self):
        self.widget.show()

    def hide_ui(self):
        self.widget.hide()

    def obtain_journal_info(self):
        # 获取期刊下拉选择框的值，即期刊名
        joural_name = self.journal_ui.journalBox.currentText()
        # 查看当前是否有线程正在执行期刊对应的爬虫
        thread_list = threading.enumerate()
        print("begin get func " + joural_name)
        get_func = {
            "AICHE_JOURNAL": aiche.obtain_info,
            "Applied_Mechanics": Applied_Mechanics.obtain_info,
            "China_OE": china_OE.obtain_info
        }

        try:
            t = threading.Thread(target=get_func[joural_name], name=joural_name)
            print("before obtain_info")
            t.start()
        except KeyError:
            pass
