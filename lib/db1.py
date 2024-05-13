import sys
import logging
import pymysql
from config import *
sys.path.append('..')
def conn():
    conn =pymysql.connect(
        host="localhost",user="root",
        password="root",db="p2p",
        port=3306,charset="utf8"
    )
    return conn
def query_db(sql):
    con=conn()
    cur=con.cursor()
    #在日志中打印sql语句
    logging.debug(sql)
    cur.execute(sql)
    result=cur.fetchall()
    logging.debug(result)
    return result
def change_db(sql):
    con=conn()
    cur=con.cursor()
    try:
        cur.execute(sql)
        con.commit()
    except Exception as e:
        logging.error(str(e))
        con.rollback()
    finally:
        cur.close()
#封装常用的数据库操作
#查询
def check_user(name):
    sql="select * from t_user where user_name = {}".format(name)
    result=query_db(sql)
    return True if result else False
#添加
def add_user(name,passwoed):
    sql="insert into t_user(user_name,password) values ('{}','{}')".format(name)
    change_db(sql)
#删除
def del_user(name):
    sql="delete from t_user where user_name='{}'".format(name)
    change_db(sql)