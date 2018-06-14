'''
定义learning_logs的url
'''
from django.conf.urls import include, url
from django.contrib.auth.views import login
from . import views

app_name = 'users'
urlpatterns = [
    # 登陆界面
    url('^login/$', login, {'template_name': 'users/login.html'}, name='login'),
    #注销
    url(r'^logout/$',views.logout_view,name='logout'),
    #创建用户
    url('^register/$',views.register,name='register')
]
