import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pymysql
from sshtunnel import SSHTunnelForwarder
# import pymysql.cursors
 
with SSHTunnelForwarder(
        ('101.132.119.70', 22), # 这里的IP地址是在连接信息里显示的SSH主机名或IP地址
        ssh_username="tangsaijuan", # 这里是运维给你的用户名，而不是数据库的用户名
        ssh_pkey=r"C:\Users\EDZ\.ssh\id_dsa", # 这里是运维给你的公钥文件存放地址
        remote_bind_address=('rm-uf61485wcg7578wl3.mysql.rds.aliyuncs.com', 3306)) as server:
    conn = pymysql.connect(
        host='127.0.0.1',
        port=server.local_bind_port,
        user='tangsaijuan',
        passwd='UT9rCy05R0Vd',
        db='saas_test')
    # cur = conn.cursor()
    # cur.execute("show databases")
    # print(cur.fetchall())

    
