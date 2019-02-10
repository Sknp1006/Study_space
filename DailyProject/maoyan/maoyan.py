import requests
import re
import json
import time
import random
from multiprocessing import Pool

#URL = "http://maoyan.com/board/4"#input("输入目标网址:")
MAXSLEEPTIME = 3
MINSLEEPTIME = 1
STAUS_OK = 200
MAX_PAGE_NUM = 10
SERVER_ERROR_MIN = 500
SERVER_ERROR_MAX = 600
CLIENT_ERROR_MIN = 400
CLIENT_ERROR_MAX = 500

def get_one_page(URL, num_retries=5): #如果对方服务器出错，则重试5次
    if num_retries == 0:
        return None
    ua_headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64)"}
    response = requests.get(URL, headers=ua_headers)
    if response.status_code == STAUS_OK: #ok
        return response.text
    elif SERVER_ERROR_MIN <= response.status_code < SERVER_ERROR_MAX:#左闭右开
        time.sleep(MINSLEEPTIME)
        get_one_page(URL, num_retries-1) #递归，可能会死循环
    elif CLIENT_ERROR_MIN <= response.status_code < CLIENT_ERROR_MAX:
        if response.status_code == 404:
            print("Page not found")
        elif response.status_code == 403:
            print("Have no rights")
        else:
            pass
    return None

def parse_one_page(html):
    pattern = re.compile('<p class="name">.*?title="([\s\S]*?)"[\s\S]*?<p class="s'
                         'tar">([\s\S]*?)</p>[\s\S]*?<p class="releasetime">([\s\S]*?)</p>')
    items = re.findall(pattern, html)
    for it in items:
        yield {
            "title": it[0].strip(),
            "actor": it[1].strip(),
            "time": it[2].strip()
        }

def write_to_file(item):
    with open("猫眼.text", 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False)+'\n')

def crawl_one_page(offset):
    url = "http://maoyan.com/board/4?offset="+str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        write_to_file(item)
    time.sleep(random.randint(MINSLEEPTIME, MAXSLEEPTIME))  # 随机休息1-3秒之后，再进行下一次爬取


if __name__ == "__main__":
    pool = Pool()
    pool.map(crawl_one_page(), [i*10 for i in range(10)])
    pool.close()
    pool.join()
    # for i in range(MAX_PAGE_NUM):
    #     crawl_one_page(i*MAX_PAGE_NUM)
    #print("ok")