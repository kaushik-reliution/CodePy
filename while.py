#WAP to take inputs from user and check number is greater than 100 or not if no then continue loop.
while(True):
    inp=int(input("Enter number"))
    if inp>100:
        print("U entered number greater than 100")
        break
    else:
        print("Try again")
        continue

