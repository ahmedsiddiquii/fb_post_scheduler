import undetected_chromedriver as uc
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
import pickle
import os
import webdriver_manager
def login_fb(username,password):



    # Initiate the ChromeDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-infobars')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-setuid-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-logging')
    options.add_argument('--disable-browser-side-navigation')
    options.add_argument('--remote-debugging-address=0.0.0.0')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--remote-debugging-port=0')
    options.add_argument('--disable-features=VizDisplayCompositor')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--start-maximized')
    options.add_argument('--disable-popup-blocking')
    options.add_argument('--disable-notifications')

    # initiate the driver
    # driver = uc.Chrome()
    driver = uc.Chrome(chrome_options=options)
    driver.get("https://web.facebook.com/")
    sleep(0.7)
    for i in range(1000):
        try:
            usernamee = driver.find_element(By.XPATH, "//input[@aria-label='Email address or phone number']")
            usernamee.send_keys(username)
            passwordd = driver.find_element(By.XPATH, "//input[@aria-label='Password']")
            passwordd.send_keys(password)
            sleep(1)
            break
        except:

            pass
    loginbtn = driver.find_element(By.XPATH,"//button[@type='submit']").click()
    sleep(10)
    try:
        notnowbtn = driver.find_element(By.XPATH, "//button[contains(text(),'Not Now')]")
        notnowbtn.click()
    except:
        pass
    try:
        login_button = driver.find_element(By.XPATH,"//button[@type='submit']")
        print("Login failed, login button still present")
        return None
    except:
        print("Login successful, login button not found")
        print(os.getcwd())
        with open("cookies/"+username+"_cookies.pkl", "wb") as f:
            pickle.dump(driver.get_cookies(), f)

        return  "cookies/"+username+"_cookies.pkl"



