import mysql.connector

try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='12pm'
                                  )
    cursor=dbcon.cursor()
    sql_st='''
            insert into employees(eid,ename,esal,age) 
            values(101,'Rahul',45000.45,52);

            '''
    cursor.execute(sql_st)
    dbcon.commit()
    print("Data inserted successfully")

except Exception as e:
    print(e)
finally:
    pass