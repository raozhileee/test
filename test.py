# -*-coding:utf-8-*-

# import shutil
# import os
# def exist(path):
#     return os.path.exists(path)
# def write(words,path):
#     with open(path,'w') as f:
#         f.write(words)
#         f.write('\n')
# while 1:
#     path=input('please input path:\n')
#     words=input('please input words:\n')
#     if not exist(path):
#         write(words,path)
#
#         print('save file successed!')
#         exit()
#     else:
#         print('file already exist ,please try again!\n')
#         continue

# import random
# a='hello'
# b=[10,20,30]
# num_list=[random.randint(1,100) for i in range(10)]
# print(list(a))
# print(list(b))
# print(str(b))
# print(tuple(b))

#
# alist=[10,'name']
# for i in range(len(alist)):
#     print('%s:%s' % (i,alist[i]))
# for i in enumerate(alist):
#     print('%s %s' % (i[0],i[1]))
# for i,j in enumerate(alist):
#     print('%s %s' % (i,j))

# atulp=(11,22,33,4,55,66,7,8,9)
# print(sorted(atulp))
# for i in reversed(atulp):
#     print(i,end='~')
# import string
# import keyword
# first_chs=string.ascii_letters+'_'
# all_chs=first_chs+string.digits
#
# while 1:
#     word=input('please input:\n')
#     if word in keyword.kwlist:
#         print('is keyword!')
#         continue
#     for i in range(len(word)):
#         if word[0] not in first_chs:
#             print('"%s"st is not right' % 1)
#             break
#         if word[i] not in all_chs:
#             print('"%s"st is not right' % str(i+1))
#             break
#     print('ok!')

#
# import subprocess
# import sys
# import random
# def adduser(username,password,fname):
#     data='''user infornation:
#     %s %s
#     '''
#     subprocess.call('useradd %s' % username,shell=True)
#     subprocess.call('echo %s | passwd --stdin %s' % (password,username),shell=True)
#     with open(fname,'a') as f:
#         f.write(data % (username,password))
# username=input('please input username:\n')
# password=input('please input password:\n')
# adduser(username,password,'/tmp/1.txt')

# alist=[0,1,2,3,4,5,6,7]
# print(alist)
# alist.append(8)
# print(alist)
# alist.remove(0)
# print(alist)
# print( alist.index(5))
# alist.insert(0,89)
# alist.pop(3)
# print(alist)
# alist.reverse()
# print(alist)
# print( alist.count(4))
# alist.extend([111,222])


# def pop1(pop_str,stack):
#     stack.append(pop_str)
#
# def deltle(stack):
#     stack.pop(-1)
#
# stack=[]
# while 1:
#     x=input('ni yao de cao zuo: \n 0:query\n 1:insert\n 2:delete\n 3:exit\n'.center(50,'~'))
#     if x=='0':
#         print('stack:    %s\n' % stack)
#     elif x=='1':
#         insert_info=input('please input the values:'.center(50,'~'))
#         pop1(insert_info,stack)
#         print('insert successed!'.center(50,'~'))
#     elif x=='2':
#         if stack:
#             deltle(stack)
#             print('delete successed\n'.center(50,'~'))
#         else:
#             print('stack is empty cannot delete !'.center(50,'~'))
#             continue
#     elif x=='3':
#         print('bye'.center(50,'~'),'\n')
#         exit()
#     else:
#         print('input error please input again !!!'.center(50,'~'))
# import keyword
# a=[1,2,3]
# b='dsf'
# a.extend('dsds')
# print('{} {}'.format(a,b))


# str1='my name is mr green'
# str2='HELLO'
# print(str1[11::1])
# str11='  '+str1
# print(str11)


# def p1():
#     print('p1')
# def p2():
#     print('p2')
# def p3():
#     print('p3')
# while 1:
#     cmds={'1':p1,'2':p2,'3':p3}
#     x=input('please input:\n')
#     if x not in ['1','2','3']:
#         print('error input')
#         continue
#     cmds[x]()

