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
import random
#请求头部文件
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
    "Referer": "http://ucp164332.a.stonevote.net/poll/f7d9c376-3213-d21f-43fe-d9031225ee39.html",
    
}

headers2 = {
    'Host': 'ucp164332.a.stonevote.net',
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Pragma": "no-cache",
    "Referer": "http://ucp164332.a.stonevote.net/poll/f7d9c376-3213-d21f-43fe-d9031225ee39.html"

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
    "Referer": "http://ucp164332.a.stonevote.net/poll/f7d9c376-3213-d21f-43fe-d9031225ee39.html"

}


#投票类
class Vote():
    
    # ip = ProxyIp().get_ip_ad().strip()
    def __init__(self,ip):
        self.ip=ip
    # 1.获取网页
    def step(self):
        
        self.s = requests.Session()
        self.t = self.s.get(
            "http://ucp164332.a.stonevote.net/poll/f7d9c376-3213-d21f-43fe-d9031225ee39.html", headers=headers1,timeout=15, proxies={'http':str(self.ip)})
       
    # 2.获取验证码
    def step2(self):

        self.capt = self.s.get("http://ucp164332.a.stonevote.net/plugin/securimage/securimage_show.php",headers=headers2,timeout=25, proxies={'http':str(self.ip)})
        filename = 'captcha/'+str(time.time())+'.png'
        with open(filename, 'wb') as fp:
            fp.write(self.capt.content)
        self.dama(filename)
        
    # 3.识别验证码
    def dama(self,filename):
        rk = RuoKuai()
        r = rk.start(filename).text
        capt = json.loads(r)['Result']
        print(capt)
        
        self.step3(capt,filename)
        #self.step3('abcds')#这里我随便写验证码
    # 4.投票
    def step3(self,capt,filename):
        # capt = input("capt:")
        self.dovote = self.s.post("http://ucp164332.a.stonevote.net/op.php",data={
            "action": "dovote",
            "guid": "f7d9c376-3213-d21f-43fe-d9031225ee39",
            "ops": "4181079|",
            "captchacode": str(capt)
        }, proxies={'http':str(self.ip)},timeout=25)
        print(self.dovote.text)
        if json.loads(self.dovote.text)['ret'] == 1:
            # 重命名文件名做训练集
            os.rename(os.path.join('',filename),os.path.join('captcha','num_'+str(random.randint(100,900))+'_'+capt+'.png'))
        print(self.dovote.text)
        # self.step4()
    # 5.截图投票成功的界面
    def step4(self):
        pass
        # p_obj=Photo()
        # try:
        #     p_obj.photo(self.ip)
        #     p_obj.close()
        # except Exception as e:
        #     p_obj.close()
        
        # print(self.t.cookies)
        # self.k = self.s.get(
        #     "http://ucp164332.a.stonevote.net/poll/f7d9c376-3213-d21f-43fe-d9031225ee39.html?searchkey=20", headers=headers1,timeout=20, proxies={'http':str(Vote.ip)})
        # print(self.k.text)
    def vote(self):
        self.step()
        self.step2()
def task(ip):
    # Vote().vote()
    # ip=''
    try:
        obj=Vote(ip)
        obj.vote()
    except Exception as e:
        print("链接超时")
        print(e)
    
#开启多进程
def thread_main():
    #线程池
    pool=ThreadPoolExecutor(8)
    #任务数
    task_count=500
    obj_ip=ProxyIp()
    
    for i in range(0,task_count):
        ip_list=obj_ip.get_ip_ad()
        for j in range(int(len(ip_list)/10)):
            pool.submit(task,ip_list[j])
        time.sleep(30)
    pool.shutdown()

if __name__ == '__main__':
    thread_main()
    # Vote(ip).vote()
    # Vote().vote()
    # thread_main()
    # n=0
    # while True:
    #     task()
    #     # Vote().vote()
    #     if n>20:
    #         break