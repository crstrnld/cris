# Assignment 1

a=int(input("(a): "))
b=int(input(" (b): "))
c=int(input("(c): "))

# Check if the conditions are met
if (a>b or b>c) and (a%2==0 and c%2!=0) and (b!=c):
    print("Conditions met")
else:
    print("Conditions not met")