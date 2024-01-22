temp=int(input("Enter any ineger number"))
n=temp
su=0

while temp > 0 :
    remin=temp%10
    fact=1
    i=1
    
    for i in range(1,remin + 1) :
        fact = fact * i
        i=i+1
    print("%d factorial is %d" %(remin,fact))
    su = su + fact
    temp = temp // 10

if(n == su):
    print("sum of factorial is %d so is a strong number" % (su))
  
else:
    print("sum of factorial is %d so it not a strong number " % (su))
   
