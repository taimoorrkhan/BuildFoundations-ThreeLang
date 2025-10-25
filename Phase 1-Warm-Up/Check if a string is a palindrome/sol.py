def Palindrome(str):
  reverseStr =""
  for i in range(len(str)-1,-1,-1):
    reverseStr+= str[i]
  if str == reverseStr:
    print("Yes its Palindrome")
  else:
    print("No its Not")
  

Palindrome("LOL")