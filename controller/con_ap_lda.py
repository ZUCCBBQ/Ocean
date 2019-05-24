from PyQt5.QtWidgets import QMainWindow, QMessageBox
from psutil import cpu_count
import threading
import os

from view.ui_ap_lda import Ui_Ap
from model.ap_lda import Cluster


class ApController():
    # 当前文件的绝对路径
    abspath = os.path.dirname(__file__)
    # 输入数据文件夹
    input_path = abspath + '/../model/data/lda_topic'
    # 输出数据文件夹
    output_path = abspath + '/../model/data/ap_lda'
    # 输入数据文件夹中完成信息抽取的期刊列表（动态变化）
    journals = []
    # 输入数据文件夹中完成信息抽取的年份列表（动态变化）
    years = []
    # 机器支持的最大线程个数
    max_threads = cpu_count()

    def __init__(self):
        # 数据属性初始化
        # 正在根据年份进行主题词聚类的期刊列表,为空说明聚类程序空闲
        self.current_journals_year = []

        # 聚类器初始化
        self.cluster = Cluster()

        # 窗口初始化
        self.window = QMainWindow()
        self.ap_ui = Ui_Ap()
        self.ap_ui.setupUi(self.window)

        # 部件初始化

        # 以下是信号与槽的连接
        self.ap_ui.journalComboBox.currentIndexChanged.connect(self.update_years)
        self.ap_ui.yearComboBox.currentIndexChanged.connect(self.update_num_topics)
        self.ap_ui.apButton.clicked.connect(self.ap_start)
        self.cluster.ap_over_msg.connect(self.ap_over)

    # 更新成功获取年份信息的期刊列表
    def update_journals(self):
        self.journals = []
        # 从输入数据文件夹中得到成功获取年份信息的期刊名
        for journal in os.listdir(self.input_path):
            self.journals.append(journal)
        self.ap_ui.journalComboBox.clear()
        self.ap_ui.journalComboBox.addItems(self.journals)

    # 更新期刊获取信息成功的年份列表
    def update_years(self):
        self.years = []
        journal = self.ap_ui.journalComboBox.currentText()
        if journal == '':
            return
        for year in os.listdir(self.input_path + '/' + journal):
            self.years.append(year.replace('.txt', ''))
        self.ap_ui.yearComboBox.clear()
        self.ap_ui.yearComboBox.addItems(self.years)

    # 设置年份文件中的主题词个数
    def update_num_topics(self):
        journal = self.ap_ui.journalComboBox.currentText()
        year = self.ap_ui.yearComboBox.currentText()
        if year == '':
            return
        lines = open(self.input_path + '/' + journal + '/' + year + '.txt', 'r', encoding='UTF-8').readlines()
        count = 0
        for line in lines:
            count += len(line.split(','))
        self.ap_ui.numTopicLabel.setText('主题词个数：' + str(count))

    def show_ui(self):
        self.update_journals()
        # 列表是否为空
        if len(self.current_journals_year) == 0:
            self.ap_ui.promptLabel.setText("请选择一个期刊和年份以进行主题词的聚类")
        else:
            self.ap_ui.promptLabel.setText(
                "正在对如下期刊相应年份的文章信息进行主题词聚类,请稍后...\n" + "年\n".join(self.current_journals_year) + '年')
        self.window.show()

    def ap_start(self):
        # 查看完成主题词提取的期刊列表是否为空
        if len(self.journals) == 0:
            QMessageBox.information(self.window,
                                    "温馨提示",
                                    "当前还没有完成主题词提取的期刊，请先抽取",
                                    QMessageBox.Ok)
            return
        # 查看完成主题词提取的年份列表是否为空
        if len(self.years) == 0:
            QMessageBox.information(self.window,
                                    "温馨提示",
                                    "当前期刊还没有完成主题词提取的年份，请先抽取",
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
        journal = self.ap_ui.journalComboBox.currentText()
        year = self.ap_ui.yearComboBox.currentText()
        journal_year = journal + year
        # 查看是否正在获取该期刊的信息
        if (journal in self.current_journals_year):
            QMessageBox.information(self.window,
                                    "温馨提示",
                                    "正在对" + journal_year + "年文章信息的主题词进行聚类,请稍后",
                                    QMessageBox.Ok)
            return
        # 创建期刊文件夹以保存相应年份的文章信息
        os.makedirs(self.output_path + '/' + journal, exist_ok=True)
        self.current_journals_year.append(journal_year)
        self.ap_ui.promptLabel.setText("正在对如下期刊相应年份的主题词进行聚类,请稍后...\n" + "年\n".join(self.current_journals_year) + '年')
        t = threading.Thread(target=self.cluster.ap_lda, name=journal_year, args=(journal, year,))
        t.start()

    def ap_over(self, journal, year, num_center, num_ap_topic):
        journal_year = journal + year
        QMessageBox.information(self.window,
                                "温馨提示",
                                "对" + journal + year + "年文章信息的主题词聚类成功\n聚类中心个数：" + str(num_center) + '\n聚类主题词个数：' + str(num_ap_topic),
                                QMessageBox.Ok)
        self.current_journals_year.remove(journal_year)
        # 列表是否为空
        if len(self.current_journals_year) == 0:
            self.ap_ui.promptLabel.setText("请选择一个期刊和年份以进行主题词的聚类")
        else:
            self.ap_ui.promptLabel.setText(
                "正在对如下期刊相应年份的文章信息进行主题词聚类,请稍后...\n" + "年\n".join(self.current_journals_year) + '年')
