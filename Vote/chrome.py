from selenium import webdriver
 
browser = webdriver.Chrome()
browser.get('http://dev.hmalls.cn/seller_manager/')
browser.add_cookie({'a':'b'})
browser.maximize_window()
browser.save_screenshot('haha.png')
browser.close()