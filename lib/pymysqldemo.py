import pymysql

try:
    conn=pymysql.connect(host="localhost",port=3306,
                         user="root",password='root',
                         database="p2p",charset="utf8")
    cursor=conn.cursor()

    cursor.execute("select * from user")

    data = cursor.fetchone()

    print(data)

except Exception as e:
    print("出错了，错误信息为{}".format(e))

finally:
    if cursor:cursor.close()

    if conn:conn.close()