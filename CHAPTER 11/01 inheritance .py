class employee:
    company = "google"
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")



# class programmer:
#     company ="microsoft"
#     def show(slef):
#         print(f"the name of the employee is {self.name} and the salary is {self.salary}")

#     def showlanguage():
#         print(f"the name of the employee is {self.name} and the salary is {self.salary}")

# TODO: # THIS SAM PROGRAM DOING LIKE THIS IN SMALL TYPE USING HESITANCE WAYS 

class programmer(employee):
    company = "Google i love  coading "
    def show(self):
        print(f"the name of the employee is {self.name} and the salary is {self.salary}")


a=employee()
b=programmer()

print(a.company,b.company)