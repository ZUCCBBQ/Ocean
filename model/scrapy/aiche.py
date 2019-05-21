from bs4 import BeautifulSoup
from FreeProxy.proxytool import proxytool
from fake_useragent import UserAgent
from PyQt5.QtCore import QObject, pyqtSignal
import csv
import requests
import random
import re
import time
import os


class AicheCrawler(QObject):
    journal_name = "AICHE_JOURNAL"
    # 获取信息结束信号，int参数是获取文章的篇数，str参数是期刊名
    obtain_over_msg = pyqtSignal(int ,str)
    # 当前文件的绝对路径
    abspath = os.path.dirname(__file__)

    def get_ip(self):
        ip_list = proxytool().get(num=1)
        ip_touple = ip_list[0]
        ip_head = ip_touple[0]
        ip_last = ip_touple[1]
        proxy_info = {'host': ip_head, 'port': ip_last}
        return proxy_info

    def get(self, str, HEADERS, csv_write, out, proxy_info):
        row = []
        result_req = requests.get(str, headers=HEADERS, proxies=proxy_info)
        resultsoup = BeautifulSoup(result_req.text, features='lxml')
        title = resultsoup.find('h2', {"class": "citation__title"})

        name_find = resultsoup.find('div', {'class', 'accordion-tabbed'})
        abstract_a = resultsoup.find('div', {"class": "article-section__content en main"})
        time = resultsoup.find('span', {"class": "epub-date"})

        if title is None:
            title = 'null'
            row.append(title)
        else:
            row.append(title.get_text())

        if name_find is None:
            author_list = 'null'
            row.append(author_list)
        else:
            span = name_find.find_all('span')
            author_list = ''
            for i in span:
                name = i.get_text()
                if re.search('E-mail', name) is None:
                    if author_list == '':
                        author_list = name
                    else:
                        author_list = author_list + ';' + name
                else:
                    pass
            row.append(author_list)
        if time is None:
            timeresult = 'null'
            row.append(timeresult)
        else:
            row.append(time.get_text())
        if abstract_a is None:
            abstract_b = 'null'
            row.append(abstract_b)
        else:
            abstract_b = abstract_a.find('p')
            row.append(abstract_b.get_text())
        print(row)
        csv_write.writerow(row)
        out.flush()

    # def if_have_next(Volumeurl):
    # 	proxies2 = get_random_ip(ip_list)
    # 	Volume_req = requests.get(Volumeurl[-1], headers=HEADERS,proxies=proxies2)
    # 	Volumesoup = BeautifulSoup(Volume_req.text, features='lxml')
    # 	next = Volumesoup.find('a',{'class':'next'})
    # 	return next

    def obtain_info(self):
        baseurl = "https://onlinelibrary.wiley.com"
        list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
            "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
            "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"]
        ua = random.choice(list)
        # ua = UserAgent(verify_ssl=False)
        # ua = ua.random
        HEADERS = {"User-Agent": ua}
        out = open(self.abspath + "/../data/journal_total/AICHE_JOURNAL.csv", 'w', newline='', encoding='UTF-8')
        csv_write = csv.writer(out, dialect='excel')
        Article_sort = []
        # 56 (65)
        # 12
        count = 0
        proxies2 = self.get_ip()
        # v+1954是年份，v是卷号， i是期号
        for v in range(64, 63, -1):
            for i in range(1, 12):
                count = count + 1
                firstone = 'https://onlinelibrary.wiley.com/toc/15475905/{0}/{1}/{2}'.format(v + 1954, v, i)
                if count % 5 == 0:
                    proxies2 = self.get_ip()
                else:
                    pass
                print(proxies2)
                Volume_req = requests.get(firstone, headers=HEADERS, proxies=proxies2)
                Volumesoup = BeautifulSoup(Volume_req.content, features='lxml')
                article = Volumesoup.find_all('a', {'class', 'issue-item__title visitable'})
                for t in range(2, len(article)):
                    Article_sort.append(article[t].get('href'))
                time.sleep(0.5)

        num = 0
        proxies3 = self.get_ip()
        for i in range(0, len(Article_sort)):
            num = num + 1
            print(num)
            url_art = baseurl + Article_sort[i]
            print(url_art)
            if num % 5 == 0:
                proxies3 = self.get_ip()
            else:
                pass
            self.get(url_art, HEADERS, csv_write, out, proxies3)
            time.sleep(0.5)
        print('over')
        out.close()
        # 获取信息结束，发送结束信号
        self.obtain_over_msg.emit(num, self.journal_name)
