import requests
import random
class ProxyIp():
    def get_ip_ad(self):
        url="http://dynamic.goubanjia.com/dynamic/get/3570e2fa4d368c2a31a2973b056ab9c2.html?sep=3&random=true"
        r = requests.get(url)
        # 
        ip_list=r.text.split('\n')[:-1]
        # print(ip_list)
        # ip=random.choice(ip_list)
        # ip_random=self.test_all(ip_list)
        # print(ip_random)
        # return random.choice(ip_list)
        return ip_list

    def test(self):
        proxies={'http':'http://'+self.get_ip_ad().strip()}
        print(proxies)
        r = requests.get('http://icanhazip.com/',proxies=proxies )
        # r1 = requests.get('https://www.baidu.com/', proxies={'https':self.get_ip_ad()})
        print(r.text)
    def test_one(self,ip):
        try:
            proxies={'http':'http://'+ip.strip()}
            print(proxies)
            r = requests.get('http://icanhazip.com/',proxies=proxies,timeout=2)
            # r1 = requests.get('https://www.baidu.com/', proxies={'https':self.get_ip_ad()})
            print(r.text)
            return 1
        except Exception as e:
            print(e)
            return 0
        
    def test_all(self,ip_list):
        n=0
        list_ip=[]
        for i in range(len(ip_list)):
            if self.test_one(ip_list[i]):
                n+=1
                list_ip.append(ip_list[i])
                # if n>5:
                #     return list_ip
                
        print("有效ip数：%d"%n)
        print("总ip数：%d"%len(ip_list))
        return list_ip

if __name__ == "__main__":
    # ProxyIp().test()
    obj=ProxyIp()
    ip_item=obj.get_ip_ad()
    print(ip_item)
    # ip_list=obj.get_ip_ad()
    obj.test_all(ip_item)