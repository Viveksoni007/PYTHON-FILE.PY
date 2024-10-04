class employee:
    company = "google"
    name= "defalut name "
    def show(self):
        print(f"the name of the employee is {self.name} and the company is {self.company}")


class coder:
    language="python"
    def printlanguage(self):
        print(f"out of all of the language here is the your language :{self.language}")


class programmer(employee,coder):
    company = "Google i love  coading "
    def showlanguage(self):
        print(f"the name  of the company {self.company} and the good in is {self.language}")


a=employee()
b=programmer()

# print(a.company,b.company)

b.show()
b.printlanguage()
b.showlanguage()
