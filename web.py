#!/usr/local/python/bin/python3.7
#-*-coding:utf-8-*-
import pymysql
import os
import hashlib
import pickle
import re
import time
import cgi
import cgitb
from django.shortcuts import render, HttpResponse
from	django.shortcuts	import	render,	get_object_or_404,redirect

def update_pass():
    name=input('请输入用户名:\n')
    passwd=input('请输入密码:\n')
    newpasswd = input('请输入新密码:\n')
    sql = "update person set password='%s' where name='%s' and password='%s'" % (newpasswd,name,passwd)
    try:
        use_db(sql)
        print('修改密码成功!')
    #results = cur.fetchall()
    except Exception:
        print("修改数据库失败!")
        raise;

def login(name,passwd):
    # name = input('请输入用户名:\n')
    # passwd = input('请输入密码:\n')
    sql="select * from person  where name='%s' and password='%s'" % (name,passwd)
    re=use_db(sql)
    if re:
        return 1;
        # print('登陆成功!')
    else:
        return 0;
        # print('用户名或密码错误！')
def login1(request):
    username=request.POST.get('username')
    password = request.POST.get('password')
    x=login(username,password)
    if x:
        return HttpResponse('登陆成功！')
    else:
        return HttpResponse('用户名或密码错误')


def use_db(sql):
    db = pymysql.connect(host="localhost", user="root", password="123456", db="db1", port=3306)
    cur = db.cursor()
    cur.execute(sql)
    re=cur.execute(sql)
    db.commit()
    db.close()
    return re

def register(name,passwd):
    # name = input('请输入用户名:\n')
    # passwd = input('请输入密码:\n')
    sql = "select * from person  where name='%s' " % name
    re = use_db(sql)
    if re:
        print('用户已经存在！')
    else:
        sql="insert into   person(name,password)  values('%s',%s)" % (name,passwd)
        use_db(sql)
        print('注册成功！')


def find(filename):
    dirt1={}
    g = os.walk(filename)
    for path, d, filelist in g:
        for filename in filelist:
            dirt1[ os.path.join(path, filename)]=''
    return dirt1

def md5sum(filename):
    m=hashlib.md5()
    with open(filename,'rb') as f:
        if f:
            tmp=f.read(4096)
            m.update(tmp)
        return m.hexdigest()

def joins(filename):
    dirt1=find(filename)
    for i in dirt1:
        dirt1[i]=md5sum(i)
    return dirt1

def cp(filea,fileb):
    with open(filea,'rb') as f:
        with open(fileb, 'wb') as d:
            tmp=f.read()
            d.write(tmp)

# if __name__ == '__main__':
    # while 1:
    #     prompt = '''(0): 登陆
    # (1): 修改信息
    # (2): 注册
    # (3): 退出
    # '''
    #     inputs=input(prompt)
    #     if inputs=='3':
    #         print('再见！')
    #         exit()
    #     cmds = {'0': login, '1': update_pass,'2':register}
    #     cmds[inputs]()

# print( md5sum('/tmp/passwd'))
#print(find('/tmp/new'))
#print(joins('/tmp/xxx'))
# with open('/tmp/record','wb') as f:
#     pickle.dump(joins('/tmp/xxx'),f)
# if __name__ == '__main__':
#
#     with open('/tmp/record','rb') as f:
#         dir1=pickle.load(f)
#         dir2=joins('/tmp/xxx')
#         dir_time='backup'+time.strftime('%Y-%m-%d', time.localtime())
#         for i in dir1 and dir2:
#             (dirr,filename) = os.path.split(i);
#             j=re.sub('xxx',dir_time,dirr)
#             if not os.path.exists(j):
#                 os.makedirs(j)
#
#             m = re.sub('xxx',dir_time, i)
#             if dir1[i]!=dir2[i]:
#                 cp(i,m)
#         for i in dir2 :
#             if i not in dir1:
#                 (dirr, filename) = os.path.split(i);
#                 j = re.sub('xxx', dir_time, dirr)
#                 if not os.path.exists(j):
#                     os.makedirs(j)
#                 m = re.sub('xxx', dir_time, i)
#                 cp(i,m)
#         with open('/tmp/record', 'wb') as d:
#             pickle.dump(dir2,d)
    form=cgi.FieldStorage()
    name=form.getvalue('name')
    password=form.getvalue('password')
    register(name,password)

