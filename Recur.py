def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac=fac*(i+1)
    return fac

def factorial_recursive(n): #when the value = 5 it jumps to else block and run a logic.
    fac = 1
    if n==1:
        return 0 # return 1 because the value return 0 the whole fact becomes 0
    else:
        return n * factorial_recursive(n-1) # Recursive logic
number=int(input("Enter number"))
print("Facotiral is ",factorial_iterative(number))
print("Facotiral using recursive ",factorial_recursive(number))