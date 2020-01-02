import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pymysql
from sshtunnel import SSHTunnelForwarder
import pymysql.cursors
from pymysql.cursors import DictCursor



class ExecuteSQL:
    """
    连接数据库的封装
    """
    def __init__(self,dbname):
        self.dbname = dbname
        self.tbj = SSHTunnelForwarder(
        ('101.132.119.70', 22), # 这里的IP地址是在连接信息里显示的SSH主机名或IP地址
        ssh_username="tangsaijuan", # 这里是运维给你的用户名，而不是数据库的用户名
        ssh_pkey=r"C:\\Users\\EDZ\\.ssh\\id_rsa", # 这里是运维给你的公钥文件存放地址
        remote_bind_address=('rm-uf61485wcg7578wl3.mysql.rds.aliyuncs.com', 3306))
        self.tbj.start()
        self.conn = pymysql.connect(
        cursorclass=DictCursor,
        host='127.0.0.1',
        port=self.tbj.local_bind_port,
        user='tangsaijuan',
        passwd='UT9rCy05R0Vd',
        db=dbname
        )


    """
    数据库执行的封装
    """
    def get_singledata(self,sql):
        results = ''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            results = cur.fetone()
        except Exception as data:
            print('Error: 执行查询失败，%s' % data)
        finally:
            self.conn.close()
        return results
        
    def get_alldata(self,sql):
        results = ''
        cur = self.conn.cursor()
        try:
            cur.execute(sql)
            results = cur.fetall()
        except Exception as data:
            print('Error: 执行查询失败，%s' % data)
        finally:
            self.conn.close()
        return results



if __name__ == "__main__":
    name = 'saas_test'
    sql = "SELECT * FROM `app_setting` where setting_type=4 and setting_name='金牌教练' and is_del=0 and brand_id=176221133013056;"
    connect = ExecuteSQL(name)
    result = connect.excute_sql(sql)
    print(result)
    
    
        
