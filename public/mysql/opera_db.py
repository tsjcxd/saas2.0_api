import pymysql
from sshtunnel import SSHTunnelForwarder

KEY_FILE = r"C:\\Users\\EDZ\\.ssh\\id_rsa"


tbj = SSHTunnelForwarder(
    ('101.132.119.70', 22),
    ssh_username="tangsaijuan",
    ssh_pkey=KEY_FILE,
    remote_bind_address=("rm-uf61485wcg7578wl3.mysql.rds.aliyuncs.com", 3306),
)
tbj.start()
conn = pymysql.connect(
    host='127.0.0.1',
    port=tbj.local_bind_port,
    user="tangsaijuan",
    password="UT9rCy05R0Vd"
)
cur = conn.cursor()
cur.execute("show databases;")
data = cur.fetchall()
cur.close()
tbj.stop()