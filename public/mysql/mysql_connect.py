import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pymysql
from sshtunnel import SSHTunnelForwarder
import pymysql.cursors


class ExecuteSQL():
    def __init__(self,dbname,sql):
        self.dbname = dbname
        self.sql = sql
        self.tbj = SSHTunnelForwarder(
        ('101.132.119.70', 22), # 这里的IP地址是在连接信息里显示的SSH主机名或IP地址
        ssh_username="tangsaijuan", # 这里是运维给你的用户名，而不是数据库的用户名
        ssh_pkey=r"C:\\Users\\EDZ\\.ssh\\id_rsa", # 这里是运维给你的公钥文件存放地址
        remote_bind_address=('rm-uf61485wcg7578wl3.mysql.rds.aliyuncs.com', 3306))
        self.tbj.start()
        self.conn = pymysql.connect(
        host='127.0.0.1',
        port=self.tbj.local_bind_port,
        user='tangsaijuan',
        passwd='UT9rCy05R0Vd',
        db=dbname
        )

    def excute_sql(self):
        results = ''
        cur = self.conn.cursor()
        try:
            cur.execute(self.sql)
            results = cur.fetchall()
        except Exception as data:
            print('Error: 执行查询失败，%s' % data)
        finally:
            self.conn.close()
        return results
        


if __name__ == "__main__":
    name = 'saas_test'
    sql = "SELECT * FROM `shop` where shop_name='汤汤Autotest';"
    connect = ExecuteSQL(name, sql)
    print(connect.excute_sql())
    
    
        
