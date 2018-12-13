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
data = [3453751692,1507156867,2649761871,1960060805,3980980810,1044825203,2158074297,2676362053,3789154482,1936009361,2028845887,5085042263,2130830185,2037181057,2611712133,1908516792,5780949476,5071610242,2061911495]
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

                if unix_time<1514736000:
                    return 'com_ok'
                if unix_time>1530288000:
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
                    account_id=v['mblog']['user']['id'],
                    account_name=v['mblog']['user']['screen_name'],
                    comments_number=v['mblog']['comments_count'],
                    like_number = v['mblog']['attitudes_count'],
                    forwarding_time = time_data,
                    forwarded_number = v['mblog']['reposts_count'],
                    creative_type = creative_type,
                    material_type = material_type,
                    followers_count = v['mblog']['user']['followers_count'],
                    follow_count = v['mblog']['user']['follow_count'],
                    forward_sum_count = r.json()['data']['cardlistInfo']['total'],
                    unix_time = unix_time
                )

                session.add(ed_user)

            elif v['card_type']==59:
                return 'complete'
        session.commit()
        return None
    else:
        if len(r.json()['data']['cards'])<=0:
            return 'com_ok'
        crawl(page, uid)

def core(uid):
    page = 1
    while True:
        if crawl(page, uid) == 'com_ok':
            break;
        page+=1
for d in data:
    core(d)



# core(3453751692) #已经爬完这个id，该换下一个了