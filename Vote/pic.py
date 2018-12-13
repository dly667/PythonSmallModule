from selenium import webdriver
import time



# from PIL import ImageGrab
# im = ImageGrab.grab()
# im.save('1112.png')

class Photo():
    def photo(self,ip):
     
        
        url = 'http://ucp164332.a.stonevote.net/poll/a70e584d-75c8-638c-b2d7-1789d7d355c4.html?searchkey=%E6%B1%A4%E6%B4%AA%E6%9E%97'
        # url = 'http://www.baidu.com'
        # brower = webdriver.Chrome()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--proxy-server=http://'+ip)
        brower = webdriver.Chrome(chrome_options=chrome_options)
        # brower.save_screenshot('1.png')
        brower.get(url)
        # brower.save_screenshot('1.png')
        brower.implicitly_wait(50)
        cookie_t = {
            'domain':'.stonevote.net',
            'name':'V-8db9d1b3-75c3-cb18-b505-50e4927caaa620181213',
            'value':'1'
        }
        brower.add_cookie(cookie_t)
        brower.get(url)
        # brower.save_screenshot('2.png')
        time.sleep(2)
        self.execute_js(brower)
        # brower.save_screenshot('3.png')
        vote_ticket_elm=brower.find_element_by_xpath("//div[@class='wrap']//div[2]/div[7]/p")
        vote_ticket=vote_ticket_elm.text.strip()
    
        n=0
        time.sleep(2)
        while True:
            try:
                elm=brower.find_element_by_xpath("//*[@id='submitalertdiv']//span")
            except Exception as e:
                elm=''
            print(elm)
            if not elm:
                break
            if n>3:
                break
            n+=1
            time.sleep(1)
        
        
        
     
        # for (k,v) in  cookies.items():
        #     cookie_t={
        #         'domain':'.stonevote.net',
        #         'name': str(k),
        #         'value':str(v),
        #         'path':'/'
        #     }
        #     brower.add_cookie(cookie_t)
        # print(brower.cookies)

       
        
        # brower.maximize_window()
        time.sleep(2)
        time_local=time.localtime()
        str_time=str(time_local[0])+str(time_local[1])+str(time_local[2])+str(time_local[3])+str(time_local[4])+str(time_local[5])
        picName = 'results/'+str_time+'_'+vote_ticket+'.png'
        brower.save_screenshot(picName)
        # print(brower.current_url)
        
        # brower.save_screenshot('4.png')
        # brower.get_screenshot_as_png()
        # input('y/n')
        #brower.close()
        brower.quit()
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
if __name__ == '__main__':
    Photo().photo({'a':'b','c':'d'})