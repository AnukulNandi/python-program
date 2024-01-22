print("Enter number for print table")
x = int (input())
i = 1
mul = 1

if x <= 0:
    print("Alwayes result should be 0 or nagetive ")
else:
    while i <= 10 :
        mul = x * i
        print(x , "*" , i , "=" , mul)
        i = i + 1