# bdict=dict([('name','tom'),('age',24)])
# print(bdict)
# print( len(bdict))
# for i,j in enumerate( bdict):
#     print('%s %s' % (i,str(j)))
# bdict['haha']='smg'
# print(bdict)
# print(hash(10))
# print( bdict.keys())
# print(bdict.values())
# print(bdict.items())
# print( bdict.get('name'))
# print(bdict.get('xx','not found'))
# bdict.update({'aada':'12345674'})
# print(bdict)

# import web
# def register():
#     pass
#
# def login():
#     pass
#
#
# def show_menu():
#     cmds={'0':register,'1':login}
#     prompt='''(0):register
# (1):login
# (2):exit
# please input you choice(0/1/2):
# '''
#     while 1:
#         choice=input(prompt)
#         if choice not in cmds:
#             print('error input')
#             continue
#         if choice=='2':
#             exit()
#         cmds[choice]()
# show_menu()

#
# import time
# length=100
# count=0
# x=1
# while 1:
#     try:
#         print('\r%s<->%s' % ('-' * count,'-' * (length-count)),end='')
#         time.sleep(0.05)
#         if count==length and x==1:
#             x=-1
#             count -=1
#             continue
#
#
#         if count==0 and x==-1:
#             x=1
#             count += 1
#             continue
#
#         if x==1:
#             count += 1
#         if x==-1:
#             count -=1
#     except (InterruptedError,KeyboardInterrupt):
#         print('\n沙雕，再见！！！')
#         exit()

# aset=set('abc')
# bset=set('cde')
# print(aset&bset)
# print(aset|bset)
# print(aset-bset)
# print( aset.add('123'))
# print( aset.update(['aaa','bbb']))
# print( aset.remove('bbb'))
# cset=aset.add('3456')
# print( cset)

# while 1:
#     try:
#         n=int(input('input:\n'))
#     except  (ZeroDivisionError,ValueError):
#         print('input invalid!!！\n')
#         continue
#     except KeyboardInterrupt:
#         print('再见,绿茶裱！！！')
#     print(n / 10)


# import os
# print(os.getcwd())
# print(os.mkdir('/tmp/xxx'))

# import pickle
# shop_list=['agg','apple','penck']
# with open('/tmp/shop','wb') as f:
#     pickle.dump(shop_list,f)
# with open('/tmp/shop','rb') as d:
#     alist=pickle.load(d)
#     print(alist)


#
# import pickle
# import time
# def show_menu():
#         prompt='''(0): 记账
# (1): 查询
# (2): 退出
# 请输入你要进行的操作(0/1/2):
# '''
#         choice=input(prompt)
#         if choice=='2':
#             exit()
#         if choice=='0':
#             record()
#         if choice=='1':
#             query()
# def record():
#     dt=time.strftime('%Y-%m-%d %X',time.localtime())
#     type=input('请输入类型 （0）：支出  （1）：收入\n')
#     money=int( input('请输入金额：\n'))
#     commit=input('请输入备注：\n')
#     if type=='0':
#         money=-money
#         type='支出'
#     if type=='1':
#         type='收入'
#     list=[dt,type,money,commit]
#     with open('/tmp/shop', 'ab') as f:
#         pickle.dump(list,f)
# def query():
#     with open('/tmp/shop', 'rb') as d:
#         alist=[' ']
#         money_all=10000
#         try:
#             print('记录时间                   类型   金额   备注')
#             while alist:
#                 alist = pickle.load(d)
#                 money_all+=alist[2]
#                 print(alist)
#         except EOFError:
#             print('\n')
#             print('余额：%d' % money_all)
#             print('')
# while 1:
#     show_menu()

#
# import random
# def fun_int():
#     y=random.randint(1,100)
#     return y
# def fun_choice():
#     z=random.choice('+-')
#     return z
# while 1:
#     choice1=input('0:算术\n1:退出\n')
#     if choice1=='0':
#         i=1
#         x = fun_int()
#         y = fun_int()
#         op = fun_choice()
#         if x < y:
#             x, y = y, x
#         while i<=3:
#
#             result=int(input('%s %s %s=\n' % (x,op,y)))
#             if op=='-':
#                 if result==x-y:
#                     print('对了!!!')
#                     break
#                 else:
#                     print('错了！')
#
#             if op=='+':
#                 if result==x+y:
#                     print('对了!!!')
#                     break
#                 else:
#                     print('错了！')
#             i+=1
#         else:
#             print('%s %s %s=%s\n' % (x,op,y,x+y))

