import os

from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
from time import sleep
import pickle
import undetected_chromedriver as uc

class BOT:
    def __int__(self):
        self.self.driver = None
    def login(self,usern,passw):

        options = webdriver.ChromeOptions()
        options.add_argument('--disable-infobars')
        options.add_argument('--disable-extensions')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-setuid-sandbox')
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-logging')
        options.add_argument("--disable-notifications")
        options.add_argument('--disable-browser-side-navigation')
        options.add_argument('--remote-debugging-address=0.0.0.0')
        options.add_argument('--remote-debugging-port=9222')
        options.add_argument('--remote-debugging-port=0')
        options.add_argument('--disable-features=VizDisplayCompositor')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--start-maximized')
        options.add_argument('--disable-popup-blocking')
        options.add_argument('--disable-notifications')
        print(True)
        # initiate the self.driver
        # self.driver = uc.Chrome()
        self.driver = uc.Chrome(options=options)
        # login

        print("logging in")
        # self.driver = uc.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://www.facebook.com/")
        # InstagramBot.sleeplimit()
        try:
            cookies = pickle.load(open("cookies/" + usern + "_cookies.pkl", "rb"))
            for cookie in cookies:
                self.driver.add_cookie(cookie)
            self.driver.get("https://www.facebook.com/")
        except:
            pass

# usern = "+91971850-3128"
# passw = "gangster@099"

    def switch(self,page):
        self.driver.get("https://web.facebook.com/"+page)
        sleep(5)
        try:
            btn=self.driver.find_element(by='xpath',value="//span[text()='Switch now']")
            btn.click()
        except:
            btn = self.driver.find_element(by='xpath', value="//span[text()='Switch Now']")
            btn.click()
        sleep(3)
        return 
    def page_post(self,title,text,page,image_path):
        if page.isdigit()==True:
            self.driver.get("https://www.facebook.com/profile.php?id=" + page)
        else:
            self.driver.get("https://www.facebook.com/" + page)
        time.sleep(5)
        button_click =  self.driver.find_element("xpath",
                                                 """//span[text()="What's on your mind?"]""").click()


        time.sleep(13)
        post_input = self.driver.find_element(by="xpath", value="//div[@data-contents='true']")
        post_input.click()
        post_input.send_keys(text)
        sleep(5)
        image_btn= self.driver.find_element("xpath","//div[@aria-label='Photo/video']")
        image_btn.click()
        sleep(3)
        image = self.driver.find_elements(by='xpath', value="//input[@type='file']")[-1]
        print(os.getcwd() + r"media/" + image_path)
        image.send_keys(os.getcwd() + r"/media/" + image_path)
        sleep(4)

        time.sleep(1)
        try:
            send = self.driver.find_element(by="xpath", value="//span[text()='post']").click()
        except:
            send = self.driver.find_element(by="xpath", value="//span[text()='Post']").click()

        sleep(15)
        self.driver.get(self.driver.current_url+"&sk=grid")
        sleep(7)
        link= self.driver.find_element("xpath","//div[@class='x1e56ztr xcud41i']//a[@aria-label][@tabindex='0'][@role='link']").get_attribute("href")


        print(link)
        return link
    def group_post(self,link,group_id):
        self.driver.get("https://www.facebook.com/groups/" + group_id)
        time.sleep(5)
        button_click = self.driver.find_element(by="xpath", value="//span[text()='Write something...']").click()
        time.sleep(13)
        post_input = self.driver.find_element(by="xpath", value="//div[@data-contents='true']")
        post_input.click()
        post_input.send_keys(link)
        sleep(9)
        try:
            send = self.driver.find_element(by="xpath", value="//span[text()='post']").click()
        except:
            send = self.driver.find_element(by="xpath", value="//span[text()='Post']").click()

        sleep(5)
    def post(self,title,text,group,image_path):
        post = title+"\n"+text
    
        
        group = group
        self.driver.get("https://www.facebook.com/groups/" + group)
        time.sleep(5)
        button_click = self.driver.find_element(by="xpath", value="//span[text()='Write something...']").click()
        time.sleep(13)
        post_input = self.driver.find_element(by="xpath", value="//div[@data-contents='true']")
        post_input.click()
        post_input.send_keys(post)
        sleep(5)
    
        image = self.driver.find_elements(by='xpath', value="//input[@type='file']")[-1]
        print(os.getcwd()+r"media/"+image_path)
        image.send_keys(os.getcwd()+r"/media/"+image_path)
        sleep(4)
    
        time.sleep(1)
        try:
            send = self.driver.find_element(by="xpath", value="//span[text()='post']").click()
        except:
            send = self.driver.find_element(by="xpath", value="//span[text()='Post']").click()
    
        sleep(5)

        print(send)


# obj = BOT()
# obj.login(usern="+91971850-3128",passw="gangster@099")
# obj.switch("https://www.facebook.com/profile.php?id=100090854342969")
# obj.post("Hey everyone","","528192982698012","images/WhatsApp_Image_2023-02-26_at_5.14.56_PM.jpeg")





