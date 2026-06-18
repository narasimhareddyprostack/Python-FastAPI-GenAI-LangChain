import json 
emp_json_str='''
            {"eid": 101, "ename": "Rahul", "esal": 45000, "avail": true, "dicscount": null}
            '''

emp=json.loads(emp_json_str)
print(emp)