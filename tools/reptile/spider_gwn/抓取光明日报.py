import requests
import time
from bs4 import BeautifulSoup
import fake_useragent
import re
import os
import datetime

ua = fake_useragent.UserAgent()
# date的格式为XXXX-YY/ZZ
date = str(datetime.date.today()).replace("-", "/").replace("/", "-", 1)
channelMap = {
    "1": "politics",
    "2": "world",
    "3": "guancha",
    "4": "theory",
    "5": "culture",
    "6": "tech",
    "7": "edu",
    "8": "economy",
    "9": "life",
    "10": "legal",
    "11": "mil",
    "12": "health",
    "13": "jiankang",
    "14": "lady",
    "15": "e",
    "q": "quit",
}


def create_root(date: str):
    # 创建当日新闻文件夹
    dateFormat = date.replace("-", "").replace("/", "")
    wsPath = os.path.dirname(__file__)
    targetPath = wsPath + "\\" + dateFormat
    if dateFormat not in os.listdir(wsPath):
        os.mkdir(targetPath)
    return targetPath


def create_dir(channel: str, rootPath: str):
    # 创建频道文件夹
    targetPath = rootPath + "\\" + channel
    if channel not in os.listdir(rootPath):
        os.mkdir(targetPath)
    return targetPath


def channel_url(channel: str) -> str:
    # 获取需要查询的板块url信息
    root = dateDirPath
    return "https://" + channel + ".gmw.cn"


def collect_urls(url: str, date: str):
    # 收集内链网址并以列表形式返回
    urls = []
    headers = {"User-Agent": str(ua.random)}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    raw_weblinks = soup.find_all("a")
    weblinks = [weblink.get("href") for weblink in raw_weblinks]
    for weblink in weblinks:
        if (weblink != None) and (weblink.find(date) != -1):
            urls.append(weblink)
    # 相对路径转绝对路径
    absUrls = []
    for x in urls:
        if x.find("https") == -1:
            x = url + "/" + x
            absUrls.append(x)
    return set(absUrls)


def spider_channel(urls: list, dirPath: str):
    # 爬取网页链接中的文章内容
    headers = {"User-Agent": str(ua.random)}
    newscount = 0
    for url in urls:
        res = requests.get(url, headers=headers)
        res.encoding = "utf-8"
        soup = BeautifulSoup(res.text, "html.parser")
        newscount += 1
        with open(
            dirPath + "/" + "news" + str(newscount) + ".txt", "w", encoding="UTF-8"
        ) as f:
            # 写入题目
            title = soup.find("h1", class_="u-title").text
            title = "题目：" + title.strip() + "\n"
            f.write(title)
            # 写入正文
            mainText = soup.find_all("div", class_="u-mainText")
            for item in mainText:
                texts = item.find_all("p")
            for tex in texts:
                word = tex.text
                cleaned_word = "".join(word.split())
                cleaned_word = "".join(cleaned_word.split("\n"))
                cleaned_word = "".join(re.sub(r"[\r\n\t\f\v]+", "", word))
                f.write(cleaned_word)
        f.close()


# 程序入口
if __name__ == "__main__":
    while 1:
        channel = channelMap[
            input(
                "请输入序号选择频道：\n1.时政\n2.国际\n3.时评\n4.理论\n5.文化\n6.科技\n7.教育\n8.经济\n9.生活\n10.法治\n11.军事\n12.卫生\n13.健康\n14.女人\n15.卫文娱\n输入 q 退出\n"
            )
        ]
        if channel == "quit":
            break
        else:
            print("正在爬取，请等待...")
            dateDirPath = create_root(date)
            channelDirPath = create_dir(channel, dateDirPath)
            channelUrl = channel_url(channel)
            weblinks = collect_urls(channelUrl, date)
            if len(weblinks) == 0:
                print("当日该频道下无新闻")
            else:
                spider_channel(weblinks, channelDirPath)
                print("爬取结束，文件已生成在", channel, "文件夹")
                time.sleep(3)
    pass
