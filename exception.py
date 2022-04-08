# try:
#     filexp = open("file123","r")
#     filexp.write("File is accesible")
# except IOError:
#     print("Error: Cant find file or u r using wrong parameter")
# else:
#     print("Written successfully")
#     filexp.close()

# try:
#    fh = open("testfile", "w")
#    try:
#       fh.write("This is my test file for exception handling!!")
#    finally:
#       print ("Going to close the file")
#       fh.close()
# except IOError:
#    print ("Error: can\'t find file or read data")

def temp(var):
   try:
      return int(var)
   except ValueError as Argument:
      print("This argument does not contain numbers \n ",Argument)

a=input("Enter value  ")
h=temp(a)
print("This is ",h)










