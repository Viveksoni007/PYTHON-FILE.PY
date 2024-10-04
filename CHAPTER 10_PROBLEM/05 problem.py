# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
from random import randint
class train:
    def __init__(self, trainno ,):
        self.trainno=trainno
        
    def book(self,fro,to):
        print(f"Ticket is booked in train no : {self.trainno} form {fro}to {to}")

    def getstatus(self):
        print(f"train no {self.trainno}is runnung on time ")

    def getfare(self,fro,to):
        print(f"train fare in total caluclated with gst {self.trainno}form {fro }to {to} is {randint(1000,3000)}")


t= train(12557)
t.book ("chakia" , "delhi")
t.getstatus ()
t.getfare ("chakia" , "delhi")

