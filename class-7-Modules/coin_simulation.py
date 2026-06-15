import random
coin_result=['Head','Tail']
head_count=0
tail_count=0
for x in range(10):
    result=random.choice(coin_result)
    if result =="Head":
        head_count=head_count+1
    elif result=="Tail":
        tail_count=tail_count+1


print("No of Heads:", head_count)
print("No of Tail:", tail_count)