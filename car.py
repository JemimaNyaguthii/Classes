
# Create 3 files in the classes directory car.py, fruit.py, and bank.py. 
# Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
class Car:
    def __init__(self,color,make,model,speed):
        self.color=color
        self.make=make
        self.model=model
        self.speed=speed
    def car_use(self):
        return f"I used a {self.make} to come to school" 
    def car_speed(self):
        return f"The {self.make} was moving at  {self.speed} KM/H."   
    def car_details(self):
        return f"This{self.make} {self.model} which was driving at a {self.speed}KM/H,was {self.color}"


    