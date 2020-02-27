from __future__ import print_function
import math
import random
import time 

random_numbers = open('input.txt', 'w')
PID =1232
for i in range(100):
  number = random.randint(1,100)
  random_numbers.write(str(number)+ '\n')
  
random_numbers.close()

def fib(num):
  n1, n2 = 0, 1
  count = 0
  global start_time
  start_time=time.time()
  print('\nProcess ID:',str(PID))
  if num <= 0:
    print("Please enter a positive integer")
  elif num == 1:
    print("\nFibonacci sequence upto",num,":")
    print(n1,"\n")
  else:
    print("\nFibonacci sequence of:"+str(num))
  while count <  num:
       print(n1,end=" ")
       fib_num = n1 + n2
       # update values
       n1 = n2
       n2 = fib_num
       count += 1
with open("input.txt") as f:
  for x in f:
    num = int(x)
    fib(num)
    print('\ntime taken:',str(time.time()-start_time),'seconds')