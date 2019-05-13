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

# 程序说明：<br/>
## 爬虫部分的程序<br/>
在获取每一篇文章的网站的时候，会出现二级目录，因为是按照时间发表期刊的，所以会要求先获得某一时间的期刊，再获取这个时间期刊的文章，所以会出现二级目录。<br/>
在程序中，会发现有一个二级嵌套的for循环，在上面会出现一些注释，这就是调整是用二级目录还是直接用当前网页的模块。<br/>
如果想看原始网页的话：程序中会出现一个requese.get ....... format的部分，这里的网址复制下来，把{}替换成for循环的数字就可以了。<br/>

## csv_year:<br/>
这一部分就是要把对应的输入文件一个一个手动更换注释来执行，输入的期刊不一样，导致我要一个一个手动的跟换输入的期刊。其实很好理解的。<br/>
还有一个就是按照年份划分的话，意味着我要参考爬虫结果的年份的对吧，所以有些爬虫结果的年份在第2列，有的在第3列，那就对应了我在每个输入文件的后面的注释2和3，按照这个改变下面年份所在的列就可以了，（注意数组下表会减一所以2对应的数组下标是1,3对应的是2)，要是觉得手动比较麻烦，可以自己改成自动的，我觉得没什么影响就没改。<br/>
## lda <br/>
这里的话就是要注意先训练，查看一个比较好的结果，就是记录比较好的结果的参数，然后去训练最后的结果，可以先稍微看一下模型（我也没看懂模型），了解什么是困惑度。困惑度越小模型越好。注释（输出）上面是模型训练，下面是输出结果。更换注释的地方就可以了。<br/>
## ap聚类<br/>
这里还是一样，ap参数只需要调preference和阻尼系数。preference对应的是相似度矩阵的对角线的值，越大聚类个数越多，越小聚类个数越少。一般少一点比较好。值的选择一般是中位数或者最小值，我这里有0，所以用的是非0最小值。模型好坏的参考是第一看聚类中心有没有重复的，第二看聚类中心的个数。<br/>
### 先这样想起来再补充


