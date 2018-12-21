import requests
import time
import chardet
import json
import datetime
import xlwt,xlrd
from xlutils.copy import copy
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
    'Host': 'www.itjuzi.com',
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54",
    "Accept": "application/json, text/plain, */*,br",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "https://www.itjuzi.com/investevent",
    "Origin": "https://www.itjuzi.com",
    "CURLOPT_FOLLOWLOCATION":"true",
    "Cookie": "acw_tc=76b20f7115447756466435129e3e733edfb023c3f8a3b2e02b602e1eab9cec; gr_user_id=e31aee24-93f0-488a-9a7e-c1624a60fae6; _ga=GA1.2.720568260.1544775648; gr_session_id_eee5a46c52000d401f969f4535bdaa78=0c403088-64da-4c64-946f-c6354f5c93b5; _gid=GA1.2.1068712652.1545356655; gr_session_id_18157795211=fc1fad3d-338b-4169-8922-0c1bad3ee608; gr_session_id_eee5a46c52000d401f969f4535bdaa78_0c403088-64da-4c64-946f-c6354f5c93b5=true; flag=681142--13777707654",
    "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5pdGp1emkuY29tL2FwaS9hdXRob3JpemF0aW9ucyIsImlhdCI6MTU0NTM1NzAwNywiZXhwIjoxNTQ1NDQzNDA3LCJuYmYiOjE1NDUzNTcwMDcsImp0aSI6IkJxSmVVR0NtaDFUeHc3TE4iLCJzdWIiOjY4MTE0MiwicHJ2IjoiMjNiZDVjODk0OWY2MDBhZGIzOWU3MDFjNDAwODcyZGI3YTU5NzZmNyJ9.ShJTV1tNfEueQsg-ekk5eS8uOfwftXlflLA0ho2gkSM"

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
    "Referer": "https://www.itjuzi.com/investevent",
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
    "Referer": "https://www.itjuzi.com/investevent"

}
# 目标网址
url = "https://www.itjuzi.com/api/investevents"
rb1 = xlrd.open_workbook('1.xls')  # 打开weng.xls文件
wb = copy(rb1)  # 利用xlutils.copy下的copy函数复制
ws = wb.get_sheet(0)  # 获取表单0

class JuZiIt:

    def crawl(self, page):

        # 初始化
        s = requests.session()
        # post请求
        rs = requests.post(url, data={
            "city": "",
            "equity_ratio": "",
            "ipo_platform": "",
            "page": page,
            "pagetotal": 9475,
            "per_page": 20,
            "prov": "",
            "round": "",
            "scope": "教育",
            "selected": "",
            "status": "",
            "sub_scope": "",
            "time": "2018年",
            "total": 0,
            "type": 1,
            "valuation": "",
            "valuations": "",
        }, headers=headers1, timeout=15)

        # content = rs.content.decode("unicode_escape")
        # str解码成json
        j = json.loads(rs.content)


        # print(j['data'])
        # 判断是否请求成功
        if j['code'] == 200:
            data = j['data']['data']

            if len(data)>0:
                for key,value in enumerate(data):
                    # 临时变量
                    temp = {}
                    date_array = datetime.datetime.utcfromtimestamp(value['time'])
                    temp = ({'time': date_array.strftime("%Y/%m/%d")})
                    investor = []
                    for i in value['investor']:
                        investor.append(i['name'])
                    temp['investor'] = "、".join(investor)
                    if temp['investor'] == "":
                        temp['investor'] = "未透露"
                    temp['name'] = value['name']
                    if temp['name'] == "":
                        temp['name'] = "未透露"
                    temp['round'] = value['round']
                    if temp['round'] == "":
                        temp['round'] = "未透露"
                    temp['money'] = value['money']
                    if temp['money'] == "":
                        temp['money'] = "未透露"
                    temp['valuation'] = value['valuation']
                    if temp['valuation'] == "":
                        temp['valuation'] = "未透露"
                    temp['valuation'] = value['valuation']
                    temp['source'] = "橘子it"
                    temp['link'] = "https://www.itjuzi.com/investevent/"+str(value['id'])
                    row = (page-1)*20+key+3
                    ws.write(row, 0, row-2)  # 改变（0,0）的值
                    ws.write(row, 1, temp['investor'])    # 改变（0,0）的值
                    ws.write(row, 2, temp['time'])    # 改变（0,0）的值
                    ws.write(row, 3, temp['name'])    # 改变（0,0）的值
                    ws.write(row, 5, temp['money'])   # 改变（0,0）的值
                    ws.write(row, 7, temp['round'])   # 改变（0,0）的值
                    ws.write(row, 9, temp['source'])  # 改变（0,0）的值
                    ws.write(row, 10, temp['link'])   # 改变（0,0）的值
            else:
                print("爬取完毕，已无新数据！")
                exit(1)
                return
        else:
            print("需要vip，请重新注册账号。或者重试代码！")
            exit(1)
            return

        wb.save('weng.xls')

if __name__ == '__main__':
    page = 28
    while True:
        time.sleep(1)
        try:
            print("当前正在抓取第", page, "页")
            JuZiIt().crawl(page)
            page += 1
            # if page == 10:
                # break
        except Exception as e:
            print(e)
