numbers=[1,2,3,4,5,6,7,8,9,10]
#       [2,3,4,5,6,7,8,9,10,11]
#       [F,T,F,T,F,T,F,T,F,T]

""" def plusone(num):
    return num+1 

lambda num:num+1
 """
map_obj=map(lambda num:num+1,numbers)
new_numbers=list(map_obj)
print(numbers)
print(new_numbers)
