import requests
import time
from bs4 import BeautifulSoup
import fake_useragent
import re
import os
import datetime
import time
import parse
import urllib

ua = fake_useragent.UserAgent()
# # date的格式为XXXX-YY-ZZ
# date = str(datetime.date.today())
date = "2024-05-31"
# channelMap = {
#     "1": "politics",
#     "2": "world",
#     "3": "guancha",
#     "4": "theory",
#     "5": "culture",
#     "6": "tech",
#     "7": "edu",
#     "8": "economy",
#     "9": "life",
#     "10": "legal",
#     "11": "mil",
#     "12": "health",
#     "13": "jiankang",
#     "14": "lady",
#     "15": "e",
#     "q": "quit",
# }


def create_root(date: str):
    # 创建当日新闻文件夹
    dateFormat = date.replace("-", "")
    wsPath = os.path.dirname(__file__)
    targetPath = wsPath + "\\" + dateFormat
    if dateFormat not in os.listdir(wsPath):
        os.mkdir(targetPath)
    return targetPath


# def create_dir(channel: str, rootPath: str):
#     # 创建频道文件夹
#     targetPath = rootPath + "\\" + channel
#     if channel not in os.listdir(rootPath):
#         os.mkdir(targetPath)
#     return targetPath


# def channel_url(channel: str) -> str:
#     # 获取需要查询的板块url信息
#     root = dateDirPath
#     return "https://" + channel + ".gmw.cn"


# def collect_urls(url: str, date: str):
#     # 收集内链网址并以列表形式返回
#     urls = []
#     headers = {"User-Agent": str(ua.random)}
#     res = requests.get(url, headers=headers)
#     soup = BeautifulSoup(res.text, "html.parser")
#     raw_weblinks = soup.find_all("a")
#     weblinks = [weblink.get("href") for weblink in raw_weblinks]
#     for weblink in weblinks:
#         if (weblink != None) and (weblink.find(date) != -1):
#             urls.append(weblink)
#     # 相对路径转绝对路径
#     absUrls = []
#     for x in urls:
#         if x.find("https") == -1:
#             x = url + "/" + x
#             absUrls.append(x)
#     return set(absUrls)


# def spider_channel(urls: list, dirPath: str):
#     # 爬取网页链接中的文章内容
#     headers = {"User-Agent": str(ua.random)}
#     newscount = 0
#     for url in urls:
#         res = requests.get(url, headers=headers)
#         res.encoding = "utf-8"
#         soup = BeautifulSoup(res.text, "html.parser")
#         newscount += 1
#         with open(
#             dirPath + "/" + "news" + str(newscount) + ".txt", "w", encoding="UTF-8"
#         ) as f:
#             # 写入题目
#             title = soup.find("h1", class_="u-title").text
#             title = "题目：" + title.strip() + "\n"
#             f.write(title)
#             # 写入正文
#             mainText = soup.find_all("div", class_="u-mainText")
#             for item in mainText:
#                 texts = item.find_all("p")
#             for tex in texts:
#                 word = tex.text
#                 cleaned_word = "".join(word.split())
#                 cleaned_word = "".join(cleaned_word.split("\n"))
#                 cleaned_word = "".join(re.sub(r"[\r\n\t\f\v]+", "", word))
#                 f.write(cleaned_word)
#         f.close()


def write_news(content: list, file_path: str):
    with open(file_path, "w", encoding="utf-8") as f:
        for x in content:
            f.write(x)
    f.close()


def collect_urls(url: str):
    # 收集内链网址并以列表形式返回
    urls = []
    headers = {"User-Agent": str(ua.random)}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    raw_weblinks = soup.find_all("a")
    # label_a = raw_weblinks.find("a")
    weblinks = [weblink.get("href") for weblink in raw_weblinks]
    for weblink in weblinks:
        if (weblink is not None) and (date in weblink):
            urls.append(weblink)
    # 相对路径转绝对路径
    # absUrls = []
    # for x in urls:
    #     if x.find("http") == -1:
    #         x = url + "/" + x
    #         absUrls.append(x)
    # return set(absUrls)
    return urls


def spider_urls(urls: list, dirPath: str):
    news_index = 0
    for url in urls:
        news_index += 1
        filePath = dirPath + "//news" + str(news_index)
        headers = {"User-Agent": str(ua.random)}
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.text, "html.parser")
        print(soup.originalEncoding)
        title = soup.find("h1", class_="main-title")
        article = soup.find("div", class_="article")
        raw_article_contents = soup.find_all("p")
        article_contents = []
        for p in raw_article_contents:
            p = p.text

            # p = str(p, encoding="utf-8")
            # p = p.encode("unicode_escape")
            # p = p.decode("utf-8").replace("\\x", "%")
            # p = urllib.parse.unquote(p)
            article_contents.append(p)
        write_news(article_contents, filePath)
        # print(article_contents)


if __name__ == "__main__":
    root = create_root(date)
    url = "https://news.sina.com.cn/"
    urls = []
    index = 0
    while len(urls) == 0:
        index += 1
        urls = collect_urls(url)
    spider_urls(urls, root)
    pass
