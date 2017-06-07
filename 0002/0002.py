import pymysql.cursors
# 连接数据库
connect = pymysql.Connect(
    user='root',
    passwd='1234',
    db='activ_code',
    charset='utf8'
)
# 获取游标
cursor = connect.cursor()
f = open('activation_code.txt', 'r')
# 逐行读取
for code in f.readlines():
    #插入数据
    sql = "INSERT INTO activ_code (code) VALUES ( '%s')"
    data = code
    cursor.execute(sql % data)
    connect.commit()
cursor.close()
connect.close()