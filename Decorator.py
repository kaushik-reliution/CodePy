def dec(f1):
    def exec():
        print("Processing")
        f1()
        print("Processed")
    return exec

# @dec # using decorator
def pro():
    print("Decorator part")
pro= dec(pro)

pro()

