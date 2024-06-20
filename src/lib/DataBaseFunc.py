from src.classes.User import User,UserException
from src.classes.GameRecord import GameRecord,GameRecordException
import sqlite3
from datetime import datetime

#注册
def userInsert(user:User)->bool:#注册
    conn = sqlite3.connect("otherresource/userMess.db")#连接数据库
    cur = conn.cursor()#创建游标
    cur.execute("SELECT MAX(Uid) FROM userMess")#设置id
    max_id = cur.fetchone()[0]
    user.setUid(str(int(max_id) + 1))
    userid = user.getUid()
    username = user.getUname()#获得name
    password = user.getUpassword()#获得password
    sql = "select * from userMess where Uname=?"#判断是否存在
    cur.execute(sql,(username,))
    data = cur.fetchall()
    if len(data) == 0:
        sql = "insert into userMess(Uid,Uname,Upassword) values(?,?,?)"#插入
        cur.execute(sql,(userid,username,password))
    else:return False
    conn.commit()
    cur.close()
    conn.close()
    return True

#登录
def checkLogin(user:User)->bool:
    conn = sqlite3.connect("otherresource/userMess.db")#连接数据库
    cur = conn.cursor()#创建游标
    username = user.getUname()#获得name
    password = user.getUpassword()#获得password
    sql = "select Uname,Upassword from userMess where Uname=? and Upassword=?"
    cur.execute(sql,(username,password))
    data = cur.fetchall()
    if data:
        return True
    cur.close()
    conn.close()
    return False

#修改
def userUpdate(user:User)->bool:
    conn = sqlite3.connect("otherresource/userMess.db")#连接数据库
    cur = conn.cursor()#创建游标
    username = user.getUname()#获得name
    password = user.getUpassword()#获得password
    if username and password:
        sql = "update userMess set Upassword=? where Uname=?"
        cur.execute(sql,(password,username))
        return True
    conn.commit()
    cur.close()
    conn.close()
    return False

def addToRankingList(gameRecord:GameRecord)->list:#list:
    conn = sqlite3.connect("otherresource/record.db")#连接数据库
    cur = conn.cursor()#创建游标
    username = GameRecord.getUname()
    userid = GameRecord.getRid()
    userscore = GameRecord.getUscore()
    now = datetime.now()#获取当前日期和时间
    formatted_datetime = now.strftime('%Y-%m-%d %H:%M:%S')#格式化日期和时间
    sql = "insert into record(Rid,Uname,Uscore,Rtime) values(?,?,?,?)"
    conn.execute(sql, (userid,username,userscore,formatted_datetime,))#插入记录
    result = cur.fetchall()
    table_list = []
    for r in result:
        table_list.append(list(r))
    conn.commit() 
    cur.close()
    conn.close()#关闭数据库连接
    return list[table_list]
    

