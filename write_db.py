"""
write_db.py 写数据库
insert  update  delete
"""

import pymysql

#  链接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')

# 生成游标对象 (用于操作数据库数据，获取sql执行结果的对象)
cur = db.cursor()

# 对数据库执行写操作
try:
    # insert插入
    # sql = "insert into cls1 (name,age,score) \
    # values ('Dave',16,92);"

    # name = input("Name:")
    # age = input("Age:")
    # score = input("Score:")
    # 合成sql语句要顾虑整体的格式，保证sql正确
    # sql = "insert into cls1 (name,age,score) \
    # values ('%s',%s,%s);"%(name,age,score)

    # 使用execute给sql传递参量
    # sql = "insert into cls1 (name,age,score) \
    #     values (%s,%s,%s);"
    # cur.execute(sql,[name,age,score]) # 不要传递表名，字段名，关键字

    # # update 操作
    # sql = "update cls1 set sex='m' where name='Bill';"
    # cur.execute(sql)
    # # delete 删除
    # sql = "delete from cls1 where sex is null;"
    # cur.execute(sql)

    # 同时执行多次sql语句
    exe = []
    for i in range(3):
        name = input("Name:")
        age = input("Age:")
        score = input("Score:")
        exe.append((name,age,score))
    sql = "insert into cls1 (name,age,score) values (%s,%s,%s)"
    cur.executemany(sql,exe)

    db.commit()  # 同步写操作结果
except Exception as e:
    print(e)
    db.rollback() # 出错时将数据库恢复到之前状态

# 关闭数据库和游标
cur.close()
db.close()









