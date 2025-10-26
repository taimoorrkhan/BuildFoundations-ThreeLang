def maxNumber(arr):
  max=0
  for i in range(0,len(arr)):
    if arr[i] > max:
      max = arr[i]

  return max

print(maxNumber([1,3,55,6,2,111]))