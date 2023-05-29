
## Leap year

year=int(input("Enter The Year: "))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f'{year} is leap year')
else:
    print(f'{year} is not leap year')



## leap year with nested

year=int(input("Enter The Year: "))
if year%100!=0:
    if year%4==0:
        print("Leap Year")
    else:
        print("Not Leap Year")
else:
    if year%400==0:
        print("Leap Year")
    else:
        print("Not Leap Year")
