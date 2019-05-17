from bs4 import BeautifulSoup
from urllib.request import urlopen

import csv
import requests
import random
from FreeProxy.proxytool import proxytool

# def get_ip_list(url, headers):
#     web_data = requests.get(url, headers=headers)
#     soup = BeautifulSoup(web_data.text, 'lxml')
#     ips = soup.find_all('tr')
#     ip_list = []
#     for i in range(1, len(ips)):
#         ip_info = ips[i]
#         tds = ip_info.find_all('td')
#         ip_list.append(tds[1].text + ':' + tds[2].text)
#     return ip_list

def get_random_ip(ip_list):
    proxy_list = []
    for ip in ip_list:
        proxy_list.append('http://' + ip)
    proxy_ip = random.choice(proxy_list)
    proxies = {'http': proxy_ip}
    return proxies

def get(str,csv_write,out,proxy_info):
	row = []

	result_req = requests.get(str, headers=HEADERS,proxies=proxy_info)
	# resulthtml = urlopen(result_req).read().decode('utf-8')
	resultsoup = BeautifulSoup(result_req.text, features='lxml')
	title = resultsoup.find('h1', {"class":"ArticleTitle"})
	authors = resultsoup.find_all('span', {"class":"authors__name"})
	abstract_a = resultsoup.find('p', {"class":"Para"})
	# print(title.get_text())
	if len(authors)==0:
		author_list = 'null'
	else:
		author_list = authors[0].get_text()
		for j in range(1,len(authors)):
			author_list=author_list+' '+authors[j].get_text()
	# print(author_list)
	# print(abstract.get_text())
	if title is None:
		title = 'null'
		row.append(title)
	else:
		row.append(title.get_text())
	row.append(author_list)
	if abstract_a is None:
		abstract_a = 'null'
		row.append(abstract_a)
	else:
		row.append(abstract_a.get_text())
	csv_write.writerow(row)
	out.flush()




# url获取


if __name__ == '__main__':
	
	baseurl="https://link.springer.com"
	user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
	url = "https://link.springer.com/journal/volumesAndIssues/11582"
	HEADERS = {"User-Agent":user_agent}
	ip_list = ['123.158.33.37:8118', '221.1.200.242:38652', '183.148.148.255:9999', '111.177.165.229:9999', '110.52.235.166:9999', '116.209.56.109:9999', '111.177.184.135:9999', '111.177.184.85:9999', '111.177.162.11:9999', '182.207.232.135:50465', '183.148.151.95:9999', '111.177.183.252:9999', '60.223.243.21:32779', '111.177.169.178:9999', '111.177.164.209:9999', '112.87.69.141:9999', '116.209.59.162:9999', '115.53.38.254:9999', '112.85.150.134:9999', '111.177.167.9:9999', '183.148.151.252:9999', '111.177.163.30:9999', '111.177.168.108:9999', '182.241.226.25:43584', '111.177.175.96:9999', '183.148.137.107:9999', '116.209.59.176:9999', '61.142.72.154:30074', '221.218.102.146:33323', '111.177.182.179:9999', '111.177.179.219:9999', '125.40.109.154:31610', '223.241.116.239:8010', '183.148.148.221:9999', '221.206.100.133:34073', '60.190.66.131:56882', '218.86.87.171:53281', '116.209.54.92:9999', '202.103.12.30:60850', '111.177.160.177:9999', '222.184.7.206:40908', '111.177.172.137:9999', '111.177.162.192:9999', '183.148.154.2:9999', '58.210.133.98:32741', '125.40.238.181:56948', '171.41.121.86:9999', '120.84.101.243:9999', '113.108.242.36:47713', '222.217.68.51:54355', '116.209.53.252:9999', '221.227.39.160:8118', '124.89.33.59:53281', '222.189.190.35:9999', '112.85.171.194:9999', '112.85.166.113:9999', '112.85.129.167:9999', '116.209.57.79:9999', '60.173.203.83:47300', '218.75.69.50:39590', '171.80.3.24:9999', '36.33.32.158:59019', '221.239.86.26:46164', '183.148.136.86:9999', '27.29.46.100:9999', '171.38.79.31:8123', '111.177.170.145:9999', '27.216.207.43:8118', '27.29.45.10:9999', '116.209.52.190:9999', '27.29.45.45:9999', '111.177.177.178:9999', '116.209.54.205:9999', '61.178.149.237:59042', '111.177.181.170:9999', '111.177.187.83:9999', '110.52.235.233:9999', '111.177.173.27:9999', '111.177.188.97:9999', '27.29.45.144:9999', '27.29.44.255:9999', '27.29.45.92:9999', '116.209.54.159:9999', '27.29.45.53:9999', '27.29.46.31:9999', '175.148.78.36:1133', '113.57.34.150:808', '27.29.46.24:9999', '116.209.56.105:9999', '180.119.141.69:9999', '61.176.223.7:58822', '118.187.58.34:53281', '111.177.171.229:9999', '111.177.166.204:9999', '112.85.171.85:9999', '106.86.208.98:41683', '60.190.250.120:8080', '27.29.45.98:9999', '59.45.13.220:35504', '111.177.183.18:9999']
	proxies = get_random_ip(ip_list)
	req = requests.get(url, headers=HEADERS,proxies=proxies)
	# html = urlopen(req).read().decode('utf-8')

	soup = BeautifulSoup(req.text, features='lxml')
	Volume = soup.find_all('a', {"class":"title"})
	out=open("/home/cbq/Desktop/scapiy/zhejiang.csv",'a',newline='')
	csv_write=csv.writer(out,dialect='excel')
	Article_sort = []
	for i in Volume:
		Volumeurl = baseurl+i.get("href")
		proxies2 = get_random_ip(ip_list)
		Volume_req = requests.get(Volumeurl, headers=HEADERS,proxies=proxies2)
		# Volumehtml = urlopen(Volume_req).read().decode('utf-8')
		Volumesoup = BeautifulSoup(Volume_req.text, features='lxml')
		Article  = Volumesoup.find_all('h3',{"class":"title"})
		for j in Article:
			Articleurl = j.find_all('a')
			for a in Articleurl:
				Article_sort.append(a.get('href'))

	num= 590
	for i in range(590,len(Article_sort)):
		num= num+1
		print(num)
		print(baseurl+Article_sort[i])
		inurl = baseurl+Article_sort[i]
		proxies3 = get_random_ip(ip_list)
		get(inurl,csv_write,out,proxies3)
	print('over')
	out.close()
