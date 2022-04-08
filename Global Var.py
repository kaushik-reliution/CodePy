gl=10 #global
def func1(n):
        global gl
        gl = gl + 20
        g = 10 #local
        print(gl,g)
        print(n,"I have a value")
func1("hello")
#print("This is global",gl)
x=10 #x change 10 to 25
# def func1():
#     x=30
#     def func2():
#         global x #global
#         x= 25
#     # print("Before calling Func2",x)
#     func2()
#     print("After calling Func2",x)
# func1()
# print("After overwrite X var",x)
