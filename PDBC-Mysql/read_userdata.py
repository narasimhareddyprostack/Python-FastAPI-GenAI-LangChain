import mysql.connector
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='dbtwo'
                                  )
    cursor=dbcon.cursor()
    sql_st='''
           select *from users
            '''
    cursor.execute(sql_st)
    users=cursor.fetchall()
    for user in users:
        print(user)
except Exception as e:
    print(e)
finally:
    pass