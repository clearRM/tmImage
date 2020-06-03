# -*- coding:utf-8 -*-
import urllib.request
import re
import os
import requests
headers = {"User-Agent ":"Mozilla/5.0 (Windows NT 6.1; Wi n64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36"}

i = 30
def downloadPic(url):
    global i
    data=urllib.request.urlopen(url).read().decode("utf-8","ignore")
    pat='"item_pic":"//(.*?)"'
    pic_url = re.compile(pat).findall(data)
    print(pic_url)
    #request = urllib.request.Request(url, headers=headers)
    #print(str(response.text))
    #html = urllib.request.urlopen(request).read()

    #pic_url = etree.HTML(html).xpath('//span[@class="imgLink"]/img/@src')

    print(pic_url)
    for oldeach in pic_url:
        each = "http://"+oldeach
        print(each+"--------------------------")
        print("正在下载第" + str(i) + "张图片,图片地址:" + str(each))
        try:
            pic = requests.get(each)
            #req_img = urllib.request.Request(url=each)
            #pic = urllib.request.urlopen(req_img)
        except:
            print("下载失败，下一张")
        if not os.path.exists("D:\爬虫数据/淘宝图片/"):
            os.mkdir("D:\爬虫数据/淘宝图片/")
        string = 'D:\爬虫数据/淘宝图片/'+ "/" + str(i) + ".jpg"
        fp = open(string, 'wb')
        fp.write(pic.content)
        fp.close()
        i += 1


if __name__ == '__main__':  # 主程序
    json_pid= 1198
    tce_sid= 3815421

    url="https://tce.taobao.com/api/mget.htm?callback=jsonp"+str(json_pid)+"&tce_sid="+str(tce_sid)+"&tce_vid=0&tid=&tab=&topic=&count=&env=online"
    print(url)


    downloadPic(url)

    print("下载完成!")
