from PIL import Image
from os import listdir   #sampledata函数用到
import requests
from requests import get,post,Session
"""dowloan()函数用到requests"""
from bs4 import BeautifulSoup
"""login()函数用到BeautifulSoup"""
from numpy import *

def biting(imgpath,threshold):
    """传入image对象进行灰度、二值处理
    imgpath:图片路径
    threshold:阀值
    """
    img = Image.open(imgpath)
    img = img.convert("L") # 转灰度
    pixdata = img.load()
    w, h = img.size
    # 遍历所有像素，大于阈值的为黑色
    for y in range(h):
        for x in range(w):
            if pixdata[x, y] < threshold:
                pixdata[x, y] = 0
            else:
                pixdata[x, y] = 255
    return img


def getimgtable(imgpath):
    img = Image.open(imgpath)
    table=[]
    pixdata = img.load()
    w, h=img.size
    for y in range(h):
        for x in range(w):
            if pixdata[x, y]== 0:
                table.append('1')
            elif pixdata[x, y]== 255:
                table.append('0')
        table.append('\n')
    return table


def creatfile(data):
    string = "".join(data)#把list类型转换成str类型
    with open('l.txt', 'w') as f:
        f.write(string)
        print("创建文件成功")


def scissor(imgpath):
    """实现剪切图片"""
    center = [16, 29, 43, 59]
    if (os.path.exists('E:/桌面文件/one/num')!=True):
        os.makedirs('E:/桌面文件/one/num')
    imgname=imgpath.split('.')
    img = Image.open(imgpath)
    for x in range(4):
        box = (center[x] - 7, 11, center[x] + 7, 35)
        region = img.crop(box)
        region.save('num/'+imgname[0]+'-'+str(x)+'.bmp')


def download():
    """下载验证码"""
    for x in range(1000):
        r = requests.get('http://219.216.96.73/pyxx/PageTemplate/NsoftPage/yzm/createyzm.aspx')
        with open('dig/'+str(x)+'.gif', 'wb') as pic:
            pic.write(r.content)


def login():
    """做了一些微小的贡献，还需要修改一下"""
    post_url = 'http://219.216.96.73/pyxx/login.aspx'
    captchaurl = 'http://219.216.96.73/pyxx/PageTemplate/NsoftPage/yzm/createyzm.aspx'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36",
        'Referer': 'http://219.216.96.73/pyxx/login.aspx',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
    }
    session = Session()
    checkcodecontent = session.get(captchaurl, headers=headers)
    with open('checkcode.gif', 'wb') as f:
        f.write(checkcodecontent.content)
    print('验证码已写入到本地！')
    os.startfile('checkcode.gif')
    checkcode = input('请输入验证码：')
    post_data = {
        '__VIEWSTATE': '/wEPDwUENTM4MWQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFEmN0bDAwJEltYWdlQnV0dG9uMS0nFEa6hHMvPk9e8UqDdLj9ClgECnCtpmFqIziOXB+0',
        '__VIEWSTATEGENERATOR': '496CE0B8',
        'ctl00$txtusername': '1700651',
        'ctl00$txtpassword': '1700651',
        'ctl00$txtyzm': checkcode,
        'ctl00$ImageButton1.x': '30',
        'ctl00$ImageButton1.y': '26',
    }
    response = session.post(post_url, data=post_data, headers=headers)
    login_code = response.text
    print('服务器端返回码： ', response.status_code)
    """print(login_code)"""

    get_url = 'http://219.216.96.73/pyxx/loging.aspx'
    headers2 = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': 'ASP.NET_SessionId=fovatpeslaij1rbalsiske0g',
        'Host': '219.216.96.73',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    html_doc = session.get(get_url, headers=headers)
    """print(response2.text)"""
    soup = BeautifulSoup(html_doc.text, "html.parser")
    k = soup.find_all('span')
    try:
        print(k[28].get_text())
    except IndexError:
        print("密码错误登陆失败")


"""
for x in range(1000):
    bit=biting('dig/'+str(x)+'.gif',88)
    bit.save('dig_bmp88/'+str(x)+'.bmp')
for x in range(1000):
    scissor('dig_bmp88/'+str(x)+'.bmp')
l=martixtoline('D.txt')
creatfile(str(l[0,::]))
t = getimgtable('num/dig_bmp88/0-1.bmp')
creatfile(t)

L, M = sampledata()
print(L)
print(M[1][56:70])

"""
def martixtoline(filename):
    """把矩阵转化为一个行向量"""
    line = zeros((1,336))#336是验证码图片剪切成单个数字后，单个数字图片的像素14x24
    f = open(filename)
    for i in range(24):
        linestr = f.readline()
        for j in range(14):
            line[0,14*i+j] = int(linestr[j])
    return line


def sampledata():  #该函数用于把样本数据转化成array类型，以便在numpy中运算
    Labels = []
    FileList = listdir('sampledata')           #load the training set
    m = len(FileList)
    Mat = zeros((m,336))    #336是验证码图片剪切成单个数字后，单个数字图片的像素14x24
    for i in range(m):
        fileNameStr = FileList[i]
        fileStr = fileNameStr.split('.')[0]     #take off .txt
        classNumStr = int(fileStr.split('-')[0])
        Labels.append(classNumStr)  #正确答案
        Mat[i,:] = martixtoline('sampledata/%s' % fileNameStr)
    return Labels,Mat




