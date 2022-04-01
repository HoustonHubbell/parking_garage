class Parking_Garage():

    def __init__(self):
        self.tickets = [10,9,8,7,6,5,4,3,2,1]
        self.spaces_available = 10
        self.current_tickets = {}

    def take_ticket(self):
        if self.spaces_available <= 0:
            print("This lot is full.")
        else:
            new_ticket = self.tickets.pop()
            self.current_tickets[new_ticket] = "unpaid"
            self.spaces_available -= 1
            print(self.current_tickets)

    def pay(self):
        ticket_number = int(input("What is your ticket number? "))
        if self.current_tickets[ticket_number] == "unpaid":
            pay_ticket = input("You need to pay $3. Pay now? y/n ")
            if pay_ticket.lower() == 'y':
                self.current_tickets[ticket_number] = "paid"
            else:
                print("You need to pay for your parking.")
        else:
            print("You have already paid")
        print(self.current_tickets)

        
    def leave_garage(self):
        ticket_number = int(input("What is your ticket number? "))
        if self.current_tickets[ticket_number] == "unpaid":
            pay_ticket = input("You need to pay $3. Pay now? y/n ")
            if pay_ticket.lower() == 'y':
                self.current_tickets[ticket_number] = "paid"
                self.spaces_available += 1
                self.tickets.append(ticket_number)
                del self.current_tickets[ticket_number]
                print("Thank you for coming")
            else:
                print("You need to pay for your parking.")
            
        else:
            self.spaces_available += 1
            self.tickets.append(ticket_number)
            del self.current_tickets[ticket_number]
        print(self.current_tickets)

car = Parking_Garage()

def run():
    while True:
        response = input("What would you like to do? Options: park, pay, leave, quit  ")
        if response.lower() == "park":
            car.take_ticket()
        elif response.lower() == "pay":
            car.pay()
        elif response.lower() == "leave":
            car.leave_garage()
        elif response.lower() == "quit":
            break
        else:
            "This is not a valid response."
run()

                

         #if unpaid, run paid method
         #if paid, increment spaces available by 1 and self.tickets by 1; decrease self.current_tickets by 1
