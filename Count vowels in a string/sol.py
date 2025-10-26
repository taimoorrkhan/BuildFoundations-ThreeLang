def VowelsInString(str):
  vowels=["a","e","i","o","u"]
  result=[]
  for i in range(0,len(str)):
    if str[i] in vowels:
      result.append(str[i])
    
  return result

print(VowelsInString("Taimoor"))