# import random
# alist=[random.randint(1,100) for i in range(10)]
# print(alist)
# result=map(lambda x:x*x,alist)
# print(list(result))


# import functools
# def foo(a,b,c,d,e,f):
#     return a+b+c+d+e+f
#
# add = functools.partial(foo,a=1,b=2,c=3,d=4)
# print(add(e=5,f=6))


# import tkinter
# root= tkinter.Tk()
# lb=tkinter.Label(text='hello')
# lb.pack()
# root.mainloop()

# def sort(alist):
#     if len(alist)<2:
#         return alist
#     middle=alist[0]
#     small=[]
#     large=[]
#     for i in alist[1:]:
#         if i< middle:
#             small.append(i)
#         else:
#             large.append(i)
#     return sort(small)+[middle]+sort(large)
# import random
# alist=[ random.randint(1,100) for i in range(10) ]
# blist=sort(alist)
# print(blist)


# def mygen():
#     yield 'hahah'
#     a=10+20
#     yield a
#     yield [1,12,3]
#
# m=mygen()
# for i in m:
#     print(i)
# m = mygen()
# for n in m:
#     print(n)


# def block(f):
#     block=[]
#     count=0
#     for line in f:
#         block.append(line)
#         count+=1
#     yield block
#
# f=open('/tmp/passwd')
# for lines in block(f):
#     print(lines)
#     print()
# import time
#
#
# def color(func):
#     def www():
#         b=time.time()
#         func()
#         c=time.time()
#         print(c-b)
#     return www
#
# # @color
# # def fun():
# #     time.sleep(2)
#
#
# @color
# def fun1():
#     time.sleep(3)
#
#
#
# #fun()
# fun1()

# import hashlib
#
# f=open('/tmp/passwd','rb')
# m=hashlib.md5()
# data=f.read(4096)
# while 1:
#     if data:
#         m.update(data)
#     else:
#         break
#
# x=m.hexdigest()
# print(x)

# import tarfile
# tar=tarfile.open('/tmp/passwd.tar.gz','w:gz')
# tar.add('/tmp/passwd')
# tar.close()



# class Other:
#     def __init__(self,phone,email):
#         self.phone=phone
#         self.email=email
#     def call(self):
#         print('tel: %s' % self.phone)
#
# class Hotel:
#     def __init__(self, price, cutoff,phone,email):
#         self.price =price
#         self.phone=phone
#         self.cutoff = cutoff
#         self.email=email
#         self.other=Other(phone,email)
#     def pay(self,days=1):
#         return (self.price*self.cutoff)*days
#
#
#     @classmethod
#     def haha(cls,var):
#         return var;
#
#     @staticmethod
#     def haha1(var):
#         return var;
#
#     def __str__(self):
#         return 'price: %s' % self.phone
#     def __call__(self):
#         print('price: %s' % self.phone)
#
# class NewHotel(Hotel):
#     def __init__(self,price, cutoff,phone,email,date):
#         super(NewHotel, self).__init__(price, cutoff,phone,email)
#         self.date=date
#     def mail(self):
#         print('email: %s' % self.email)
#     def showdate(self):
#         print('date: %s' % self.date)
#     def foo(self):
#         print('New hotel')
#
# class A:
#     def foo(self):
#         print('is A')
# class B(NewHotel,A):
#     pass
#
# if __name__ == '__main__':
#     tidy = Hotel(150,0.9,'12334','123@163.com')
#     tidy.price=200
#     tidy.cutoff=1
#     print(tidy.pay())
#     print(tidy.pay(2))
#     tidy1=Hotel(150,1,'1388888888','rzl@163.com')
#     tidy1.other.call()
#     tidy2 = NewHotel(150, 1, '1388888888', 'rzl@163.com')
#     tidy2.mail()
#     tidy3 = NewHotel(150, 1, '1388888888', 'rzl@163.com','2017-1-1')
#     tidy3.showdate()
#     tidy4 = B(150, 1, '1388888888', 'rzl@163.com', '2017-1-1')
#     tidy4.mail()
#     tidy4.foo()
#     var=Hotel.haha1('司马光')
#     print(var)
#     print(tidy)
#     tidy()



