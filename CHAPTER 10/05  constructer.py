class employee:
    language= "python", "enlish"
    slary=    999999900000 # this is called is class attribute

    def __init__(self,name,slary,language):
        self.name =name 
        self.slary=slary
        self.language=language
        print("I am creating a new object called dunder method ")
        

    def getinfo(self):
        print(f"the language is {self.language}. the salary is {self.slary}" )

    

    @staticmethod    #this is called a static method whitout using the self method
    def greet():
        print("good morning")    



vivek = employee("vivek",999999999999,"c++")
# vivek.name ="vivek"   #maan lo ya muhe print nshi chsngr karna object istance ke se
print(vivek.name,vivek.slary,vivek.language)



# rohan =employee()
# rohan.name = "rohan soni"
# print(rohan.name,rohan.slary)