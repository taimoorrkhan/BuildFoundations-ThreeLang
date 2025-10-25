using System;

//string are immutable 

class Program
{
  public static string reverseString(string str)
  {
    if (str == null) return null;
    char[] arr = str.ToCharArray();
    Array.Reverse(arr);
    return new string(arr);

  }

  static void Main(string[] args)
  {
    reverseString("Taimoor");
  }

}