# class type_switch:
#     def __init__(self,file):
#         self.file=file
#
#     def switch_linux(self):
#
#         with open(self.file,'r') as f:
#             with open(self.file+'.windows.txt','w') as d:
#                 #while f.read():
#                     tmp=str( f.read()).replace('\n','\r\n')
#                     d.write(tmp)
#
#     def switch_li(self):
#
#         with open(self.file,'r') as f:
#             with open(self.file+'.null.txt','w') as d:
#                 #while f.read():
#                     tmp=str( f.read()).replace('\n','')
#                     d.write(tmp)
#
# switch = type_switch('/tmp/passwd')
# switch.switch_linux()
# switch.switch_li()


# import re
# m=re.sub('xxx','backup','/tmp/xxx/1.txt')
# print(m)

# import re
# import collections
#
# def count_patt(fname,patt):
#     cpatt=re.compile(patt)
#     result=collections.Counter()
#     with open(fname) as fobj:
#         for line in fobj:
#             m=cpatt.search(line)
#             if m:
#                 key=m.group()
#                 result[key]=result.get(key,0)+1
#     return result
#
# if __name__ == '__main__':
#     fname='/var/log/xferlog'
#     ip=''


# import socket
# from time import strftime
#
# host=''
# port=12345
# addr=(host,port)
# s=socket.socket(type=socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.bind(addr)
# #s.listen(1)
# while 1:
#     # cli_sock,cli_addr=s.accept()
#     # print('Client connect from :',cli_addr)
#     # while 1:
#         data,cliaddr=s.recvfrom(1024)
#         # if data.strip()==b'end':
#         #     break
#         clock=strftime('%H:%M:%S')
#         #data=b'rzl:  '+data
#         print(data.decode('utf8'))
#         data='[%s] %s' % (clock, data)
#         s.sendto(data.encode('utf8'),cliaddr)
#    # cli_sock.close()
# s.close()


# import re
# m=re.match('foo','food')
# print(m.group())
#
# m=re.search('foo','food')
# print(m.group())
#
# m=re.findall('foo','food')
# print(m)
#
# m=re.finditer('foo','food')
# for i in m:
#     print(i.group())
#
# pat=re.compile('foo')
# m=pat.match('food')
# print(m.group())

# import re
# mylist=re.split('\.| |-','hello-way- fd.ff')
# print(mylist)
# m=re.sub('xxx','YYY','xxxDSAF')
# print(m)

# with open('/tmp/passwd','rb') as f:
#     for i in f:
#         print(i)

# import time
# dir_time='backup-'+time.strftime('%Y-%m-%d %X', time.localtime())
# print(dir_time)


# import re
#
# def count(filename,part):
#     cpart=re.compile(part)
#     result={}
#     with open(filename) as f:
#         for line in f:
#             m=cpart.search(line)
#             if m:
#                 key=m.group()
#                 result[key]=result.get(key,0)+1
#     return result
#
# if __name__ == '__main__':
#
#     filename='/var/log/xferlog'
#     ip='(\d+\.){3}\d+'
#     print(count(filename,ip))


# import tkinter
# from functools import partial
#
# def hello(word):
#     def welcome():
#
#     return welcome  # hello函数的返回值还是函数
#
# root = tkinter.Tk()
# MyBtn = partial(tkinter.Button, root, fg='white', bg='blue')
# b1 = MyBtn(text='抽奖', command=hello('China'))
# b3 = MyBtn(text='quit', command=root.quit)
# MyLa=partial(tkinter.Label,root,fg='white', bg='blue')
# l1=MyLa(text='充气娃娃')
#
#
# b1.pack()
# b3.pack()
# l1.pack()
# root.mainloop()
# import os

