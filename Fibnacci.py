# check if the number of terms is valid
def fib(num):
  # first two terms
  n1, n2 = 0, 1
  count = 0
  if num <= 0:
    print("Please enter a positive integer")
  elif num == 1:
    print("Fibonacci sequence upto",num,":")
    print(n1)
  else:
    print("Fibonacci sequence:")
  while count <  num:
       print(n1)
       fib_num = n1 + n2
       # update values
       n1 = n2
       n2 = fib_num
       count += 1

number = fib(int(input("Enter the number")))