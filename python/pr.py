num= int(input("Enter number :: "))
if num > 1 :
    for i in range(2,int(num/2+1)):
        if num % i == 0:
            print(num,"not prime number")
            break
        else:
            print(num,"prirme")
else:
    print(num," get valid input")