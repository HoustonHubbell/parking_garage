#Parking Garage Project

class Parking_Garage():

    def __init__(self):
        self.tickets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.spaces_available = 10
        self.current_tickets = {}

    def take_ticket(self):
        if self.spaces_available <= 0:
            print("This lot is full.")
        else:
            new_ticket = self.tickets.pop()
            self.current_tickets[new_ticket] = "unpaid"
            self.spaces_available -= 1

    def pay(self):
         ticket_number = input("What is your ticket number?")
         if ticket_number[new_ticket] == "unpaid":
            pay_ticket = input("You need to pay $3. Pay now? y/n")
            if input.lower() == 'y':
                ticket_number[new_ticket] = "paid"
            else:
                print("You need to pay for your parking.")

        
    def leave_garage(self):
         if self.current_tickets[new_ticket] == "unpaid":
            print("You need to pay now.")
         else:
             self.tickets = new_ticket.pop()
             self.spaces_available += 1

    def run():
        while True:
            response = input("What would you like to do? Options: take ticket, leave")
            if response.lower() == "take ticket":
                



         #if unpaid, run paid method
         #if paid, increment spaces available by 1 and self.tickets by 1; decrease self.current_tickets by 1


