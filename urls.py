#-*-coding:utf-8-*-
# from	django.conf.urls	import	url
# from . import web
#
# urlpatterns	=	[
#     url(r'login',	web.login1,	name='login1')
#
# ]
import requests

url='http://127.0.0.1/polls/vote/'
data={'choice':1,'question_id':1}
r=requests.post(url,data)
