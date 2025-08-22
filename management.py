import random 
from datetime import datetime 
from models import Train, Passenger
from exceptions import BookingError, PNRNotFoundError


class RailwayManagement: 
    def __init__(self): 
        self.trains = [] 
        self.passengers = {} 

    def add_train(self, train): 
        #  Add new Train to self.trains 
        self.trains.append(train)

    def display_trains(self): 
        # Loop through trains and print details 
        if not self.trains:
            print("No trains available.")
        for Train in self.trains:
            print(Train.display_train_info())

    def find_train(self, train_id): 
        """Find a train by its ID.Returns the train object if found,else None.""" 
        # Loop through self.trains and return the train with matching train_id 
        for train in self.trains:
            if train.train_id == train_id:
                return train
        return None
    
    def generate_pnr(self, train_id): 
        date = datetime.now().strftime("%d%m%y")
        rand_str = ''.join(random.choices("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", k=4))
        return f"{train_id}-{date}-{rand_str}"

    
    def book_ticket(self, train_id, name, age, gender): 
        """ 
        TODO: 
        1. Find train by train_id. 
        2. If seats are available, book and generate PNR. 
        3. If not available, then raise BookingError. 
        4. Store booking details file (dict with pnr, passenger, train_id, timestamp). 
        """ 
        # Full booking flow: check seat, assign, create passenger 
        train = self.find_train(train_id)
        if not train:
            raise BookingError("Invalid Train ID")

        if train.get_available_seats() <= 0:
            raise BookingError("No seats available")

        train.book_seat()  
        pnr = self.generate_pnr(train_id)
        timestamp = datetime.now()
        passenger = Passenger(name, age, gender, pnr, train_id, timestamp)
        self.passengers[pnr] = passenger
        self.save_booking_to_file(passenger)
        return passenger

    def cancel_ticket(self, pnr): 
        """ 
        TODO: 
        1. Find booking by PNR ,if PNR not found raise PNRNotFoundError. 
        2. Remove booking and increment train's seat count. 
        """ 
        # Cancel booking by removing from dict and restoring seat 
        if pnr not in self.passengers:
            raise PNRNotFoundError("PNR not found")

        passenger = self.passengers.pop(pnr)
        train = self.find_train(passenger.train_id)
        if train:
            train.cancel_seat()
        return passenger


    def get_passengers_by_train(self, train_id): 
        """ 
        Get a list of all passengers for a specific train using train_id. 
        """ 
        return [p for p in self.passengers.values() if p.train_id == train_id]

    def check_pnr_status(self, pnr): 
        """ 
        TODO: 
        1. Find booking by PNR. 
        2. Display details if found, else raise PNRNotFoundError. 
        """ 
        if pnr not in self.passengers:
            raise PNRNotFoundError("PNR not found")
        return self.passengers[pnr]

    def save_booking_to_file(self, passenger): 
        #  To Do: write booking details to file
        with open("bookings.txt", "a") as f:
            f.write(f"{passenger.pnr},{passenger.name},{passenger.age},{passenger.gender},"
                    f"{passenger.train_id},{passenger.timestamp}\n")
