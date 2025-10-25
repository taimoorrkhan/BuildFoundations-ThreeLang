function Palindrome(str) {
  return str == str.split('').reverse().join('')
}

console.log(Palindrome("LOL"))