# class demoa:
#     def funa(self):
#         print('funa')
#
#
# class demob(demoa):
#     def funa(self):
#         print('funb')
#
#
# a=lambda x,y:x*y
# print(a(2,3))
# b=demoa()
# b.funa()
#
# import random
# import pickle
#
# def add(word):
#     with open('/tmp/word', 'rb') as f:
#         try:
#             old=pickle.load(f)
#         except EOFError:
#             old=[]
#         if word not in old:
#             old.append(word)
#             with open('/tmp/word', 'wb') as d:
#                 pickle.dump(old,d)
#             print('已添加：%s!' % word)
#         else:
#             print('品类已经存在,无需再次添加！\n')
#
# def red():
#     try:
#         with open('/tmp/word', 'rb') as d:
#             old = pickle.load(d)
#             return old
#     except EOFError:
#         return None
#
# def rans(num):
#     old = red()
#     all=len(old)
#     list_ran=[]
#     for i in range(num):
#         tmp=random.randrange(all)
#         list_ran.append(old[tmp])
#         old.pop(tmp)
#     return list_ran
#
# if __name__ == '__main__':
#     prompt = '''(0): 自动生成菜单
# (1): 添加新项
# (2): 查看都有什么
# (3): 退出
# 请选择你的操作：
# '''
#     while 1:
#         input_op = input(prompt)
#         if input_op=='3':
#             print('再见！')
#             exit()
#         if input_op=='0':
#             list_all=red()
#             if list_all:
#                 num1=input('请输入品类数量：\n')
#                 if num1.isdigit():
#                     num=int(num1)
#                     list_ran=rans(num)
#                     print('吼吼,换换新口味：')
#                     print(list_ran)
#                     print()
#                 else:
#                     print('输入有误,请重新输入！\n')
#                     continue
#
#             else:
#                 print('品种为空,请先添加选择项!\n')
#                 continue
#
#         if input_op == '1':
#             word = input('请输入新品类名称：\n')
#             add(word)
#
#             print()
#             continue
#
#         if input_op == '2':
#             listall=red()
#             print('所有的品种参上：')
#             print(listall)
#             print()
#         if input_op not in {'0','1','2','3'}:
#             print('选择项不正确,请重新输入！\n')
#             continue
#
# list1=[]
# list1.insert(0,'3')
# list1.insert(0,'333')
# list1.remove('3')
# print(list1)


# import re
# pat=re.compile('.*x.*')
# m=pat.match('aaaxxxsssccc')
# print(m.group())


# import subprocess
# import threading
# import os
# def ping(host):
#     rc=subprocess.call('ping -c2 %s &> /dev/null' % host,shell=True)
#     if rc:
#         print('%s:down' % host)
#     else:
#         print('%s:up' % host)
#
# if __name__ == '__main__':
#     ip=['176.121.207.%s' % i for i in range(1,255)]
#     for i in ip:
#         t=threading.Thread(target=ping,args=(i,))
#         t.start()

# import os
# import time
#
# pid=os.fork()
# if pid:
#     print('parent sleep...')
#     time.sleep(600)
#     print('parent done')
#
# else:
#     print('child sleep...')
#     time.sleep(10)
#     print('child done')
# import os
# import threading
# import time
# class Sum:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def __call__(self):
#         sum=0
#         for i in range(self.a,self.b+1):
#             sum+=i
#         print(sum)
# b=time.time()
# for i in range(3):
#     x='t'+str(i)
#     x=threading.Thread(target=Sum(1,10000000))
#     x.start()
#     # t2=threading.Thread(target=Sum(10000000,20000000))
#     # t2.start()
#     # t3=threading.Thread(target=Sum(20000000,30000000))
#     # t3.start()
#     # t4=threading.Thread(target=Sum(30000000,40000000))
#     # t4.start()
#     # t5=threading.Thread(target=sum,args=(20000000,50000000))
#     # t5.start()
# x.join()
#     # t2.join()
#     # t3.join()
#     # t4.join()
# # t5.join()
# a=time.time()
# print(a-b)

# c=time.time()
# sum(1,50000000)
# d=time.time()
# print(d-c)


# import socket
# from time import strftime
#
# host=''
# port=12345
# addr=(host,port)
# s=socket.socket(type=socket.SOCK_DGRAM)
# s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
# s.bind(addr)
# #s.listen(1)
# while 1:
#     # cli_sock,cli_addr=s.accept()
#     # print('Client connect from :',cli_addr)
#     # while 1:
#         data,cliaddr=s.recvfrom(1024)
#         # if data.strip()==b'end':
#         #     break
#         clock=strftime('%H:%M:%S')
#         #data=b'rzl:  '+data
#         print(data.decode('utf8'))
#         data='[%s] %s' % (clock, data)
#         s.sendto(data.encode('utf8'),cliaddr)
#    # cli_sock.close()
# s.close()

