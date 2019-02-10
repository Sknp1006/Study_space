import requests
import os
import sys
import json

# 视频AV号列表
aid_list = []

# 测试mid编号
#mid = 1707081
# 测试视频列表
#aid_list = [7081208, 7046588, 6830834, 6763279]

# 评论用户及其信息
info_list = []


# 获取指定UP的所有视频的AV号 mid:用户编号 size:单次拉取数目 page:页数
def getAllAVList(mid, size, page):
    # 获取UP主视频列表
    for n in range(1, page + 1):
        url = "http://space.bilibili.com/ajax/member/getSubmitVideos?mid=" + \
              str(mid) + "&pagesize=" + str(size) + "&page=" + str(n)
        r = requests.get(url)
        text = r.text
        json_text = json.loads(text)
        # 遍历JSON格式信息，获取视频aid
        for item in json_text["data"]["vlist"]:
            aid_list.append(item["aid"])
    with open("aid list.txt", "w", encoding='utf-8') as al:
        al.write(str(aid_list))
    print("一共有：", len(aid_list), "个视频")
    print("列表已输出")


# 获取一个AV号视频下所有评论
def getAllCommentList(item):
    url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=1&type=1&oid=" + str(item) + "&sort=1&nohot=1"
    r = requests.get(url)
    numtext = r.text
    json_text = json.loads(numtext)
    commentsNum = json_text["data"]["page"]["count"]
    page = commentsNum // 20 + 1
    for n in range(1, page):
        url = "https://api.bilibili.com/x/v2/reply?jsonp=jsonp&pn=" + str(n) + "&type=1&oid=" + str(
            item) + "&sort=1&nohot=1"
        req = requests.get(url)
        text = req.text
        json_text_list = json.loads(text)
        for i in json_text_list["data"]["replies"]:
            info_list.append([i["member"]["mid"], i["content"]["message"]])
    # print(info_list)


# 保存评论文件为txt
def saveTxt(filename, filecontent):
    filename = str(filename) + ".csv"
    with open(filename, "a", encoding='utf-8') as txt:
        print("文件写入中")
        for content in filecontent:
            txt.write(content[0] + ' ' + content[1].replace('\n', '') + '\n\n')


# 获取数据，到分词保存，一气呵成
if __name__ == "__main__":
    mid = int(input("请输入mid编号："))
    getAllAVList(mid, 100, 100)
    for item in aid_list:
        info_list.clear()
        getAllCommentList(item)
        saveTxt(item, info_list)
    print("写入完成，共写入", len(aid_list), "个文件")



