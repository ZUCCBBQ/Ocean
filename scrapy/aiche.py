from bs4 import BeautifulSoup
import csv
import requests
import random
from FreeProxy.proxytool import proxytool
from fake_useragent import UserAgent
import re 
import time
def get_ip():
    ip_list = proxytool().get(num=1)
    ip_touple = ip_list[0]
    ip_head = ip_touple[0]
    ip_last = ip_touple[1]
    proxy_info = {'host': ip_head, 'port': ip_last}
    return proxy_info

def get(str,HEADERS,csv_write,out,proxy_info):
	row = []
	result_req = requests.get(str, headers=HEADERS,proxies=proxy_info)
	resultsoup = BeautifulSoup(result_req.text, features='lxml')
	title = resultsoup.find('h2', {"class":"citation__title"})

	name_find = resultsoup.find('div', {'class', 'accordion-tabbed'})
	abstract_a = resultsoup.find('div', {"class":"article-section__content en main"})
	time = resultsoup.find('span',{"class":"epub-date"})
	
	
	if title is None :
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
			if re.search('E-mail',name) is None:
				if author_list == '':
					author_list = name
				else:
					author_list = author_list +';'+ name
			else:
				pass
		row.append(author_list)
	if time is None:
		timeresult = 'null'
		row.append(timeresult)
	else:
		row.append(time.get_text())
	if abstract_a is None :
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

def obtain_info():
    baseurl = "https://onlinelibrary.wiley.com"
    ua = UserAgent(verify_ssl=False)
    ua = ua.random
    HEADERS = {"User-Agent": ua}
    out = open("../data/journal_total/AICHE_JOURNAL.csv", 'w', newline='')
    csv_write = csv.writer(out, dialect='excel')
    Article_sort = []
    # 56 (65)
    # 12
    count = 0
    proxies2 = get_ip()
    # for i in range (65,56,-1):
    for j in range(1, 4):
        count = count + 1
        firstone = 'https://onlinelibrary.wiley.com/toc/15475905/2019/65/{0}'.format(j)
        if count % 5 == 0:
            proxies2 = get_ip()
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
    proxies3 = get_ip()
    for i in range(0, len(Article_sort)):
        num = num + 1
        print(num)
        url_art = baseurl + Article_sort[i]
        print(url_art)
        if num % 5 == 0:
            proxies3 = get_ip()
        else:
            pass
        get(url_art, HEADERS, csv_write, out, proxies3)
        time.sleep(0.5)
    print('over')
    out.close()

if __name__ == '__main__':
	obtain_info()
