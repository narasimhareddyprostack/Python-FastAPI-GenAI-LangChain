import mysql.connector
dbcon=None 
try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='12pm'
                                  )
    cursor=dbcon.cursor()
    sql_st='''
                create table employees(
                eid int, 
                ename varchar(32),
                esal float,
                age int
                )

            '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("New Table Created successfully")

except Exception as e:
    print(e)
finally:
    pass