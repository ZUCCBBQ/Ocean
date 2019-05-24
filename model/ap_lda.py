from PyQt5.QtCore import QObject, pyqtSignal
from sklearn.cluster import AffinityPropagation
from scipy.spatial.distance import pdist
from scipy.spatial.distance import squareform
import pandas as pd
import numpy as np
import os
from sklearn import metrics
from sklearn import decomposition
import matplotlib.pyplot as plt
from itertools import cycle


class Cluster(QObject):
    # 主题词聚类结束信号，第一个str参数是期刊名，第二个str参数是年份，第一个int参数是聚类中心的个数，第二个int参数是聚类主题词的个数
    ap_over_msg = pyqtSignal(str, str, int, int)
    # 当前文件的绝对路径
    abspath = os.path.dirname(__file__)

    def __init__(self):
        QObject.__init__(self)

    def AP(self, word_all, word_lda_all):
        onehots = word_lda_all
        onehots = np.array(onehots)
        D = 1 - pdist(onehots, 'cosine')
        D1 = squareform(D, force="no", checks=True)
        Similarity = D1

        '''
         #similarity[0][0] = medium
        sum = np.sum(D)
        for i in range(size):
            Similarity[i][i] = sum/len(D) # sum = np.sum(D1[i])
        '''
        print("Similarity")

        preferenece = Similarity[Similarity != 0].min()
        # preferenece = np.median(Similarity)
        # for i in range(0,len(word_all)):
        #     Similarity[i][i]= 0
        #     # np.median(Similarity)
        print(preferenece)
        ap = AffinityPropagation(affinity='precomputed', max_iter=1000, damping=0.8, preference=preferenece).fit(
            Similarity)

        results = []
        words = word_all
        words = np.array(words)
        centers = []
        ida_spot = []
        num_center = len(ap.cluster_centers_indices_)
        for i in range(num_center):
            centers.append(words[ap.cluster_centers_indices_[i]])
        for i in range(num_center):
            ida_spot.append(word_lda_all[ap.cluster_centers_indices_[i]])
        for i in range(len(centers)):
            results.append([centers[i], ida_spot[i]])

        # labels = ap.labels_
        # for i in range(len(labels)):
        #     cluster = labels[i]
        #     center = centers[cluster]
        #     results.append([words[i], center])
        #     # 排序
        return (num_center, results)

    def ap_lda(self, journal, year):
        input_path = self.abspath + '/data/lda_topic/' + journal + '/'
        input_filename = year + '.txt'
        input_file = pd.read_csv(input_path + input_filename, sep='\t')
        data = input_file.values.tolist()
        # print(len(data))
        wordlist = []
        for i in data:
            topic = i[0]
            wordlist.append(topic.split(','))

        word_lda_all = []
        word_all = []
        for topic in wordlist:
            word = []
            word_lda = []
            for i in topic:
                word.append(i.split(':')[0])
                word_lda.append(float(i.split(':')[1]) * 100)
            word_all.append(word)
            word_lda_all.append(word_lda)
        (num_center, results) = self.AP(word_all, word_lda_all)
        num_ap_topic = len(results)
        output_path = self.abspath + '/data/ap_lda/' + journal + '/'
        output_filename = year + '.csv'
        with open(output_path + output_filename, 'w', newline='', encoding='UTF-8') as f:
            for item in results:
                topic = item[0]
                ida_r = item[1]
                for j in range(0, len(topic)):
                    topic_csv = topic[j] + ',' + str(ida_r[j])
                    f.write(topic_csv + '\n')
        self.ap_over_msg.emit(journal, year, num_center, num_ap_topic)
