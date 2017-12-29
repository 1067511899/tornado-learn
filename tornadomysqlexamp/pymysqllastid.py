import pymysql.cursors

#主要是为了确认一个场景：
#自增长主键，插入一条记录之后，如何立刻获取生成的id。
#基于java的实现，preparestatement是支持这个功能的。python的话，貌似mysql提供的
#官方驱动是支持的，但是非官方的各种实现不支持。
#可以通过last_insert_id()来获取。但是并发情况下如何就不确认了，尤其是协程情况下。

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='test',
                             password='',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        sql = "select last_insert_id()"
        cursor.execute(sql)
        result=cursor.fetchone()
        print(result)
        

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

#     with connection.cursor() as cursor:
# #         # Read a single record
# #         sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
# #         cursor.execute(sql, ('webmaster@python.org',))
# #         result = cursor.fetchone()
#         sql = "select last_insert_id()"
#         cursor.execute(sql)
#         result=cursor.fetchone()
#         print(result)
finally:
    connection.close()
