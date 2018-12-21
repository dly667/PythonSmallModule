import json
import time
import requests
from lxml import etree
import re
url = "http://kj.wto56kj.com/common/ewb_query.zul?ewbNo=800000137678"
headers1 = {
    'Host': 'kj.wto56kj.com',
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54",
    "Accept": "application/json, text/plain, */*,br",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "http://www.wto56kj.com",
    "Origin": "",
    "CURLOPT_FOLLOWLOCATION":"true",
    "Cookie": "JSESSIONID=BF6CAD03E81256BCE2A5C1A6FC30F605",

}
def is_vaild_date(date):
    try:
        if ":" in date:
            time.strptime(date, "%Y-%m-%d %H:%M:%S")
        else:
            time.strptime(date, "%Y-%m-%d")
        return True
    except:
        return False
# 初始化
s = requests.session()
# post请求
rs = requests.get(url, headers=headers1, timeout=15)
content = rs.content

html = etree.HTML(content.decode("utf-8"))
html_data = html.xpath('body/script/text()')
# print(html_data)
r = r"\[.*\]"
temp = []

for i in html_data:
    # print(i)
    result = re.search(r,i,re.S)
    # print(json.loads(result.group(0)))
    rs = result.group(0)
    bb = rs[4]+rs[5]+rs[6]+rs[7]

    r2 = "\['zul.wgt.Label'[^v]*value:'([^\]]*)']]"   # ['zul.wgt.Label','t37Vd1',{sclass:'itemLabel',value:'1'},[]],
    rs2 = re.compile(r2).findall(rs)
    print(rs2)
    # rs2 = re.search(rs,re.S)
    ccc = rs2[14:]
    # b = [ccc[i:i + 14] for i in range(0, len(ccc), 14)]

    flag = 0
    final_rs = []
    for item in ccc:
        item = item.replace('\\u3010','')
        item = item.replace('\\u3011','')
        item = item.replace('\\uff1a','')
        item = item.replace('\\uff0c','')

        if is_vaild_date(item) is True:
            if flag == 2:
                flag = 0
                flag += 1
                final_rs.append(temp)
                temp = []
                temp.append(item)
            else:
                flag += 1
                temp.append(item)
        else:

            temp.append(item)



    # print(is_vaild_date(ccc[0]))
    # for item in rs2.group():
    #     print(item)
    # print(rs2)

    # print(result.group(0))
    # print(bb)
# pass
# print(rs.content)


# print(json.loads(a))
