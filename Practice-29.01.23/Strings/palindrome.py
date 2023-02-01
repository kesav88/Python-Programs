#Python Program to Check if a Given String is Palindrome
str1="malayalam"
if str1[::] == str1[::-1]:
    print("the given string is palindrome")
else:
    print("the given string is not palindrome")