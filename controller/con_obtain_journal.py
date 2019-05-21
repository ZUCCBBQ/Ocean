from PyQt5.QtWidgets import QMainWindow, QMessageBox
from PyQt5.QtCore import QObject, pyqtSignal
from psutil import cpu_count
import threading
import os

from model.scrapy import aiche, Applied_Mechanics, china_OE
from view.ui_obtain_journal import Ui_Journal


class JournalController(QObject):
    # 当前文件的绝对路径
    abspath = os.path.dirname(__file__)
    # 创建数据文件夹
    output_path = abspath + '/../model/data/journal_total'
    os.makedirs(output_path, exist_ok=True)
    # 支持获取信息的期刊列表
    journals = ["AICHE_JOURNAL", "Applied_Mechanics", "China_OE"]
    # 机器支持的最大线程个数
    max_threads = cpu_count()
    # 获取信息结束信号
    obtain_over_msg = pyqtSignal()

    def __init__(self):
        QObject.__init__(self)
        # 数据属性初始化
        # 当前正在获取信息的期刊列表,为空说明获取信息程序空闲
        self.current_journals = []

        # 爬虫对象初始化
        self.aiche_crawler = aiche.AicheCrawler()
        self.chine_oe_crawler = china_OE.ChineOECrawler()
        self.applied_mechanics_crawler = Applied_Mechanics.AppliedMechanicsCrawler()

        # 爬虫程序入口
        self.get_func = {
            "AICHE_JOURNAL": self.aiche_crawler.obtain_info,
            "Applied_Mechanics": self.applied_mechanics_crawler.obtain_info,
            "China_OE": self.chine_oe_crawler.obtain_info
        }

        # 窗口初始化
        self.window = QMainWindow()
        self.journal_ui = Ui_Journal()
        self.journal_ui.setupUi(self.window)

        # 部件初始化
        self.journal_ui.jounralComboBox.clear()
        self.journal_ui.jounralComboBox.addItems(self.journals)

        # 以下是信号与槽的连接
        self.journal_ui.obtainButton.clicked.connect(self.obtain_start)
        self.aiche_crawler.obtain_over_msg.connect(self.obtain_over)
        self.chine_oe_crawler.obtain_over_msg.connect(self.obtain_over)
        self.applied_mechanics_crawler.obtain_over_msg.connect(self.obtain_over)

    def show_ui(self):
        # current_journal列表是否为空
        if len(self.current_journals) == 0:
            self.journal_ui.promptLabel.setText("请选择一个期刊以获取信息")
        else:
            self.journal_ui.promptLabel.setText("正在获取如下期刊的信息,请稍后...\n" + "\n".join(self.current_journals))
        self.window.show()

    def obtain_start(self):
        # 查看线程启动数是否已满
        if (threading.active_count() == self.max_threads):
            QMessageBox.information(self.window,
                                    "温馨提示",
                                    "线程启动数已达最大值,请稍后...",
                                    QMessageBox.Ok)
            return

        # 获取期刊下拉选择框的值，即期刊名
        journal = self.journal_ui.jounralComboBox.currentText()
        # 查看是否正在获取该期刊的信息
        if (journal in self.current_journals):
            QMessageBox.information(self.window,
                                    "温馨提示",
                                    "正在获取" + journal + "期刊的信息,请稍后",
                                    QMessageBox.Ok)
            return

        self.current_journals.append(journal)
        self.journal_ui.promptLabel.setText("正在获取如下期刊的信息,请稍后...\n" + "\n".join(self.current_journals))
        t = threading.Thread(target=self.get_func[journal], name=journal)
        t.start()

    def obtain_over(self, num_paper, journal):
        QMessageBox.information(self.window,
                                "温馨提示",
                                "成功获取" + journal + "期刊的信息,共获取" + str(num_paper) + "篇文章",
                                QMessageBox.Ok)
        self.current_journals.remove(journal)
        # current_journal列表是否为空
        if len(self.current_journals) == 0:
            self.journal_ui.promptLabel.setText("请选择一个期刊以获取信息")
        else:
            self.journal_ui.promptLabel.setText("正在获取如下期刊的信息,请稍后...\n" + "\n".join(self.current_journals))
        self.obtain_over_msg.emit()
