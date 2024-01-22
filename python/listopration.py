#list operation
a = ['Anukul',12,'tapan',34,10]
print(a)
#revese print
a.reverse()
print(a)

A = [1,50,30,10,20,4,5,0,-1]
print(A)

#sortig
A.sort()
print(A)
A.sort( reverse = True) # reverse sorting
print(A)

#max,min,locatin
print(min(A))
print(max(A))

print(A.index(max(A)))
print(A.index(min(A)))

#append():-Adding element from end position
x=[1,2,3,3,4]
x.append(5)
print(x)

#pop:-Deleting value end or spacific index
x.pop(2)#  2nd index value are to be deleted
print(x)
x.pop() # pop the value from end
x.pop()
print(x)
x.remove(1) # remove the value '1' in x list
x.remove(3) # remove the value '3' in x list
print(x)

#insert():-insert item at a given position
x.insert(0,1) # first give index then value( 0 index 1 is value)
x.insert(1,3)
x.insert(2,5)
print(x)

#del():-deleting item To(0) index form (2) index
del x[0:2]
print(x)

#loop inside list
b=[1,2,3,4,5]
c = [ i**2 for i in b]
print(b)
print(c)
#logic structure
d=[n**3 for n in b if n<=4]
print(d)
