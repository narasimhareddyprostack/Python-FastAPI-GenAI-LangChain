import mysql.connector

try:
    dbcon=mysql.connector.connect(host='localhost',
                                  user='root',
                                  password='root',
                                  database='12pm'
                                  )
    cursor=dbcon.cursor()
    sql_st='''
           select *from employees
            '''
    cursor.execute(sql_st)
    employees=cursor.fetchall()
    for emp in employees:
        print(emp)
    
    #print("Data inserted successfully")

except Exception as e:
    print(e)
finally:
    pass