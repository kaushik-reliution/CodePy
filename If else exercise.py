#WAP to check whether age is greater than 18 you can drive.

print("Enter your age")
age = int(input())
if age<7 or age>100:
    print("Not a logical age")
if age>18 and age<100:
    print("you can drive")
elif age==18:
    print("We will think ")
else:
    print("You cant drive")




