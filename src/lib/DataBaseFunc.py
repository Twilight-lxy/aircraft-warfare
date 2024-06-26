from src.classes.User import User
from src.classes.GameRecord import GameRecord
import sqlite3
from datetime import datetime


# 注册
def userInsert(user: User) -> bool:  # 注册
    conn = sqlite3.connect("otherresource/userMess.db")  # 连接数据库
    cur = conn.cursor()  # 创建游标
    cur.execute("SELECT MAX(Uid) FROM userMess")  # 设置id
    max_id = cur.fetchone()[0]
    if max_id == None:
        max_id = 0
    user.setUid(str(int(max_id) + 1))
    userid = user.getUid()
    username = user.getUname()  # 获得name
    password = user.getUpassword()  # 获得password
    sql = "select * from userMess where Uname=?"  # 判断是否存在
    cur.execute(sql, (username,))
    data = cur.fetchall()
    if len(data) == 0:
        sql = "insert into userMess(Uid,Uname,Upassword) values(?,?,?)"  # 插入
        cur.execute(sql, (userid, username, password))
    else:
        return False
    conn.commit()
    cur.close()
    conn.close()
    return True


# 登录
def checkLogin(user: User) -> bool:
    conn = sqlite3.connect("otherresource/userMess.db")  # 连接数据库
    cur = conn.cursor()  # 创建游标
    username = user.getUname()  # 获得name
    password = user.getUpassword()  # 获得password
    sql = "select Uname,Upassword from userMess where Uname=? and Upassword=?"
    cur.execute(sql, (username, password))
    data = cur.fetchall()
    if data:
        return True
    cur.close()
    conn.close()
    return False


# 修改
def userUpdate(oldusername: str, user: User) -> bool:
    conn = sqlite3.connect("otherresource/userMess.db")  # 连接数据库
    cur = conn.cursor()  # 创建游标
    username = user.getUname()  # 获得name
    password = user.getUpassword()  # 获得password
    sql = "update userMess set Uname=?,Upassword=? where Uname=?"
    cur.execute(sql, (username, password, oldusername))
    data = cur.fetchall()
    if data:
        return True
    conn.commit()
    cur.close()
    conn.close()

    return True
    return False


# 添加记录
def addToRankingList(gameRecord: GameRecord):  # list:
    conn = sqlite3.connect("otherresource/record.db")  # 连接数据库
    cur = conn.cursor()  # 创建游标
    username = gameRecord.getUsername()
    cur.execute("SELECT MAX(Rid) FROM record")  # 设置id
    max_id = cur.fetchone()[0]
    if max_id == None:
        max_id = 0
    gameRecord.setUid(str(int(max_id) + 1))
    userid = gameRecord.getUid()
    userscore = gameRecord.getUscore()
    now = datetime.now()  # 获取当前日期和时间
    formatted_datetime = now.strftime("%Y-%m-%d %H:%M:%S")  # 格式化日期和时间
    sql = "insert into record(Rid,Uname,Uscore,Rtime) values(?,?,?,?)"
    conn.execute(
        sql,
        (
            userid,
            username,
            userscore,
            formatted_datetime,
        ),
    )  # 插入记录
    conn.commit()
    cur.close()
    conn.close()  # 关闭数据库连接


# 获取记录
def getRankingList() -> list:  # list:
    conn = sqlite3.connect("otherresource/record.db")  # 连接数据库
    cur = conn.cursor()  # 创建游标
    cur.execute("select * from record order by Uscore desc")
    records = cur.fetchall()
    table_list = []
    for r in records:
        record = GameRecord(r[1], r[2], r[3])
        table_list.append(record)
    cur.close()
    conn.close()  # 关闭数据库连接
    return table_list
