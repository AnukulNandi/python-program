a=int(input("Enter a number"))
r=0
s=[]
while a!=0 :
    r=a%2
    s.append(r)
    a=a//2
print("Bimary number")
for i in s:
    print(i,end='')
