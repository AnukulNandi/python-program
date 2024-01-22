c = 1 + 3j
print( type(c))

str = "string using doble code"
print(str)

s= '''tring using tripule code'''
print(s)

# LIST(third braket)
# list are starting squer braket '[' and enclose with ']'. It can hold hetarozenious data
lis=['anukul',123,'debu',314, 'monu']
print(lis)
print(type(lis))
print(lis[2: ]) # in this 2 is staring index
print(lis[0:1]) #in this 0 is starting index and 1 is element number
print(lis + lis) # in this concatethe list
print(lis * 3) # reprinting

# TUPLE(first braket)
# tuple are starting squer braket '(' and enclose with ')'
tup = ( "hi", 1, " Anukul" , " nandi")
print(tup)
print(type(tup))
print( tup[1: ])
print(tup [0:2])

# dictionary(Second braket)
#Dictionary are starting squer braket '{' and enclose with '}'
d={10:"Anukul",2:"Manojit",3:"Ramesh", 4:"Sayan"}
d[5]='shankha' # insert new datai nto dictionary
print(d)
print(type(d))
print("my name is " +  d [10])#identify by key  1
print("friend name is " + d[4])#identify by key  4
print(d.values())# show the dictionary's values
print(d.keys())# show the dictionary's keys

