year=int (input("Enter year to check leap-year or not "))

if year % 400 == 0  or year % 4 == 0 and year % 100 != 0 :
    print(year , " is a leap year")
    
else:
    print(year , "is non leap year") 
        
