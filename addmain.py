def str1(string):
    return f"This is the wrong addition {string}"

def add(num1, num2):
    return num1 + num2 + 5

print("coming from source is: ",__name__)
if __name__ == '__main__':
    print(str1("See below:-"))
    plus = add(5, 6)
    print(plus)



