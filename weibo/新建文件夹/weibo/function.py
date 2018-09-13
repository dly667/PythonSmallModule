import datetime
i = datetime.datetime.now()
def deal_time(strdata):
    index1 = strdata.find('小时前', 0, len(strdata))
    index2 = strdata.find('分钟前', 0, len(strdata))
    index3 = strdata.find('昨天', 0, len(strdata))

    if index1!= -1:
        
        if i.hour-int(strdata[slice(index1)])<0:
            t = i.day-1
        else:
            t = i.day
        return str(i.month)+'-'+str(t)
    elif index2!=-1:
        if i.minute-strdata[slice(index2)]<0:
            t = i.day-1
        else:
            t = i.day
        return str(i.month)+'-'+str(t)
    elif index3!=-1:
        t = i.day-1
        return str(i.month)+'-'+str(t)
        
