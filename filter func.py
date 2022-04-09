filt = [4,6,9,7,3,66,90]

def is_grt_5(x):
    return x>5
grt_5=list(filter(is_grt_5,filt))
print("numbers greater than 5",grt_5)