# class Student:
#     school="Akirachix"
#     def __init__(self,name,age,nationality,first_name,last_name):
#         self.name=name
#         self.age=age
#         self.nationality=nationality
#         self.first_name=first_name
#         self.last_name=last_name
#     def greet_student(self):
#         return f"Hello {self.name},welcome to {self.school} am proud to be an {self.nationality}"

# Update the Student Class to include these attributes - first_name, last_name, age, country
#      - Add these methods to the Student class
#              - show_full_name
#              - year_of_birth
#              - show_initials
class Student:
    def __init__(self,first_name,last_name,age,country):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.country=country  
    def show_full_name(self):
        return f"Hello I am {self.first_name}  {self.last_name}" 

    def show_initials(self):
        return f"Hello,my initials are {self.first_name[0]} {self.last_name[0]}"

    def year_of_birth(self):
        return f"Hello I was born in {2023-self.age}"    


phrase='"my name is jem"'








    
    
   
