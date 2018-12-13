# -*- coding: utf-8 -*-
import requests

# 蘑菇代理的隧道订单
appKey = "UzlRTTkxNnBMbDBJbXNvMjpud2RUSlNySXFWM3hjTWhW"

# 蘑菇隧道代理服务器地址
ip_port = 'transfer.mogumiao.com:9001'


# if r.status_code == 302 or r.status_code == 301 :
#     loc = r.headers['Location']
#     url_f = "https://ip.cn" + loc
#     print(loc)
#     r = requests.get(url_f, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
#     print(r.status_code)

    # print(r.text.encode(encoding='gbk'))
    # print(getCoding(r.text))
def crawl(url):
    # 准备去爬的 URL 链接
    # url = 'https://ip.gs'

    proxy = {"http": "http://" + ip_port, "https": "https://" + ip_port}
    headers = {"Proxy-Authorization": 'Basic ' + appKey, "Content-type": "text/html", "charset": "utf-8"}
    r = requests.get(url, headers=headers, proxies=proxy, verify=False, allow_redirects=False)
    # print(r.status_code)
    # print(r.content.decode(encoding='utf-8'))
    return r
