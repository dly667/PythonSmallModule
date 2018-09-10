import datetime
from sqlalchemyDemo import session,Data,sessionmaker,create_engine,Column, Integer, String,Base

i = datetime.datetime.now()
def deal_time(strdata):
    index1 = strdata.find('小时前', 0, len(strdata))
    index2 = strdata.find('分钟前', 0, len(strdata))
    index3 = strdata.find('昨天', 0, len(strdata))
    index4 = strdata.find('20',0,2)
    cur_month = i.strftime("%m")
    cur_month = str(i.year)+'-'+cur_month
   
    if index1!= -1:    
        if i.hour-int(strdata[slice(index1)])<0:
            t = i.day-1
        else:
            t = i.day
        return str(cur_month)+'-'+str(t)
    elif index2!=-1:
        if i.minute-int(strdata[slice(index2)])<0:
            t = i.day-1
        else:
            t = i.day
        return str(cur_month)+'-'+str(t)
    elif index3!=-1:
        t = i.day-1
        return str(cur_month)+'-'+str(t)
    else :
        if index4==-1 :
            strdata = str(i.year) +'-'+strdata
        return strdata

def prn_obj(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

uids = [1288915263,2418724427,2778292197,2418801567,3508612897,2258833123,2611704935,2417139911,2518353303,1936009361]
def create_class(tablename):
    return type('D',(Base,),dict( 
            __tablename__ = str(tablename),
            id = Column(Integer, primary_key=True),
            account_id = Column(Integer),
            account_name = Column(String),
            comments_number = Column(Integer),
            like_number = Column(Integer),
            forwarding_time = Column(String),
            forwarded_number = Column(Integer),
            creative_type = Column(String),
            material_type = Column(String),
            followers_count = Column(Integer),
            follow_count = Column(Integer),
            forward_sum_count = Column(Integer),
        )
    )
def separate_excel():
    i=0
    for uid in uids:
        i = i+1
        D = create_class('d'+str(i))

        for row in session.query(Data).filter(Data.account_id==str(uid)).all():
          
            # 将数据写入数据库
            ed_user = D(
                account_id = row.account_id,
                account_name = row.account_name,
                comments_number = row.comments_number,
                like_number = row.like_number,
                forwarding_time = row.forwarding_time,
                forwarded_number = row.forwarded_number,
                creative_type = row.creative_type,
                material_type = row.material_type,
                followers_count = row.followers_count,
                follow_count = row.follow_count,
                forward_sum_count = row.forward_sum_count,
            )
               
            session.add(ed_user)
        session.commit()    
        print(i)
separate_excel()