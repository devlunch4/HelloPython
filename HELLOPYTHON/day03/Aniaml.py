class Animal:
    def __init__(self):
        self.age= 0
        self.egg = False
    def getOld(self):
        self.age+=1 
        
        
a = Animal()
print(a.age)
print(a.egg)
a.getOld()
print(a.age)
print(a.egg)