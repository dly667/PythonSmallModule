from selenium import webdriver
import time
from proxy import ProxyIp



# from PIL import ImageGrab
# im = ImageGrab.grab()
# im.save('1112.png')

class Photo():
    def __init__(self):
        # ip=ProxyIp().get_ip_ad()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--proxy-server=http://'+ip)
        self.brower = webdriver.Chrome(chrome_options=chrome_options)
    def photo(self):
        url = 'http://ucp164332.a.stonevote.net/poll/f7d9c376-3213-d21f-43fe-d9031225ee39.html?searchkey=20'
        # url = 'http://www.baidu.com'
        # brower = webdriver.Chrome()
        # chrome_options = webdriver.ChromeOptions()
        # # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--proxy-server=http://'+self.ip)
        # brower = webdriver.Chrome(chrome_options=chrome_options)

        # brower.save_screenshot('1.png')
        self.brower.get(url)
        # brower.save_screenshot('1.png')
        self.brower.implicitly_wait(30)
        cookie_t = {
            'domain':'.stonevote.net',
            'name':'V-a3920a26-f49c-dfff-5820-7d7f873fd8b520180722',
            'value':'1'
        }
        self.brower.add_cookie(cookie_t)
        self.brower.refresh()
        self.brower.get(url)
        # brower.save_screenshot('2.png')
        time.sleep(2)
        # brower.save_screenshot('3.png')
        
        
        
     
        # for (k,v) in  cookies.items():
        #     cookie_t={
        #         'domain':'.stonevote.net',
        #         'name': str(k),
        #         'value':str(v),
        #         'path':'/'
        #     }
        #     brower.add_cookie(cookie_t)
        # print(brower.cookies)

        print(self.brower.get_cookies())
        
        # brower.maximize_window()
        time.sleep(2)
        self.save_png()
        # print(brower.current_url)
        
        # brower.save_screenshot('4.png')
        # brower.get_screenshot_as_png()
        # input('y/n')
        #brower.close()
        # self.brower.quit()
    def execute_js(self,brower):
        brower.execute_script("""
        (function () {
        var y = 0;
        var step = 40;
        window.scroll(0, 0);
    
        function f() {
            if (y < document.body.scrollHeight-800) {
            y += step;
            window.scroll(0, y);
            setTimeout(f, 50);
            } else {
            
            }
        }
    
        setTimeout(f, 1000);
        })();
        """)
    def close(self):
        self.brower.quit()
    def save_png(self):
        self.execute_js(self.brower)
        vote_ticket_elm=self.brower.find_element_by_xpath("//*[@id='op_4181079']/div/div[3]/div")
        vote_ticket=vote_ticket_elm.text.strip()
        print(vote_ticket)
        n=0
        time.sleep(2)
        while True:
            try:
                elm=self.brower.find_element_by_xpath("//*[@id='submitalertdiv']//span")
            except Exception as e:
                elm=''
            print(elm)
            if not elm:
                break
            if n>3:
                break
            n+=1
            time.sleep(1)
        time_local=time.localtime()
        str_time=str(time_local[0])+str(time_local[1])+str(time_local[2])+str(time_local[3])+str(time_local[4])+str(time_local[5])
        picName = 'results/'+str_time+'_'+vote_ticket+'.png'
        self.brower.save_screenshot(picName)
def main():
    p_obj=Photo()
    p_obj.photo()
    while True:
        p_obj.save_png()
        p_obj.brower.refresh()

if __name__ == '__main__':
    # Photo().photo({'a':'b','c':'d'})
    main()