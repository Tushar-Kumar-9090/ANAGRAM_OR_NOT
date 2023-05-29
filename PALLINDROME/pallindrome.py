
## WAP to find given string is pallindrome or not

s=input("Enter The String: ")
if s==s[::-1]:
    print("String is Pallindrome")
else:
    print("String is Not Pallindrome")




## Find given string is pallindrome or not without using built-in method

s=input("Enter a string ")
k=''
for i in range(-1,-(len(s)+1),-1):
    k+=s[i]
if k==s:
    print("pallindrome")
else:
    print("not pallindrome")
