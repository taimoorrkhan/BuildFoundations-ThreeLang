def factorial_iterative(n):
  result = 1
  for i in range(1,n+1):
    result *= i
  return result

print(factorial_iterative(5))

""" While Loop Approach """

result = 1
num = 5
while num > 0:
  result *= num
  num -= 1

print(result)

def factorial_recursive(n):
  if n==0 or n==1:
    return 1
  else:
    n = n * factorial_recursive(n-1)
  return n

print(factorial_recursive(5))