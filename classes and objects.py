
#class defintion
class Fruit: 
    #attributes and properties
    def __init__(self,name,colour,size,taste):
        self.name = name #creating property for name and assigning it to self.name
        self.colour = colour
        self.size =size
        self.taste = taste
        self.day = 0
    def nextday(self):
        self.day = self.day +1
    def check_freshness(self):
        print("This fruit is",self.day,"days old")
        

#object
fruit1 = Fruit('orange','orange','medium','sweet')
print(fruit1.name)
print(fruit1.colour)
print(fruit1.size)
print(fruit1.taste)
fruit1.check_freshness()
fruit1.nextday()
fruit1.check_freshness()

fruit2 = Fruit('banana','yellow','medium','sweet')
print(fruit2.name)
print(fruit2.colour)
print(fruit2.size)
print(fruit2.taste)
fruit2.check_freshness()