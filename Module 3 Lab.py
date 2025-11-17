#Name: Douglas Marshall
#ASS: Module 3 Lab
#Def: Takes traits of a vehicle and prints them



class vehicle:
    type = "car"

    def __init__(self, type):
        self.type = type
        
            
            
class automobile(vehicle):
    
    def __init__(self, type, year, make, model, doors, roof):
        super().__init__(type)
        self.type = vehicle.type
        self.year = year
        self.make = make
        self.model = model
        
        if doors == 2 or 4:
            self.doors = doors
            
        if roof == "solid" or "sun roof":
            self.roof = roof
            
    def __str__(self):
        return f"Vehicle type: {self.type}\nYear: {self.year}\nMake: {self.make}\nModel: {self.model}\nNumber of doors: {self.doors}\nType of roof: {self.roof}"
    
year = int(input("What year is it? "))
make = str(input("What is the make? "))
model = str(input("The model? ")) 

doors = ""

while doors != 2 and doors != 4:
    doors = int(input("Does it have 2 doors or 4? "))
    if doors != 2 and doors != 4:
        print("Please enter either \"2\" or \"4\". ")
    
roof = ""

while roof != "solid" and roof != "sun roof":
    roof = str(input("Type of roof? \"solid\" or \"sun roof\" "))
    if roof != "solid" and roof != "sun roof":
        print("Acceptable answers: \"solid\" or \"sun roof\" ")

vehicle1 = automobile(type, year, make, model, doors, roof)
print(vehicle1)
    


    