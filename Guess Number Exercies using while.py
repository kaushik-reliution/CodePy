#WAP to guess the number and show result to the user whether right or wrong.

n=20
guess=1
print("Number of guessing limit is 7 times only \n")
while(guess<=7):
    guess_num=int(input("Guess the number \n"))
    if(guess_num<20):
        print("Jumped to the lowest\n")
    elif(guess_num>20):
        print("Dont jump to high\n")
    else:
        print("Guess done")
        print(guess,"no of guesses is fininshed")
        break
    print(7-guess,"no of guesses left \n")
    guess = guess + 1
if(guess_num>7):
    print("you lost")