# import socket
# from time import strftime
# import threading
#
# class TcpTimeServer:
#     def __init__(self, host='', port=12345):
#         self.addr = (host, port)
#         self.serv = socket.socket()
#         self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#         self.serv.bind(self.addr)
#         self.serv.listen(1)
#
#     def chat(self, c_sock):
#         while True:
#             data = c_sock.recv(1024)
#             if data.strip() == b'quit':
#                 break
#             data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode('utf8'))
#             c_sock.send(data.encode('utf8'))
#         c_sock.close()
#
#     def mainloop(self):
#         while True:
#             cli_sock, cli_addr = self.serv.accept()
#             t=threading.Thread(target=self.chat,args=(cli_sock,))
#             t.start()
#
#         self.serv.close()
#
# if __name__ == '__main__':
#     s = TcpTimeServer()
#     s.mainloop()


# list1=['192.168.4.%s' % i for i in range(1,255)  ]
# print(list1)


# import os
# import subprocess
# import threading
# def ping(i):
#     #for i in list1:
#         # pid=os.fork()
#         # if not pid:
#             rc=subprocess.call('ping -c2 %s &>/dev/null' % i ,shell=True)
#             if rc:
#                 print('%s:down' % i)
#                 #exit()
#             else:
#                 print('%s:up' % i)
#                 #exit()
#
# list1=['176.121.207.%s' % i for i in range(1,255)]
# for ip in list1:
#     t=threading.Thread(target=ping,args=(ip,))
#     t.start()

# import pymysql
#
# conn	=	pymysql.connect(host='127.0.0.1',	port=3306,	user='root',
# passwd='123456',	db='db1',	charset='utf8')
# cursor=conn.cursor()
# # sql="insert into departments(dep_id,dep_name) values(%s,%s)"
# # data=[(2,'运维部'),(3,'开发部')]
# # cursor.executemany(sql,data)
# #result=cursor.execute(sql,(1,'人事部'))
# #conn.commit()
# # sql="select * from departments"
# # cursor.execute(sql)
# # cursor.scroll(2)
# # cursor.scroll(0,mode='absolute')
# # result=cursor.fetchall()
# # for i in result:
# #     print(i)
# # sql="update departments set dep_name=%s where dep_name=%s"
# # cursor.execute(sql,('人力资源部','人事部'))
# sql='delete from departments where dep_id=%s'
# cursor.execute(sql,3)
#
# conn.commit()
# cursor.close()
# conn.close()


# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy import Column,Integer,String,ForeignKey,Date,and_,or_
# from sqlalchemy.orm	import	sessionmaker
#
# engine=create_engine('mysql+pymysql://root:123456@localhost/db3?charset=utf8',encoding='utf8',echo=True)
# Base=declarative_base()
# Session=sessionmaker(bind=engine)
#
# class Departments(Base):
#     __tablename__='departments'
#     dep_id=Column(Integer,primary_key=True)
#     dep_name=Column(String(20))
#     def __str__(self):
#         return '部门ID：%s 部门名称：%s' %(self.dep_id,self.dep_name)
#
# class Employees(Base):
#     __tablename__ = 'employees'
#     emp_id = Column(Integer, primary_key=True)
#     name = Column(String(20))
#     sex=Column(String(20))
#     dep_id=Column(Integer,ForeignKey('departments.dep_id'))
#     def __str__(self):
#         return '员工：%s' % self.name
#
# class Salary(Base):
#     __tablename__ = 'salary'
#     id = Column(Integer, primary_key=True)
#     emp_id= Column(Integer,ForeignKey('employees.emp_id'))
#     date=Column(Date)
#     basic=Column(Integer)
#     awards=Column(Integer)
# class User(Base):
#     __tablename__ = 'user'
#     id=Column(Integer,primary_key=True)
#     name=Column(String(20))
#     sex=Column(String(10))


