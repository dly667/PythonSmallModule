import requests
import random
class ProxyIp():
    def get_ip_ad(self):
      
        r = requests.get("http://dynamic.goubanjia.com/dynamic/get/3570e2fa4d368c2a31a2973b056ab9c2%20.html?sep=3")
        # 
        ip_list=r.text.split('\n')[:-1]
        # print(ip_list)
        ip=random.choice(ip_list)
        return ip

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
            r = requests.get('http://icanhazip.com/',proxies=proxies,timeout=5)
            # r1 = requests.get('https://www.baidu.com/', proxies={'https':self.get_ip_ad()})
            print(r.text)
            return 1
        except Exception as e:
            print(e)
            return 0
        
    def test_all(self,ip_list):
        n=0
        for item in ip_list:
            if self.test_one(item):
                n+=1
        print("有效ip数：%d"%n)
        print("总ip数：%d"%len(ip_list))

if __name__ == "__main__":
    # ProxyIp().test()
    obj=ProxyIp()
    ip_list=obj.get_ip_ad()
    obj.test_all(ip_list)