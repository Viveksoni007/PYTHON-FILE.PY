# Create a class “Programmer” for storing information of few programmers working at Microsoft.

class programer:
    compamy = "MICROSOFT"
    def __init__(self , name ,salary ,pincode):
        self.name =name
        self.salry=salary
        self.pincode=pincode
        



p= programer("vivek ",9999999,122001)
print(p.compamy,p.name,p.salry,p.pincode)

r= programer("rohan ",9999999,122001)
print(r.compamy,r.name,r.salry,r.pincode)