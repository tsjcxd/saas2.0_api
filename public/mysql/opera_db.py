import pymysql
from sshtunnel import SSHTunnelForwarder

KEY_FILE = "C:\\Users\\EDZ\\.ssh\\id_dsa"

# with open(KEY_FILE, 'r') as f:
#     text = f.read()
# print(text)


ts = SSHTunnelForwarder(
    ('101.132.119.70', 22),
    ssh_username="tangsaijuan",
    ssh_pkey=KEY_FILE,
    remote_bind_address=("rm-uf61485wcg7578wl3.mysql.rds.aliyuncs.com", 3306),
)
ts.start()
conn = pymysql.connect(
    host='127.0.0.1',
    port=ts.local_bind_port,
    user="tangsaijuan",
    password="UT9rCy05R0Vd",
    database="saas_test"
)
cur = conn.cursor()
cur.execute("SELECT * FROM `shop` LIMIT 1")
data = cur.fetchall()
cur.close()
ts.stop()