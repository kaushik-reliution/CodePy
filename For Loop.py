# num=int(input("Enter number"))
# for i in range(num, 0, -1):
#     for j in range(0, i):
#         print(i, end="")
#     print("\n ")


num=int(input("Enter number"))
for i in range(num):
    for j in range(0,num-i):
        print(j+1, end="")
    print("\n")



