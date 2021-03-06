import numpy as np
from PIL import Image
from os import listdir  # sampledata函数用到
import requests
import os
from requests import get, post, Session
"""dowloan()函数用到requests"""
from bs4 import BeautifulSoup

def download():
    """下载验证码"""
    for x in range(1500):
        r = requests.get('https://zhjw.neu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS')
        with open('dig/' + str(x) + '.jpg', 'wb') as pic:
            pic.write(r.content)

def biting(imgpath, threshold):
    """传入image对象进行灰度、二值处理
    imgpath:图片路径
    threshold:阀值
    """
    img = Image.open(imgpath)
    img = img.convert("L")  # 转灰度
    pixdata = img.load()  #读取图片像素RGB数值
    w, h = img.size    #获取图片尺寸大小，即长宽像素
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:   #像素小于阀值，置为0，图片变为黑白图
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img

def scissor(imgpath):
    """实现剪切图片"""
    center = [10, 24, 37]  #验证码图片3个数字的重心
    if (os.path.exists('dig') != True):
        os.makedirs('dig')
    imgname = imgpath.split('.')[0].split('/')
    img = Image.open(imgpath)
    for x in range(3):
        box = (center[x] - 7, 0, center[x] + 7, 18)
        region = img.crop(box)  #进行图片剪切，box(a,b,c,d)参数为宽从像素a到b，高从像素c到d
        region.save('dig/cut/bmp' + imgname[2] + '-' + str(x) + '.bmp')


# download()
# for x in range(1500):#该循环用于批量二值化
    # bit=biting('dig/'+str(x)+'.jpg',140)
    # bit.save('dig/bit/'+str(x)+'.bmp')
    # scissor('dig/bit/'+str(x)+'.bmp')

def login(username):
    """做了一些微小的贡献,并且按照基本法修改成功"""
    post_url = 'https://zhjw.neu.edu.cn/ACTIONLOGON.APPPROCESS?mode=4'
    captchaurl = 'https://zhjw.neu.edu.cn/ACTIONVALIDATERANDOMPICTURE.APPPROCESS'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
        'Referer': 'https://zhjw.neu.edu.cn/ACTIONLOGON.APPPROCESS?mode=3',
        'Accept-Encoding': 'gzip, deflate,br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    session = Session()
    checkcodecontent = session.get(captchaurl, headers=headers)
    with open('checkcode.jpg', 'wb') as f:
        f.write(checkcodecontent.content)
    print('验证码已写入到本地！')

    checkcode = input('验证码')
    # bit = biting('checkcode.gif', 140)  #88是阀值，去除验证码干扰线和随机噪声点
    # bit.save('checkcode.bmp')
    # scissor('checkcode.bmp')

    # for x in range(4):
    #     t = getimgtable('num/checkcode-' + str(x) + '.bmp')
    #     creatfile(t, 'num/checkcode-' + str(x) + '.txt')
    # L, M = sampledata()  #返回样本的标签和样本标签对应的数阵
    # for x in range(4):
    #     test = martixtoline('num/checkcode-' + str(x) + '.txt')  #把要验证的数字转化为行向量
    #     checkcode = checkcode + str(classify0(test, M, L, 3))    #验证码识别

    post_data = {
        'WebUserNO': username,
        'Password': username,
        'Agnomen': checkcode,
        'submit.x': 25,
        'submit.y': 9,
    }
    # """以下三行代码
    # 获取默认页http://219.216.96.73/pyxx/Default.aspx的html
    # 一旦post_url = 'http://219.216.96.73/pyxx/login.aspx'被正确的密码验证码登录，连接会被服务器重定向至默认页，即
    # http://219.216.96.73/pyxx/Default.aspx它实际是一个多个frame组成的网页，从状态码302 Found可以看出
    # """
    response = session.post(post_url, data=post_data, headers=headers)
    # print('服务器端返回码： ', response.status_code)
    default_htmldoc = BeautifulSoup(response.text, "html.parser")
    script = default_htmldoc.find_all('script')
    print(script[1].get_text())
    # """以下代码获取信息学号姓名导师信息的网页"""
    # get_url = 'http://219.216.96.73/pyxx/loging.aspx'
    # loging_htmldoc = session.get(get_url, headers=headers)
    #
    # script = default_htmldoc.find_all('script')
    # try:
    #     if (script[5].get_text() == "alert('密码错误!')"):
    #         return ('密码错误 登陆失败')
    #     elif (script[5].get_text() == "alert('你输入的验证码错误！')"):
    #         return ('验证码识别出错')
    #     elif (script[5].get_text() == "alert('该学生档案已转入存档,不能登录本系统!')"):
    #         return ('该学生档案已转入存档,不能登录本系统!')
    # except IndexError:
    #     soup = BeautifulSoup(loging_htmldoc.text, "html.parser")
    #     span = soup.find_all('span')
    #     return (span[28].get_text())  #返回HTML文档中第28个<span>标签的文本内容
    
'''
# -------------------------------------黑白图片求像素和进行粗分类-------------------
import shutil
def getimgtable(imgpath):  #把黑白图片求像素和
    img = Image.open(imgpath)
    table = 0
    pixdata = img.load()
    w, h = img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] == 0:
                table+=1
            elif pixdata[x, y] == 255:
                table+=0
    return table

dir='cut'
flist=os.listdir(dir)
for x in range(len(flist)):
    fileNameStr = flist[x]
    imgsum = getimgtable(dir+'/'+fileNameStr)

    if (imgsum==40):
        shutil.move(dir+'/'+fileNameStr, "1")
    if (imgsum==62):
        shutil.move(dir+'/'+fileNameStr, "2")
    if (imgsum==53)or(imgsum==51)or(imgsum==52):
        shutil.move(dir+'/'+fileNameStr, "3")
    if (imgsum==55)or(imgsum==54)or(imgsum==56):
        shutil.move(dir+'/'+fileNameStr, "4")
    if (imgsum==68)or(imgsum==67)or(imgsum==69):
        shutil.move(dir+'/'+fileNameStr, "5")
    if (imgsum==60):
        shutil.move(dir+'/'+fileNameStr, "6")
    if (imgsum==41):
        shutil.move(dir+'/'+fileNameStr, "7")
    if (imgsum==28):
        shutil.move(dir+'/'+fileNameStr, "+")
    if (imgsum==27):
        shutil.move(dir+'/'+fileNameStr, "x")
# -------------------------------------黑白图片求像素和进行粗分类-------------------
'''

