#  syntax for(start,end,condition)

import time

for i in range(0,10):
    print(i+1)  #prints from 1 to 10

for i in range(0,10,2):
    print(i+1) #prints from 1 to 10 in odd series

for i in "John Doe":
    print(i) #prints each character in the string

# Wish Happy BIrthday to your friends with this program 

for i in range(10,0,-1):
    print(i)
    time.sleep(1)
print("Happy Birthday")