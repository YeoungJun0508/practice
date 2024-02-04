import random

lotto_num = [] 
count = 0;

def GetRandomNum():
    number = random.randint(1,45)
    return number

while True:
    random_number = GetRandomNum()
    if random_number not in lotto_num:
        lotto_num.append(random_number)
        count+=1

    if count>5:
        break

print(lotto_num)

