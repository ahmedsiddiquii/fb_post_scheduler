from django.urls import path
from polls import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('home', views.home,name="home"),
    path('post', views.post_p,name='post'),

    path('title', views.title,name='title'),
    path('title', views.title_post, name="title_post"),
path('submit', views.submit, name="submit"),
    path('login_user/', views.login_user, name="login_user"),
path('',views.login),
path('save_page', views.save_page,name="save_page"),
path('delete_page/<str:page_id>/',views.delete_page,name="delete_page"),
path('delete_group/<str:group_id>/',views.delete_group,name="delete_group"),
path('edit_post/<int:id>/',views.edit_post,name="edit_post"),
path('off_post/<str:title>/',views.off_post,name="off_post"),
path('on_post/<str:title>/',views.on_post,name="on_post"),
path('delete_post/<str:title>/',views.delete_post,name="delete_post"),
path('update_post', views.update_post,name='update_post'),
path('add_account', views.add_account,name='add_account'),
path('logout_user', views.logout_user,name='logout_user'),
path('group', views.group,name='group'),
path('save_group', views.save_group,name='save_group'),

path('login_with_facebook_cookies', views.login_with_facebook_cookies,name='login_with_facebook_cookies'),
]

urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)