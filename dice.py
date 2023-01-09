import random as rd
import time as time

ideal = [1,2,3,4,5,6]
noni = ideal

print("enter the number which you want such that it has 50% chance to come in dice (or enter 0): \n")
a = int(input())

while True:
    if a==0:
        print(rd.choice(ideal))

    elif a==1 or a==2 or a==3 or a==4 or a==5 or a==6:
        for i in range(4):
            noni.append(a)
        print(rd.choice(ideal))

    else:
        print("dhang se daal!!!")

    time.sleep(2)

