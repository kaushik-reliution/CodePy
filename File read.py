#using block to open file
with open("Writ.txt") as f:
    a = f.read(4)
    print("Using Block:- ", a)


# fil = open("Writ.txt","rt")
# # print(fil.readline())
# # fil.seek(19)
# print(fil.readlines()) #print line by line
# # content = fil.read()# print whole paragraph
# # for line in fil:
# #     print(line, end="")
# fil.close()

# fil = open("Writ.txt","a")
# fil.write("Ancient Temple Kandariya Mahadev\n")
# fil.close()
#Handle read and Write
# f=open("Writ.txt", "r+")
# print(f.read())
# f.write("Located in Madhya Pradesh")

#file seek(), tell()

f=open("Writ.txt")
# print(f.tell())
print(f.readline())
f.seek(5)
print(f.tell())

print(f.readline())
# print(f.tell())
f.close()