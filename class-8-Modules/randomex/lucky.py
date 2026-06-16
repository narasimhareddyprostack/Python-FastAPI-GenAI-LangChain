from random import choice,choices

enames=["Darshini","Naveen","Sai","Shive","AD","Vikas","RG","SG","Priya"]

luck_ename=choice(enames)
print(luck_ename)

luck_draw_List=choices(enames,k=3)
luck_draw_List=choices(enames,3)
print(luck_draw_List)