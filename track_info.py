import string
import time
import random
from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()
firefox_options.add_argument('--headless')
firefox_options.add_argument('--disable-gpu')

class TrackInfo:
    
    def __init__(self):
        super(TrackInfo).__init__()
        self.webdriver = webdriver.Firefox(firefox_options=firefox_options, executable_path='./geckodriver')
        self.webdriver.get("https://baidu.com")     # Keep Browse alive
        random.seed(time.time())
    
    def get_package_info(self, package_num: string, sf_phone: string=None) -> []:
        self.webdriver.get("https://m.kuaidi100.com/result.jsp?nu="+package_num)
        if sf_phone is not None:
            shunfeng=1
        try:
            self.webdriver.find_element_by_class_name("more-text").click()
        except:
            print("Expanded")
        state = self.webdriver.find_element_by_class_name("result-list") #.find_element_by_class_name("sortup")
        print(state.text)
        self.webdriver.close()

    # def __del__(self):
    #     self.webdriver.quit()

if __name__=="__main__":
    tracker = TrackInfo()
    tracker.get_package_info("4300454679951")
    tracker.webdriver.quit()


