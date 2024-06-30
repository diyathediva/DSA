class Vehicle:
    def __init__(self,colour,size,fuel):
       self.colour = colour
       self.size = size
       self.fuel = fuel 
       self.totaldistance = 0
    def travel(self,distance):
        self.totaldistance = self.totaldistance + distance
        
class Car(Vehicle):
    def __init__(self,colour,size,fuel,brand,numofwheels,numofdoors):
        Vehicle.__init__(self,colour,size,fuel)
        self.brand = brand
        self.numofwheels = numofwheels
        self.numofdoors = numofdoors
     
    def cardetails(self):
        print('This',self.brand,'of colour',self.colour,'has travelled distance of',self.totaldistance)
      
           
    
vehicle1 = Vehicle('red','small','petrol')
print(vehicle1.colour)
print(vehicle1.size)
print(vehicle1.fuel)
print(vehicle1.totaldistance)
vehicle1.travel(20)
print(vehicle1.totaldistance)

car = Car('blue','big','petrol','BMW','4','4')
car.cardetails()
car.travel(30)
car.cardetails()

vehicle1.cardetails()
