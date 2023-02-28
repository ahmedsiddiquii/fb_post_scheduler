import sys
import os
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from polls.models import *
from django.contrib.auth.models import User

import threading
from django.utils import timezone
import pytz
import geoip2.database
from tzlocal import get_localzone
import datetime

import smtplib
import random
import string
from email.message import EmailMessage
import time
import scripts
from main import *

history = []

# MY_DATE = datetime.date.today()
# # MY_DATE = datetime.date(2023,2,19)
# def email_send(email,message):
#     gmail_user = 'instabotpbr@gmail.com'
#     gmail_password = 'rxokscbmhqqydpkt'
#
#     # choose from all lowercase letter
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(8))
#     print("Random string of length", 8, "is:", result_str)
#
#     sent_from = gmail_user
#     to = email
#     subject = 'Activity Summary'
#
#     template = "Your Daily Activity Summary : \n\n"+message
#     body = template
#     print(body)
#
#     email_text = template
#
#     msg = EmailMessage()
#     msg.set_content(body)
#
#     msg['Subject'] = subject
#     msg['From'] = sent_from
#     msg['To'] = to
#
#     try:
#         smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         smtp_server.ehlo()
#         smtp_server.login(gmail_user, gmail_password)
#         smtp_server.send_message(msg)
#         smtp_server.close()
#         print("Email sent successfully!")
#         return result_str
#     except Exception as ex:
#         print("Something went wrong….", ex)
#         return None
# def start_thread(start_time,end_time,status,accounts,comments,user,insta_user,insta_password,no_followers):
#     print(no_followers)
#
#     try:
#         main(start_time,end_time,status,accounts,comments,user,insta_user,insta_password,no_followers)
#         obj = Setting.objects.get(username=user)
#         obj.status = "on"
#         obj.save()
#     except Exception as e:
#         print(e)
#         obj = Setting.objects.get(username=user)
#         obj.status = "on"
#         obj.save()
#
# def send_email():
#     global MY_DATE
#     while True:
#         TEMP_DATE = datetime.date.today()
#         # TEMP_DATE = datetime.date(2023,2,19)
#         data = {}
#         if TEMP_DATE!=MY_DATE:
#
#             obj2 = list(Activity.objects.filter(date=MY_DATE).values())
#             print(obj2)
#             for record in obj2:
#                 username = record['user_email']
#                 data[username] = []
#
#             for record in obj2:
#
#                 username = record['user_email']
#                 user_obj = list(User.objects.filter(username=username).values())[0]
#                 user_email = user_obj['email']
#                 description = record['description']
#                 timestamp = record['timestamp']
#                 data[username].append([description,timestamp])
#             for key in data:
#                 message = ""
#                 for record in data[key]:
#                     message+=record[0]+" performs at "+record[1]+"\n"
#
#                 username = key
#                 user_obj = list(User.objects.filter(username=username).values())[0]
#                 user_email = user_obj['email']
#
#
#                 #send email code here sending message as arg
#                 email_send(user_email,message)
#             MY_DATE = TEMP_DATE




# def save_activity():
#     while True:
#         with open("activity.txt","r") as file:
#             lines= file.readlines()
#         if len(lines)>0:
#             for l in lines:
#                 l = l.replace("\n","").split("||")
#                 obj = Activity()
#                 obj.description = l[0]
#                 obj.date = datetime.datetime.strptime(l[1],"%Y-%m-%d").date()
#                 obj.timestamp = l[2]
#                 obj.user_email = l[3]
#                 obj.type = l[4]
#                 obj.save()
#
#         with open("activity.txt", "w") as file:
#             pass


def login_engine():
    while True:
        time.sleep(0.3)
        obj = list(FBAccount.objects.all().values())
        for i in obj :
            username = i['username']
            status= i['status']
            fb_email = i['email']
            fb_pass = i['password']
            if status == "run":
                print("running")
                s=threading.Thread(target=scripts.login_fb,args=(fb_email,fb_pass,))
                s.start()
                obj2 = FBAccount.objects.get(username=username)
                obj2.status = "running"
                obj2.save()



def start_thread(title,text,post_as,fb_email,fb_password,image,group,id):
    global history
    obj = BOT()
    obj.login(fb_email,fb_password)
    if post_as == 'Profile':
        pass
    else:
        obj.switch(post_as)
    try:
        obj.post(title,text,group,image)
    except Exception as e:
        print(e)
        pass
    obj.driver.close()
    history.remove(id)


def main2():
    global history
    # s=threading.Thread(target=save_activity)
    # s.start()
    s=threading.Thread(target=login_engine)
    s.start()
    while True:
        obj=PostModel.objects.all().values()
        for i in list(obj):
            status = i['status']
            if status=="on":
                post_time = i['time']
                every = i['every']
                post_time_hour, post_time_minute, post_time_sec = i['time'].hour, i['time'].minute, i['time'].second

                now_time = datetime.datetime.now()
                # Get the local timezone
                local_timezone = get_localzone()
                # Make the datetime object timezone-aware
                now_time = local_timezone.localize(now_time)
                # time=.localize(local_time)
                utc_time = timezone.localtime(now_time, timezone.utc)


                time_hour, time_minute, time_sec = utc_time.hour, utc_time.minute,utc_time.second
                day_name = datetime.datetime.now().strftime("%A")



                if post_time_hour==time_hour and post_time_minute==time_minute and post_time_sec==time_sec and every==day_name and i['id'] not in history:
                    title = i['title']
                    text = i['text']
                    post_as = i['post_as']
                    group  = i['group']
                    username = i['username']
                    obj2 = FBAccount.objects.filter(username=username).values()[0]
                    fb_email = obj2['email']
                    fb_password = obj2['password']

                    image=i['image']

                    print(title,text,post_as,group,username,fb_email,fb_password)
                    history.append(i['id'])
                    print(image)
                    s=threading.Thread(target=start_thread,args=(title,text,post_as,fb_email,fb_password,image,group,i['id']))
                    s.start()










if __name__ == "__main__":
    main2()
    # login_engine()
    # save_activity()
    # send_email()