import math
import random
import time 

random_numbers = open('input.txt', 'w')

for i in range(100):
  number = random.randint(1,100)
  random_numbers.write(str(number)+ '\n')
random_numbers.close()

def factorial(n): 
    return 1 if (n==1 or n==0) else n * factorial(n - 1);  
PID=1234

with open("input.txt") as f:
  for x in f:
    PID+=1
    start_time=time.time()
    num = int(x)
    print('ProcessID:'+PID)
    print('The value of N:'+str(num))
    print('The factorial of N:'+str(factorial(num)))
    print('time taken:'+str(time.time()-start_time)+'seconds')
    print("\n")
f.close()
