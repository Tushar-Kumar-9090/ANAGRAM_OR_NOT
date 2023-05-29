
## WAP to check given 2 strings are anagram or not??

s1=input("Enter 1st String: ")
s2=input("Enter 2nd String: ")
if sorted(s1)==sorted(s2):
    print("String is Anagram")
else:
    print("String Is Not Anagram")



## WAP to check given 2 strings are anagram or not without using sorted() method??

s1=input("Enter 1st String: ")
s2=input("Enter 2nd String: ")
c1=0
c2=0
for i in s1:
    if i in s2:
        c1+=1
    else:
        break
else:
    for i in s2:
        c2+=1
if c1==c2:
    print("String is anagram")
else:
    print("String Not Anagram")
