from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
driver = webdriver.Chrome()
# login
driver.get("https://www.facebook.com/")

email = "+91971865-1836"
password = "stonewhite@078"

def post():
    post = "hello every one"

    email_input = driver.find_element(by="xpath",value="//input[@aria-label='Email address or phone number']")
    email_input.send_keys(email)

    password_input = driver.find_element(by="xpath",value="//input[@aria-label='Password']")
    password_input.send_keys(password)

    button = driver.find_element(by="xpath",value="//button[@name='login']").click()
    time.sleep(2)
    group="3854087768006145"
    driver.get("https://www.facebook.com/groups/"+group)
    time.sleep(5)
    button_click = driver.find_element(by="xpath",value="//span[@class='x1lliihq x6ikm8r x10wlt62 x1n2onr6']").click()
    time.sleep(5)

    post_input = driver.find_element(by="xpath",value="//div[@class'x9f619 x1lliihq x5yr21d xh8yej3']")
    post_input.send_keys(post)
    time.sleep(1)
    send=driver.find_element(by="xpath",value="//*[contains(text(), 'post')]").click()
    print(send)
    

post()


    # post_click = driver.find_element(by="xpath",value="//div[@class='x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe xi81zsa']").click()
    # time.sleep(10)

    # post_input = driver.find_element(by="xpath",value="//div[@class='x78zum5 xl56j7k']")
    # post_input.send_keys(post)

    # send=driver.find_element(by="xpath",value="//*[contains(text(), 'post')]").click()
    # print(send)



