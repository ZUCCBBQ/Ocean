# Ocean<br/>
Ocean project<br/>
scrapy文件夹下是所有的爬虫程序，一个文件对应一个网站的爬虫，网站结构不同需要的爬虫文件就不一样。但是期刊类的网站，结构差不多。<br/>
爬取文章的标题，作者列表，时间，摘要这四个信息。<br/>
爬取好的内容存成csv文件<br/>

csv_year.py是将爬取后的csv结果保存按年份分开的文件<br/>
LDA_2.py是lda主题抽取的程序，结果保存成txt文件<br/>
ap_lda.py是进行ap聚类的文件<br/>

将ap聚类的结果放到 wordart网站上就可以画出比较好的词云了<br/>

过程中的csv文件比较大我就没有上传<br/>

注:这些程序有些部分 需要手动修改，可能无法直接运行。<br/>
文件保存地址<br/>
爬虫中的网站<br/>
csv按照年份分开时的读取<br/>
lda的结果保存（训练与结果的保存不是同时进行的））<br/>
就是程序中注释掉的部分更换一下就可以直接跑了<br/>
# readme的格式我明天再改一下<br/>
