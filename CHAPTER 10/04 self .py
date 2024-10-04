class employee:
    language= "python", "enlish"
    slary=    999999900000 # this is called is class attribute

    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.slary}" )

    

    @staticmethod    #this is called a static method whitout using the self method
    def greet():
        print("good morning")    



vivek = employee()
# vivek.language = "java script"
print( vivek.slary,vivek.language)

# vivek.getinfo()
vivek.greet()
# employee.getinfo(vivek)