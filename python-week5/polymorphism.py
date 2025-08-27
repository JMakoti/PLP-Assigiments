class Vehicles:
    def __init__(self, brand ,model):
        self.brand = brand
        self.model = model

    #method
    def move(self):
        return ("moves!")

class Car(Vehicles):
    pass

class Plane(Vehicles):
    def move(self):
        return ("Flys!")

class Boat(Vehicles):
    def move(self):
        return ("Sails!")

#creating objects
car0 = Car("Ford","Mustang")
plane0 = Plane("Boeing","747")
boat0 = Boat("Ibiza","Touring 20")


for vehicle in (car0 , plane0 ,boat0):
    print(f"{vehicle.brand} {vehicle.model} {vehicle.move()}")
   