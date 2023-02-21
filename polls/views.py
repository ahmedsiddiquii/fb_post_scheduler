from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import views as auth_views
from .models import *
from django.contrib import messages,auth
from django.template import loader
from selenium.webdriver.support.ui import Select
from selenium import webdriver
import time
# path="E:/Analyt IQ/28th/chromedriver"
# driver = webdriver.Chrome(path)

# Create your views here.
def login(request):
   return render(request, "index.html")   

def home(request):
   return render(request,'home.html')

def post_p(request):
   return render(request,'post.html')

def title(request):
   return render(request,'title.html')

def login_user(request):
   print("aaaaa")
   if request.method == 'POST':
      username = request.POST['username']
      password = request.POST['password']
      user = auth.authenticate(username=username, password=password)
      if user is not None:
         if user.is_active:
            auth.login(request, user)
         
         return render('home.html')
      else:
         
         return render('login')
   else:
      return render(request, 'index.html')

def title_post(request):
   print("bbbbbbbbbbbb")
   if request.method == 'GET':

      print("aaaaaaaa")
      title=request.POST['title']
      message=request.POST['message']
      print(title,"title====title")
      print(message,"message====message")

      # driver.get("https://www.facebook.com/")

      # email = "+91971865-1836"
      # password = "stonewhite@078"
      # post= "Hi"+"how are you"
      # # post = str(title+message)

      # def post():
         

      #    email_input = driver.find_element(by="xpath",value="//input[@aria-label='Email address or phone number']")
      #    email_input.send_keys(email)

      #    password_input = driver.find_element(by="xpath",value="//input[@aria-label='Password']")
      #    password_input.send_keys(password)

      #    button = driver.find_element(by="xpath",value="//button[@name='login']").click()
      #    time.sleep(5)

      #    post_click = driver.find_element(by="xpath",value="//div[@class='x1lkfr7t xkjl1po x1mzt3pk xh8yej3 x13faqbe xi81zsa']").click()
      #    time.sleep(10)

      #    post_input = driver.find_element(by="xpath",value="//div[@class='x78zum5 xl56j7k']")
      #    post_input.send_keys(post)

      #    send=driver.find_element(by="xpath",value="//*[contains(text(), 'post')]").click()
      #    print(send)

   return render(request,'post.html')