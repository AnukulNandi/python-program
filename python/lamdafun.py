x=lambda a : a*10
print(x(5))
# in function
def myfunction(n):
    return lambda a:a/n
mydoubler = myfunction(2)
print(mydoubler(10))