#coding:utf-8
import requests
from sqlalchemyDemo import session,Data
from function import deal_time
import time
# r = requests.get('https://m.weibo.cn/api/container/getIndex?uid=1288915263&luicode=10000011&lfid=100103type\
# %3D1%26q%3D%E5%B9%B3%E5%AE%89%E5%8C%97%E4%BA%AC&featurecode=20000320&sudaref=login.sina.com.cn&display=0&\
# retcode=6102&type=uid&value=1288915263&containerid=1076031288915263&page=2')

# for v in (r.json()['data']['cards']):
#     if(v['card_type']==9):
#         # 将数据做最终处理
#         time = deal_time(v['mblog']['created_at'])
#         if 'pics' in v['mblog'] != False:
#             material_type = 'image'
#         elif 'page_info' in v['mblog']!=False:
#             material_type = 'video'
#         else:
#             material_type = 'text'
        
#         if 'retweeted_status' in v['mblog'] != '':
#             creative_type = '1'
#         else:
#             creative_type = '2'
#         # 将数据写入数据库
#         ed_user = Data(
#             account_id=v['mblog']['user']['id'],\
#             account_name=v['mblog']['user']['screen_name'],
#             comments_number=v['mblog']['comments_count'],\
#             like_number = v['mblog']['attitudes_count'],
#             forwarding_time = time,
#             forwarded_number = v['mblog']['reposts_count'],
#             creative_type = creative_type,
#             material_type = material_type,
#             followers_count = v['mblog']['user']['followers_count'],
#             follow_count = v['mblog']['user']['follow_count'],
#         )
#         session.add(ed_user)

#     elif v['card_type']==58:
#         pass
#     elif v['card_type']==59:
#         pass
#     elif v['card_type']==31:
#         pass

# session.commit()


#封装函数
# 1288915263
data = [2418724427,2778292197,2418801567,3508612897,2258833123,2611704935,2417139911,2518353303,1936009361]
page = 1

def crawl(page,uid):
    uid = str(uid)
    page = str(page)
    print("%s当前第 %s 页"%(uid,page))
    time.sleep(1)
    r = requests.get('https://m.weibo.cn/api/container/getIndex?uid='+uid+'&luicode=10000011&lfid=100103type\
%3D1%26q%3D%E5%B9%B3%E5%AE%89%E5%8C%97%E4%BA%AC&featurecode=20000320&sudaref=login.sina.com.cn&display=0&\
retcode=6102&type=uid&value='+uid+'&containerid=107603'+uid+'&page='+page)
    if r.json()['ok'] == 1:
        for v in (r.json()['data']['cards']):
            if(v['card_type']==9):
                # 将数据做最终处理
                time_data = deal_time(v['mblog']['created_at'])
                unix_time = time.mktime(time.strptime(time_data, '%Y-%m-%d'))
                if unix_time<1519833600 :
                    return 'com_ok'
                if unix_time>1527782399:
                    continue
                if 'pics' in v['mblog'] != False:
                    material_type = 'image'
                elif 'page_info' in v['mblog']!=False:
                    material_type = 'video'
                else:
                    material_type = 'text'
                # 1表示转发  2表示原创
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
                    forwarding_time = time_data,
                    forwarded_number = v['mblog']['reposts_count'],
                    creative_type = creative_type,
                    material_type = material_type,
                    followers_count = v['mblog']['user']['followers_count'],
                    follow_count = v['mblog']['user']['follow_count'],
                    forward_sum_count = r.json()['data']['cardlistInfo']['total'],
                )
                session.add(ed_user)
            elif v['card_type']==59:
                return 'complete'
        session.commit()
        crawl(int(page)+1,uid)
    else:
        crawl(page,uid)
crawl(1,1936009361)

