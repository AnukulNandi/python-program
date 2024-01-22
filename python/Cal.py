#check big of two number
#print("Enter your name")
name=input("Enter your name")

print("Enter  two number")
a=int(input())

b=int(input())

if(a>b):
    print("a is big" , a)
    
    print("after  some operation " , name , "your result is :: ")
    
    sum = a + b
    print("ADDITION IS :: %d" %sum)

    mul = a * b
    print("MULTIPLICATION IS :: %d" %mul)

    sub = a - b
    print("SUBTRACTION IS :: %d" %sub)

    div = a / b
    print("DIVITION IS :: %.2f" %div)
    
else:
    print("b is big " , b)
    print("aftter  some operation " , name , "your result is :: ")
    
    sum = b + a
    print("ADDITION IS :: %d" %sum)

    mul = b * a
    print("MULTIPLICATION IS :: %d" %mul)

    sub = b - a
    print("SUBTRACTION IS :: %d" %sub)

    div = b / a
    print("DIVITION IS :: %.2f" %div)
