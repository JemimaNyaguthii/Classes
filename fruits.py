# Create 3 files in the classes directory car.py, fruit.py, and bank.py. 
# Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
class Fruit:
    def __init__(self,color,texture,flavour):
        self.color=color
        self.texture=texture
        self.flavour=flavour
    def fruit_eat(self):
        return f"Apple is a {self.color} fruit and it is {self.texture}"
    def fruit_blend(self):
        return f"A {self.color} apple has a {self.flavour} flavour" 
    def fruit_sell(self):
        return f"A {self.color} apple with a {self.flavour} flavour is expensive."    



