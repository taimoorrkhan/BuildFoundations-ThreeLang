def sum_array(arr):
  sum = 0
  for i in range(0,len(arr)):
    sum+= arr[i]
  
  return sum

print(sum_array([1,2,4,5]))