# if __name__ == '__main__':
#     Base.metadata.create_all(engine)
# import re
# from urllib.error import   HTTPError
#
# from urllib.request import urlopen
#
#
# html=urlopen('https://mirrors.aliyun.com/centos/7.5.1804/virt/x86_64/kubernetes110/')
# p=html.readlines()
# list1=[]
# for i in p:
#     x=i.decode('utf8')
#     m=re.search('kuber.*\.rpm"',x)
#     if m:
#         list1.append (('https://mirrors.aliyun.com/centos/7.5.1804/virt/x86_64/kubernetes110/'+m.group()).strip('"') )
#
# for i in list1:
#     try:
#         html=urlopen(i)
#         with open('/tmp/images/'+i.split('/')[-1],'wb')as w:
#             data=html.read()
#             w.write(data)
#     except HTTPError as e:
#         if e.code==404:
#
#          print('页面被狗叼走了！！！')


# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
# from getpass import getpass
# mail_host='smtp.163.com'
# mail_user='raozhile@163.com'
# mail_pwd=getpass()
# message=MIMEText('python 邮件测试\n','plain','utf8')
# message['From']=Header('raozhile@163.com','utf8')
# message['To']=Header('raozhile@163.com','utf8')
# message['Subject']=Header('mail test','utf8')
#
# sender='raozhile@163.com'
# receivers=['754082556@qq.com']
# smtp_obj=smtplib.SMTP()
# smtp_obj.connect(mail_host)
# smtp_obj.login(mail_user,mail_pwd)
# smtp_obj.sendmail(sender,receivers,message.as_string())


# from urllib.request import urlopen
# import json
# html=urlopen('http://www.weather.com.cn/data/sk/101010100.html')
# data=html.read()
# a=json.loads(data)
# print(a)
# print(a['weatherinfo']['temp'])

# import requests
# import re
# r=requests.get('http://www.weather.com.cn/data/sk/101010100.html')
# r.encoding='utf8'
# text=r.json()
#
# # results=re.findall('[\u4e00-\u9fa5]',text)
# # res=''.join(results)
# print(text['weatherinfo']['temp'])

# import requests
# import json
# url='http://127.0.0.1/api_jsonrpc.php'
# headers={'Content-Type':'application/json-rpc'}
# data= {
#             "jsonrpc": "2.0",
#             "method": "host.create",
#             "params": {
# 	            "host":	"test_python",
# 				"interfaces":	[
# 					{	"type":	1,	"main":	1,	"useip":	1,	"ip":	"192.168.4.1",	"dns":	"",
#                 "port":	"10050"	}
# 				],
# 				"groups":	[	{	"groupid":	"2"	}	],
#             },
#             "auth":'e945857d227c365fcadecbb9a92bf084',
#             "id": 1
#       }
# data=  {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }


# r=requests.post(url,headers=headers,data=json.dumps(data))
# print(r.json())


# import wget
# import requests
# import re
# url='https://image.baidu.com/search/index?tn=baiduimage&ipn=r&ct=201326592&cl=2&lm=-1&st=-1&fr=&sf=1&fmq=1526269427171_R&pv=&ic=0&nc=1&z=&se=1&showtab=0&fb=0&width=&height=&face=0&istype=2&ie=utf-8&word=%E5%A3%81%E7%BA%B8'
# r=requests.get(url)
# r.encoding='utf8'
# img_urls=re.findall('https{0,1}:[\.\w\/&=,]*\.jpg',r.text)
#
#
# for i in img_urls:
#     x=i.split('/')[-1]
#
#     wget.download(i,out='/tmp/images/'+x)


# from	email.mime.text	import	MIMEText
# from	email.header	import	Header
# message	=	MIMEText('Python	邮件发送测试...',	'plain',	'uG-8')
# message['From']	=	Header("zzg",	'utf-8')			#	发送者
# message['To']	=		Header("root",	'utf-8')								#	接收者
# subject	=	'Python	SMTP	邮件测试'
# mail_host='smtp.163.com'
# mail_user='raozhile@163.com'
# mail_pass='4221828sbsb'
# smtp_obj	=	smtplib.SMTP()
