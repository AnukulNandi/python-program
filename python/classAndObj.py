class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def myfunc(self):
        #only string can not int
        print("hello  i am "+ self.name )
p1 = person("Anukul",21)
p1.myfunc()