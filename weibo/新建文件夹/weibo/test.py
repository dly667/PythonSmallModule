#coding:utf-8
import requests
from sqlalchemyDemo import session,Data
from function import deal_time
r = requests.get('https://m.weibo.cn/api/container/getIndex?uid=1288915263&luicode=10000011&lfid=100103type\
%3D1%26q%3D%E5%B9%B3%E5%AE%89%E5%8C%97%E4%BA%AC&featurecode=20000320&sudaref=login.sina.com.cn&display=0&\
retcode=6102&type=uid&value=1288915263&containerid=1076031288915263&page=2')
print(r.json())
for v in (r.json()['data']['cards']):
    if(v['card_type']==9):
        # 将数据做最终处理
        time = deal_time(v['mblog']['created_at'])
        if 'pics' in v['mblog'] != False:
            material_type = 'image'
        elif 'page_info' in v['mblog']!=False:
            material_type = 'video'
        else:
            material_type = 'text'
        
        if 'retweeted_status' in v['mblog'] != '':
            creative_type = '1'
        else:
            creative_type = '2'
        # 将数据写入数据库
        ed_user = Data(
            account_id=v['mblog']['user']['id'],\
            account_name=v['mblog']['user']['screen_name'],
            comments_number=v['mblog']['comments_count'],\
            like_number = v['mblog']['attitudes_count'],
            forwarding_time = time,
            forwarded_number = v['mblog']['reposts_count'],
            creative_type = creative_type,
            material_type = material_type,
        )
        session.add(ed_user)

    elif v['card_type']==58:
        pass
    elif v['card_type']==59:
        pass
    elif v['card_type']==31:
        pass

session.commit()
page = 1
def crawl(page):
    r = requests.get('https://m.weibo.cn/api/container/getIndex?uid=1288915263&luicode=10000011&lfid=100103type\
%3D1%26q%3D%E5%B9%B3%E5%AE%89%E5%8C%97%E4%BA%AC&featurecode=20000320&sudaref=login.sina.com.cn&display=0&\
retcode=6102&type=uid&value=1288915263&containerid=1076031288915263&page='+page)
    if r.json()['ok'] == 1:
        for v in (r.json()['data']['cards']):
            if(v['card_type']==9):
                print(v['mblog']['created_at'])
                # 将数据写入数据库
                ed_user = Data(name='ed', fullname='Ed Jones', password='edspassword')
                session.add(ed_user)
            elif v['card_type']==59:
                return 'complete'
        # crawl(page=page+1)
    else:
        crawl(page)
    
