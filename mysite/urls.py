from django.contrib import admin
from django.urls import path
from polls import views
urlpatterns = [
    path('',views.login),
    path('home.html',views.home),
    path('post.html',views.post_p),
    path('title.html',views.title),
    path('title.html',views.title_post,name="title_post"),
    path('login_user/',views.login_user,name="login_user"),

]
