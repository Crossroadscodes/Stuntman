import requests
import time
from bs4 import BeautifulSoup
import fake_useragent
ua = fake_useragent.UserAgent()
import re

def write_news(filePath,data):#调用此函数可以完成文件写入
    with open(filePath,mode='a',encoding='utf-8') as file:
            file.write(data)
            #file.write('\n')

def get_guangming_news(url,filePath): #调用此函数获取新闻正文
    headers={'User-Agent':str(ua.random)}
    res=requests.get(url,headers=headers)
    res.encoding='utf-8'
    soup=BeautifulSoup(res.text,'html.parser')
    try:
        h1=soup.find('h1')#找到标签h1
        h1_content=h1.text
        write_news(filePath,h1_content)
        items=soup.find_all('div',class_='u-mainText')
        item_s = items
        for item in items:
            item_s=item.find_all('p')
        for i in item_s:
            word=i.text
            cleaned_word  = ''.join(word.split())
            #cleaned_word = ''.join(cleaned_word_s.split('\n'))
            #cleaned_word  = ''.join(re.sub(r'[\r\n\t\f\v]+','',word))
            write_news(filePath,cleaned_word)
    except AttributeError:
        print("该网页不含文本无法爬取") 

def collect_urls(url,date): #调用此函数收集网址并以列表形式返回
    urls=[]
    headers={'User-Agent':str(ua.random)}
    test=requests.get(url,headers=headers)
    test_soup=BeautifulSoup(test.text,'html.parser')
    url=test_soup.find_all('ul',class_='channel-newsGroup')
    for urls_ in url:
        x=urls_.find_all('a')
        for url_s in x :
            i=url_s['href']
            new_date=date[0:7]+'/'+date[-2:]
            if new_date in i:
                urls.append(i)
    return urls

def star_process(filePath,url,date,weblink):#调用此函数判断<a>标签中是否缺少内容
    print(filePath+' 准备就绪')                  #如果不完整则补全 最终调用函数爬取所有网址
    urls =collect_urls(url,date)        #抓取页面内；新闻文本超链接
    urls_count=len(urls)        #计数
    newlists=[]
    k=0
    while k < urls_count:
        if 'https' not in urls[k]:      #抓取的url链接中若无绝对路径，则加入绝对路径
            newlist=weblink+urls[k]
            newlists.append(newlist)
            k=k+1
        else:
            newlists.append(urls[k])
            k=k+1
            continue
    for newlist_ in newlists:
        get_guangming_news(newlist_,filePath)

#程序入口
date=input('请输入要爬取的日期 例如2023-08-13: ')
print('程序开始运行')
urls=[  'https://news.gmw.cn/node_23548.htm',
        'https://news.gmw.cn/node_23547.htm',
        'https://news.gmw.cn/node_23545.htm',
        'https://news.gmw.cn/node_23708.htm',
        'https://politics.gmw.cn/node_9844.htm',
        'https://politics.gmw.cn/node_9840.htm',
        'https://politics.gmw.cn/node_9831.htm',
        'https://politics.gmw.cn/node_9828.htm',
        'https://world.gmw.cn/node_4661.htm',
        'https://world.gmw.cn/node_24177.htm',
        'https://world.gmw.cn/node_4696.htm',
        'https://mil.gmw.cn/node_8986.htm',
        'https://mil.gmw.cn/node_8981.htm',
        'https://mil.gmw.cn/node_8984.htm',
        'https://mil.gmw.cn/node_8982.htm',
        'https://mil.gmw.cn/node_11177.htm'
    ]
for url in urls:
    if '23548' in url:
        filePath='D:/gmnews_spider/新闻中心时政'+date+'.txt'
        weblink='https://news.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '23547' in url:
        filePath='D:/gmnews_spider/新闻中心国际军事'+date+'.txt'
        weblink='https://news.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '23545' in url:
        filePath='D:/gmnews_spider/新闻中心经济'+date+'.txt'
        weblink='https://news.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '23708' in url:
        filePath='D:/gmnews_spider/新闻中心法治社会'+date+'.txt'
        weblink='https://news.gmw.cn/'
        star_process(filePath,url,date,weblink)
    if '9844' in url:
        filePath='D:/gmnews_spider/时政频道要闻'+date+'.txt'
        webliwnk='https://politics.gmw.cn/'
        star_process(filePath,url,date,weblink)
    if '9840' in url:
        filePath='D:/gmnews_spider/时政频道国内'+date+'.txt'
        weblink='https://politics.gmw.cn/'
        star_process(filePath,url,date,weblink)
    if '9831' in url:
        filePath='D:/gmnews_spider/时政频道权威发布'+date+'.txt'
        weblink='https://politics.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '9828' in url:
        filaPath='D:/gmnews_spider/时政频道政策解读'+date+'.txt'
        weblink='https://politics.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '4661' in url:
        filePath='D:/gmnews_spider/国际频道国际要闻'+date+'.txt'
        weblink='https://world.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '24177' in url:
        filePath='D:/gmnews_spider/国际频道光明推荐'+date+'.txt'
        weblink='https://world.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '4696' in url:
        filePath='D:/gmnews_spider/国际频道外媒聚焦'+date+'.txt'
        weblink='https://world.gmw.cn/'
        star_process(filaPath,url,date,weblink)
    elif '8986' in url:
        filePath='D:/gmnews_spider/军事频道要闻速揽'+date+'.txt'
        weblink='https://mil.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '8981' in url:
        filePath='D:/gmnews_spider/军事频道军事视点'+date+'.txt'
        weblink='https://mil.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '8984' in url:
        filePath='D:/gmnews_spider/军事频道中国军情'+date+'.txt'
        weblink='https://mil.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '8982' in url:
        filePath='D:/gmnews_spider/军事频道国际军情'+date+'.txt'
        weblink='https://mil.gmw.cn/'
        star_process(filePath,url,date,weblink)
    elif '11177' in url:
        filePath='D:/gmnews_spider/军事频道邻邦扫描'+date+'.txt'
        weblink='https://mil.gmw.cn/'
        star_process(filePath,url,date,weblink)
print('爬取结束')
