from bs4 import BeautifulSoup
from urllib.request import urlopen
import time
import csv
import requests
import random
from FreeProxy.proxytool import proxytool
from fake_useragent import UserAgent
import os
abspath = os.path.dirname(__file__)

def get_ip():
    ip_list = proxytool().get(num=1)
    ip_touple = ip_list[0]
    ip_head = ip_touple[0]
    ip_last = ip_touple[1]
    proxy_info = {'host': ip_head, 'port': ip_last}
    return proxy_info

def get(str,csv_write,HEADERS,out,proxy_info):
	row = []
	result_req = requests.get(str, headers=HEADERS,proxies=proxy_info)
	resultsoup = BeautifulSoup(result_req.text, features='lxml')
	title = resultsoup.find('h1', {"class":"ArticleTitle"})
	authors = resultsoup.find_all('span', {"class":"authors__name"})
	abstract_a = resultsoup.find('p', {"class":"Para"})
	time = resultsoup.find_all('time')
	if title is None :
		title = 'null'
		row.append(title)
	else:
		row.append(title.get_text())
	if len(authors) == 0:
		author_list = 'null'
		row.append(author_list)
	else:
		author_list = authors[0].get_text()
		for j in range(1,len(authors)):
			author_list=author_list+' '+authors[j].get_text()
		row.append(author_list)
	if len(time)<2:
		time = 'null'
		row.append(time)
	else:
		row.append(time[1].get_text())
	if abstract_a is None :
		abstract_a = 'null'
		row.append(abstract_a)
	else:
		row.append(abstract_a.get_text())
	print(row)
	csv_write.writerow(row)
	out.flush()

def if_have_next(Volumeurl,HEADERS,proxies2):
	Volume_req = requests.get(Volumeurl[-1], headers=HEADERS,proxies=proxies2)
	Volumesoup = BeautifulSoup(Volume_req.text, features='lxml')
	next = Volumesoup.find('a',{'class':'next'})
	return next


# url获取
def obtain_info():
	baseurl = "https://link.springer.com"
	list = ["Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
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
	# ua.update()
	# ua = ua.random
	HEADERS = {"User-Agent": ua}
	print(len(HEADERS))
	out = open(abspath + "/../data/journal_total/China_OE.csv", 'w', newline='', encoding='UTF-8')
	csv_write = csv.writer(out, dialect='excel')
	Article_sort = []
	# (33) 32 25
	count = 0
	proxies2 = get_ip()
	# for i in range (33,32,-1):
	#	for j in range(1,2):
	Volumeurl = []
	firstone = 'https://link.springer.com/journal/13344/33/1'
	Volumeurl.append(firstone)
	next = firstone
	#		count = count+1
	#		if count % 5 == 0:
	#			proxies2 = get_ip()
	#		else:
	#			pass
	while next is not None:
		next = if_have_next(Volumeurl, HEADERS, proxies2)
		if next is None:
			continue
		else:
			Volumeurl.append(baseurl + next.get('href'))
	if len(Volumeurl) > 1:
		for t in Volumeurl:
			Volume_req = requests.get(t, headers=HEADERS, proxies=proxies2)
			time.sleep(0.5)
			Volumesoup = BeautifulSoup(Volume_req.text, features='lxml')
			Article = Volumesoup.find_all('h3', {"class": "title"})
			for m in Article:
				Articleurl = m.find_all('a')
				for a in Articleurl:
					Article_sort.append(a.get('href'))
	else:
		Volume_req = requests.get(firstone, headers=HEADERS, proxies=proxies2)
		Volumesoup = BeautifulSoup(Volume_req.text, features='lxml')
		Article = Volumesoup.find_all('h3', {"class": "title"})
		for m in Article:
			Articleurl = m.find_all('a')
			for a in Articleurl:
				Article_sort.append(a.get('href'))
	# time.sleep(0.5)

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
		get(url_art, csv_write, HEADERS, out, proxies3)
		time.sleep(0.5)
	print('over')
	out.close()

if __name__ == '__main__':
	obtain_info()
