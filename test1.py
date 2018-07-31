#-*-coding:utf-8-*-

# import socket
# host='127.0.0.1'
# port=12345
# addr=(host,port)
# c=socket.socket(type=socket.SOCK_DGRAM)
#
# #c.connect(addr)
# while 1:
#         data = input('你：')
#         c.sendto(data.encode('utf8'),addr)
#
#         if data.strip()=='end':
#             break
#         data = c.recvfrom(1024)
#         #data=b'rzl:  '+data
#         print(data[0].decode('utf8'))
#
#
# c.close()

# from test import Departments,Session,Salary,Employees,and_,or_,User
# # hr=Salary(id=2,emp_id=1,date='1990-10-10',basic=20000,awards=1000)
# # dd=Salary(id=3,emp_id=2,date='1999-10-10',basic=20000,awards=1000)
# # hr=Employees(emp_id=1,name='tom',sex='boy',dep_id=1)
# # dd=Employees(emp_id=2,name='tomm',sex='girl',dep_id=2)
# # deps=[hr,dd]
# # session=Session()
# # session.add_all(deps)
# # session.commit()
# # session.close()
# # session=Session()
# # qset=session.query(Departments.dep_name,Employees.name).join(Employees,Employees.dep_id==Departments.dep_id)
# # # for depp in qset:
# # #     print('%s' % (depp))
# # # print(qset.one())
# # print(qset.all())
#
# # record1=User(id='2',name='tomm',sex='boy')
# # record2=User(id='3',name='tommm',sex='girl')
# # record_all=[record1,record2]
# # session=Session()
# # session.add_all(record_all)
# # session.commit()
# # session.close()
# session=Session()
# # for row in session.query(User).filter(or_( User.name.like('tomm_')),User.name.like('tommm')):
# #     print(row.id,row.name,row.sex)
# # q=session.query(Employees.name,Departments.dep_name).join(Departments,Employees.dep_id==Departments.dep_id)
# # print(q.all())
#
# q1=session.query(User).get(1)
# session.delete(q1)
# session.commit()
# session.close()
# import pymysql
# name=input()
# password=input()
# db = pymysql.connect(host="localhost", user="root", password="123456", db="db1", port=3306)
# cursor = db.cursor()
# sql="select * from person  where name=%s and password=%s"
# cursor.execute(sql ,(name,password))
# result=cursor.fetchall()
#
# print(result)

# import	urllib.request
# from urllib.request import urlopen
#
# url='http://www.tedu.cn'
# header={
# 			'User-Agent':'Mozilla/5.0	(X11;	Fedora;	Linux	x86_64)	AppleWebKit/537.36	(KHTML,	like	Gecko)	Chrome/58.0.3029.110	Safari/537.36'
# }
# html=urllib.request.Request(url,headers=header)
# data=urlopen(html)

import paramiko
import getpass
import string
import threading


def remote_comm(host,pwd,command):

    ssh=paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host,
        username='root',
        password=pwd

    )
    a=ssh.exec_command(command)
    out=a[1].read()
    error=a[2].read()
    if out:
        print(out.decode('utf8'))
    if error:
        print(error.decode('utf8'))

if __name__ == '__main__':
    filename=input('filname')
    command=input('command')
    pwd=getpass.getpass()
    with open(filename) as f:
        ips=[line.strip() for line in f]
    for ip in ips:
        t=threading.Thread(target=remote_comm,args=(ip,pwd,command))
        t.start()