import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# 若快验证码识别类
class RuoKuai():
    config = {
        'username': 'dly996',
        'password': 'Asdf3344',
        'typeid': '3050',
        'softid': '108574',
        'softkey': 'cf826a0d7f5c40278c4b7724d5ace5c0',
    }
    url = 'http://api.ruokuai.com/create.json'
    '''
    username	true	string	用户名。
    password	true	string	用户密码。(支持32位MD5)
    typeid	true	int	题目类型，参考(类型表)或联系客服。
    timeout	false	int	任务超时时间，默认与最小值为60秒。
    softid	true	int	软件ID，开发者可自行申请。
    softkey	true	string	软件KEY，开发者可自行申请。
    image
    '''

    '''
    Accept: */*
    Accept-Language: zh-cn
    Content-Type: multipart/form-data; boundary=-------------RK （注释：请求头主要设置这行，一般情况下其他行默认,RK可以换成任意字符串，注意与下面分割字符串前面"-"的个数）
    Host: api.ruokuai.com
    '''
    headers = {
        'Content-Type': 'multipart/form-data; boundary=-------------RK'
    }

    def get_post_data(self, filename):
        fields = RuoKuai.config
        fields['image'] = (filename, open(filename, 'rb'), 'multipart/form-data')
        return MultipartEncoder(
            fields=fields,
            boundary='-------------RK'
        )

    def start(self,filename):
        data = self.get_post_data(str(filename))
        return requests.post(RuoKuai.url, headers=RuoKuai.headers, data=data,timeout=30)



