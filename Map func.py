# lis= ["3","5","7","4"]
# lis= list( map (int, lis)) #map function convert strings to int and return to lis
# # for i in range(len(lis)): # 1st-Way to convert string into int
# #     lis[i] = int( lis[i] )#  Its to complicated lets do something new(map)
# lis[2]= lis[2] + 1
# print(lis[2])

# #Lets do square using map fucntion
# numb=[5,3,2,7,8,6,9]
# sqaure = list(map(lambda x:x*x, numb))
# print("Square of Nums:- ",sqaure)

#square and cube using map function

def s(x):
    return x * x
def c(x):
    return x*x*x
fun = [s,c]
for i in range(4):
    val = list(map(lambda a:a(i), fun))
    print("Square", val,"Cube")
