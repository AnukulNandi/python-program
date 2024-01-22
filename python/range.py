num=int(input("Enter number to  starting a table"))
num1=int(input("Enter number to ending a table"))
if num>0 and num1>1:
    if num1 > num:
        for i in range(num,num1+1):
            print("the table of",i," is ::")
            for j in range(0,11):
                ad = i*j
                print(i,"*",j,"=",ad)
    else:
        print("Give the input always \n first number < second number")
else:
    print("Give valid input...  ")
