def generate_fibonacci(n):
  first_n = 0
  second_n = 1
  fibonacci_sequence = []
  for i in range(n):
    next = first_n + second_n
    fibonacci_sequence.append(first_n)
    first_n = second_n
    second_n = next
    
  return fibonacci_sequence
  
print(generate_fibonacci(6))