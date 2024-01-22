a = int(input("Enter 1st number"))
b = int(input("Enter 1st number"))
hcf = 1
for i in range(2,a+1):
    if a % i==0 and b % i==0 :
        hcf = i
        print("%d and %d hcf is %d" %(a,b,hcf))
        break
lcm = int((a*b)//hcf)
print("%d and %d lcm is %d" %(a,b,lcm))
        
