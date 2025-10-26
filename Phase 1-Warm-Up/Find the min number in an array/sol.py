def minNumber(arr):
  min=arr[0]
  for i in range(0,len(arr)):
    if arr[i] < min:
      min = arr[i]

  return min

print(minNumber([3,55,6,2,111]))