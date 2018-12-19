import requests
from lxml import etree

url = "http://www.jingmeiti.com/archives/category/news/zixun"
headers1 = {
    'Host': 'www.jingmeiti.com',
    "Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36 OPR/54.0.2952.54",
    "Accept": "application/json, text/plain, */*,br",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Referer": "http://www.jingmeiti.com/",
    "Origin": "https://www.itjuzi.com",
    "CURLOPT_FOLLOWLOCATION":"true",
    "Cookie": "gr_user_id=159cc3dc-8956-4107-9eef-02467d867849; UM_distinctid=167bf339e714dd-07a4981167f3e4-162a1c0b-1fa400-167bf339e721032; CNZZDATA1260308686=1082659512-1545096502-https%253A%252F%252Fwww.baidu.com%252F%7C1545206357; gr_session_id_b1e9b85e169a87d9=956c52f4-4a38-4cd5-86bc-16bfc1fe6e4c; gr_session_id_b1e9b85e169a87d9_956c52f4-4a38-4cd5-86bc-16bfc1fe6e4c=true",
    "Authorization": "bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL3d3dy5pdGp1emkuY29tL2FwaS9hdXRob3JpemF0aW9ucy9yZWZyZXNoVG9rZW4iLCJpYXQiOjE1NDQ3NzU2NjEsImV4cCI6MTU0NTI2OTM5MywibmJmIjoxNTQ1MTgyOTkzLCJqdGkiOiJ3N1hrYTN4SFZKckl0U1JNIiwic3ViIjo2Nzc4NTcsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjcifQ.Qeh2Nl5EnIxnrCGNQoF0uUmCwFvxAvg9oy6fk-zX0qo"

}

# 初始化
s = requests.session()
# post请求
rs = requests.get(url, headers=headers1, timeout=15)
content = rs.content
# print(content)
html = etree.HTML(content)
html_data = html.xpath('//*[@id="page-content"]/div/div/div[1]/div/div/div/div[2]/div[1]/h2/a/@href')
for i in html_data:
    print(i)
# print(rs.content)