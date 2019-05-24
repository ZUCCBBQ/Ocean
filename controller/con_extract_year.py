from PyQt5.QtWidgets import QMainWindow, QMessageBox
from psutil import cpu_count
import threading
import os

from view.ui_extract_year import Ui_Year
from model.csv_year import YearExtractor


class YearController():
    # 当前文件的绝对路径
    abspath = os.path.dirname(__file__)
    # 输入数据文件夹
    input_path = abspath + '/../model/data/journal_total'
    # 输出数据文件夹
    output_path = abspath + '/../model/data/journal_year'
    # 输入数据文件夹中获取信息完成的期刊列表（动态变化）
    journals = []
    # 支持抽取信息的年份
    years = range(2010, 2019, 1)
    # 机器支持的最大线程个数
    max_threads = cpu_count()

    def __init__(self):
        # 数据属性初始化
        # 当前正在根据年份抽取信息的期刊列表,为空说明提取信息程序空闲
        self.current_journals_year = []

        # 抽取器初始化
        self.year_extractor = YearExtractor()

        # 窗口初始化
        self.window = QMainWindow()
        self.year_ui = Ui_Year()
        self.year_ui.setupUi(self.window)

        # 部件初始化
        self.year_ui.yearComboBox.clear()
        self.year_ui.yearComboBox.addItems([str(year) for year in self.years])

        # 以下是信号与槽的连接
        self.year_ui.extractButton.clicked.connect(self.extract_start)
        self.year_extractor.extract_over_msg.connect(self.extract_over)

    # 更新成功获取信息的期刊列表
    def update_journals(self):
        self.journals = []
        # 将输入数据文件夹中的文件去掉后缀名得到获取信息的期刊名
        for file in os.listdir(self.input_path):
            self.journals.append(file.replace('.csv', ''))
        # 因为并行的缘故，所以要将正在获取信息的期刊去掉
        for t in threading.enumerate():
            name = t.getName()
            if name in self.journals:
                self.journals.remove(name)
        self.year_ui.journalComboBox.clear()
        self.year_ui.journalComboBox.addItems(self.journals)

    def show_ui(self):
        self.update_journals()
        # 列表是否为空
        if len(self.current_journals_year) == 0:
            self.year_ui.promptLabel.setText("请选择一个期刊和年份以获取文章信息")
        else:
            self.year_ui.promptLabel.setText(
                "正在抽取如下期刊相应年份的文章信息,请稍后...\n" + "年\n".join(self.current_journals_year) + '年')
        self.window.show()

    def extract_start(self):
        # 查看成功获取信息的期刊列表是否为空
        if len(self.journals) == 0:
            QMessageBox.information(self.window,
                                    "温馨提示",
                                    "当前还没有成功获取信息的期刊，请先获取",
                                    QMessageBox.Ok)
            return
        # 查看线程启动数是否已满
        if (threading.active_count() == self.max_threads):
            QMessageBox.information(self.window,
                                    "温馨提示",
                                    "线程启动数已达最大值,请稍后...",
                                    QMessageBox.Ok)
            return

        # 获取期刊下拉选择框的值，即期刊名和年份
        journal = self.year_ui.journalComboBox.currentText()
        year = self.year_ui.yearComboBox.currentText()
        journal_year = journal + year
        # 查看是否正在获取该期刊的信息
        if (journal in self.current_journals_year):
            QMessageBox.information(self.window,
                                    "温馨提示",
                                    "正在抽取" + journal_year + "年的文章信息,请稍后",
                                    QMessageBox.Ok)
            return
        # 创建期刊文件夹以保存相应年份的文章信息
        os.makedirs(self.output_path + '/' + journal, exist_ok=True)
        self.current_journals_year.append(journal_year)
        self.year_ui.promptLabel.setText("正在抽取如下期刊相应年份的文章信息,请稍后...\n" + "年\n".join(self.current_journals_year) + '年')
        t = threading.Thread(target=self.year_extractor.extract_year, name=journal_year, args = (journal, year,))
        t.start()

    def extract_over(self, journal, year, num_paper):
        journal_year = journal + year
        QMessageBox.information(self.window,
                                "温馨提示",
                                "成功抽取" + journal_year + "年的信息,共抽取" + str(num_paper) + "篇文章",
                                QMessageBox.Ok)
        self.current_journals_year.remove(journal_year)
        # 列表是否为空
        if len(self.current_journals_year) == 0:
            self.year_ui.promptLabel.setText("请选择一个期刊和年份以获取文章信息")
        else:
            self.year_ui.promptLabel.setText(
                "正在抽取如下期刊相应年份的文章信息,请稍后...\n" + "年\n".join(self.current_journals_year) + '年')
