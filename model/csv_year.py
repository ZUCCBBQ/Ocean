from PyQt5.QtCore import QObject, pyqtSignal
import csv
import os


class YearExtractor(QObject):
    # 抽取信息结束信号，第一个str参数是期刊名，第二个str参数是年份，int参数是抽取文章的篇数
    extract_over_msg = pyqtSignal(str, str, int)
    # 当前文件的绝对路径
    abspath = os.path.dirname(__file__)

    # input_filename = 'aaa_final.csv' #2
    # input_filename = 'AIAA.csv' #2
    # input_filename = 'AICHE_JOURNAL.csv'  # 2
    # input_filename = 'Applied_Mechanics.csv' #2
    # input_filename = 'applied_physics.csv' #2
    # input_filename = 'China_OE.csv' #2
    # input_filename = 'Hydrodynamics.csv' #2
    # input_filename = 'Marine_Science.csv' #2
    # input_filename = 'China_Technological.csv' #2

    # input_filename = 'Computers_Fluids.csv' #3
    # input_filename = 'Computional_Physics.csv' #3
    # input_filename = 'Engineering_Structures.csv' #3
    # input_filename = 'fluids_and_structures_final.csv' #3
    # input_filename = 'OceanEngineering_final.csv' #3
    def extract_year(self, journal, year):
        input_path = self.abspath + '/data/journal_total/'
        input_filename = journal + '.csv'
        input_file = csv.reader(open(input_path + input_filename, 'r', encoding='UTF-8'))
        input_list = list(input_file)
        # for i in range(0,100):
        #     if '2019' in input_list[i][2]:
        #         print('2019'+input_list[i][2])
        #     else:
        #         print(input_list[i][2])
        output_path = self.abspath + '/data/journal_year/' + journal + '/'
        output_filename = year + '.csv'
        with open(output_path + output_filename, 'w', newline='', encoding='UTF-8') as f:
            writer = csv.writer(f)
            count = 0
            num = 0
            for i in range(0, len(input_list)):
                count = count + 1
                if year in input_list[i][2]:
                    num = num + 1
                    writer.writerow(input_list[i])
                else:
                    pass
        # 抽取信息结束，发送结束信号
        self.extract_over_msg.emit(journal, year, num)
