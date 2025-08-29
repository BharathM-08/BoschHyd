def pali(s):
    return s == s[::-1]

s = input("Enter the String: ")
if(pali(s)):
    print("Palindrome")
else:
    print("Not Palindrome")