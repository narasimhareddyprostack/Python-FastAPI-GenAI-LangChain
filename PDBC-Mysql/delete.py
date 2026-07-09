import mysql.connector

try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='dbtwo'
                                  )
    cursor=dbcon.cursor()
    sql_st='''
            delete from users
            where user_id=6;

            '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data Deleted  successfully")

except Exception as e:
    print(e)
finally:
    pass