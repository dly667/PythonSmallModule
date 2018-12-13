import requests
import base64
from lxml import etree
import time
import chardet
import urllib.request
import re
import json
from ruokuai import RuoKuai
from proxy import ProxyIp
# from pic import Photo
from concurrent.futures import ThreadPoolExecutor
import os
headers = {
    'Host': 'ucp164332.a.stonevote.net',
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": "acw_sc__=5b5138af1d3810deb561537afca30f894a75c9c2"

}

headers1 = {
    'Host': 'ucp164332.a.stonevote.net',
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "http://ucp164332.a.stonevote.net/poll/a70e584d-75c8-638c-b2d7-1789d7d355c4.html",
    
}
headers2 = {
    'Host': 'ucp164332.a.stonevote.net',
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54",
    "Accept": "image/webp,image/apng,image/*,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Pragma": "no-cache",
    "Referer": "http://ucp164332.a.stonevote.net/poll/a70e584d-75c8-638c-b2d7-1789d7d355c4.html",
    "Cookie": "aliyungf_tc=AQAAAE2Z7FWTRQoA4svrcwg1O47pdq/1; PHPSESSID=1267f9a2ee1b07f6b40ab397029a3e58; mvotelang=cn; userrefurl=http%3A%2F%2Fucp164332.a.stonevote.net%2Fpoll%2Fa70e584d-75c8-638c-b2d7-1789d7d355c4.html%3Fsearchkey%3D%25E6%25B1%25A4%25E6%25B4%25AA%25E6%259E%2597; s_toneucid=9d9f0057-0635-6ba2-a95e-7b6a9eebe698; VIST-8db9d1b3-75c3-cb18-b505-50e4927caaa620181213=8db9d1b3-75c3-cb18-b505-50e4927caaa620181213; bdshare_firstime=1544682553950; V-8db9d1b3-75c3-cb18-b505-50e4927caaa620181213=1; _alicdn_sec__=5c1207852cf543dc780c9b7031b06030f82e68c2"

}
headers3 = {
    'Host': 'ucp164332.a.stonevote.net',
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Pragma": "no-cache",
    "Referer": "http://ucp164332.a.stonevote.net/poll/a70e584d-75c8-638c-b2d7-1789d7d355c4.html"

}

# ip = ProxyIp().get_ip_ad().strip()
class Vote():
 
    # 1.获取网页
    # ip = ProxyIp().get_ip_ad().strip()
    
    def step(self):
        
        self.s = requests.Session()
        self.t = self.s.get(
            "http://ucp164332.a.stonevote.net/poll/a70e584d-75c8-638c-b2d7-1789d7d355c4.html", headers=headers1,timeout=15)#proxies={'http':str(self.ip)}
       
    # 2.获取验证码
    def step2(self):

        self.capt = self.s.get("http://ucp164332.a.stonevote.net/plugin/securimage/securimage_show.php",headers=headers2,timeout=15)#, proxies={'http':str(self.ip)}
        filename = 'captcha/'+str(time.time())+'.png'
        with open(filename, 'wb') as fp:
            fp.write(self.capt.content)
        self.dama(filename)
        
    # 3.识别验证码
    def dama(self,filename):
        rk = RuoKuai()
        r = rk.start(filename).text
        # print(r)
        capt = json.loads(r)['Result']
        print(capt)
        self.step3(capt)
        #self.step3('abcds')#这里我随便写验证码
    # 4.投票
    def step3(self,capt):
        # capt = input("capt:")
        self.dovote = self.s.post("http://ucp164332.a.stonevote.net/op.php",data={
            "action": "dovote",
            "guid": "a70e584d-75c8-638c-b2d7-1789d7d355c4",
            "ops": "4486474|",
            "captchacode": str(capt),
            "otheropid": 0,
            "otherop": '',
            "inner": 0,
            "invitecode": '',
            "wxparam": '',
            "prvstr": '',
            "prvhash": '',
            "prvtime": '',
            "smscoderequestid": 0

        },timeout=30)#, proxies={'http':str(self.ip)}
        print(self.dovote.text)
        self.step4()
    # 5.截图投票成功的界面
    def step4(self):
        Photo().photo(self.ip)
      
        # self.k = self.s.get(
        #     "http://ucp164332.a.stonevote.net/poll/f7d9c376-3213-d21f-43fe-d9031225ee39.html?searchkey=20", headers=headers1,timeout=20, proxies={'http':str(Vote.ip)})
        # print(self.k.text)
        pass
    def step5(self):
        '''获取页面看是否投票成功'''
        headers1["cookie"]="aliyungf_tc:%s"%self.s.cookies.get_dict()["aliyungf_tc"]
        res=self.s.get("http://ucp164332.a.stonevote.net/poll/a70e584d-75c8-638c-b2d7-1789d7d355c4.html?searchkey=%E6%B1%A4%E6%B4%AA%E6%9E%97",headers=headers1)
        # print()
        print(res.content)
    def vote(self):
        self.step()
        self.step2()
        # self.step5()
def task():
    # Vote().vote()
    try:
        obj=Vote()
        obj.vote()
    except Exception as e:
        print("链接超时")
        print(e)
    

def thread_main():
    pool=ThreadPoolExecutor(5)
    task_count=20
    for i in range(0,task_count):
        pool.submit(task)
        time.sleep(5)
    pool.shutdown()

if __name__ == '__main__':
    Vote().vote()
    # thread_main()
    # n=0
    # while True:
    #     task()
    #     # Vote().vote()
    #     if n>20:
    #         break