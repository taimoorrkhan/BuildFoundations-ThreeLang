
def reverseString(str):
  emptyString =""
  for i in range(len(str)-1,-1,-1):
    emptyString+= str[i]
  
  return emptyString


print(reverseString("Taimoor"))
