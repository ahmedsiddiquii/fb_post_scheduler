from django.contrib import admin
from django.urls import path
from polls import views
from django.urls import path,include
urlpatterns = [
    path('',include('polls.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),


]
