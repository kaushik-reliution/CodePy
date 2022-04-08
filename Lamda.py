# minus=lambda x, y: x-y
# print(minus(8,5))
#
# def minus(a,b):
#
#     return a-b
#
# print ("Wihtout Lambda Function:-",minus(6,2))

# def a_srt(a):
#     return a[1]

a=[[1,8],[4,2],[6,7]]
a.sort(key= lambda x: x[1]) #using lambda function

print(a)
