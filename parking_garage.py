#Parking Garage Project

class Parking_Garage():


    def __init__(self):
        self.tickets = [1,2,3,4,5,6,7,8,9,10]
        self.spaces_available = []
        self.current_tickets = {}

    def take_ticket(self):
        if self.spaces_available <= 0:
            print("This lot is full.")
        else:
            self.spaces_available -= self.tickets
            
            
            
            


    def pay(self):
        ticket_number = input("What is your ticket number?")
        



    def leave():


