import requests
import re
import json
import time
import random

# 获取js源代码，获取英雄id
# 拼接URL地址
# 获取图片下载地址
# 下载图片

#获取英雄图片
def getLOLImages():
    # 模拟浏览器访问，防止被反爬
    header = {'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36'}
    # proxie = ['118.190.95.43:9001','101.236.60.8:8866','61.135.217.7:80']
    url_js = "http://lol.qq.com/biz/hero/champion.js"
    # 获取js源代码
    res_js = requests.get(url_js).content
    # 转码  将二进制转成字符串
    html_js = res_js.decode()
    # 正则表达式 .*?为通配符
    req = '"keys":(.*?),"data"'
    # 生成只有一个元素的列表list_js
    list_js = re.findall(req,html_js)
    # 把列表中的元素解码成字典
    dict_js = json.loads(list_js[0])
    
    # 定义图片列表
    pic_list = []
    for key in dict_js:
        # key = 英雄id
        # 英雄最大皮肤不超过20
        for i in range(20):
            num = str(i)
            if len(num) == 1:
                hero_num = "00" + num
            elif len(num) == 2:
                hero_num = "0" + num
            # http://ossweb-img.qq.com/images/lol/web201310/skin/big81007.jpg
            numstr = key + hero_num
            url = "http://ossweb-img.qq.com/images/lol/web201310/skin/big" + numstr +".jpg"
            pic_list.append(url)

    # 获取图片名称
    list_filepath = []
    # 构造EZreal.jpg
    path = "G:\\Python实验\\LOL英雄皮肤\\"
    for name in dict_js.values():
        for i in range(20):
            #  Aatrox0.jpg
            file_path = path + name + str(i) + ".jpg"
            list_filepath.append(file_path)

    # 下载图片
    n = 0
    for picurl in pic_list:
        #response = requests.get(picurl,proxies={'http': random.choice(proxie)},headers=header)
        response = requests.get(picurl,  headers=header)
        # 获取状态码
        if response.status_code == 200:
            print("正在下载%s"%list_filepath[n])
        #    time.sleep(1)
            with open(list_filepath[n], 'wb') as f:
                f.write(response.content)
        n = n+1

getLOLImages()
