'''
定义learning_logs的url
'''
from django.conf.urls import include, url
from . import views

app_name = 'learning_logs'
urlpatterns = [
    # 主页
    url(r'^$', views.index, name='index'),
    # 显示所有的主题
    url('^topics/$', views.topics, name='topics'),
    # 特定主题的详细页面
    url('^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),
    # 用于添加新主题的网页
    url('^new_topic/$', views.new_topic, name='new_topic'),
    # 用于添加新条目
    url('^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    # 用于编辑条目
    url('^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),
]
