using System;

//string are immutable 

class Program
{
  public static bool Palindrome(string str)
  {
    if (str == null) return null;
    char[] arr = str.ToCharArray();
    Array.Reverse(arr);
    string reverseString = new string(arr);
    return str == reverseString;

  }

  static void Main(string[] args)
  {
    Console.WriteLine(Palindrome("Taimoor"));
  }

}

