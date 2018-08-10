# -*-coding:utf-8-*-
from	django.conf.urls	import	url
from	.	import	views
urlpatterns	=	[
	url(r'^$',	views.index,	name='index'),
    url(r'^hello/$',	views.hello,	name='hello'),
    url(r'^index$',views.index,name='index'),
    url(r'^(?P<question_id>[0-9]+)/result/$',views.result,name='result'),
    #url(r'^(?P<question_id>[0-9]+)/vote/$',views.vote,name='vote'),
    url(r'^vote/$',views.vote,name='vote'),
    url(r'^vote1/$',views.vote1,name='vote1'),
    url(r'^resultall/$',views.resultall,name='resultall'),
    url(r'^home/$',views.home,name='home'),
    url(r'^login/$', views.login, name='login'),
    url(r'^protected/$', views.protected, name='protected'),
    url(r'^test/$', views.test, name='login'),
]
