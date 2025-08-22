class Train: 
    def __init__(self, train_id, name, seats): 
        self.train_id = train_id 
        self.name = name 
        self.seats = seats 
        self.booked_seats = 0 

    def get_available_seats(self): 
        return  self.seats - self.booked_seats 

    def book_seat(self): 
        if self.get_available_seats() > 0:
            self.booked_seats += 1
        else:
            print("No seats available") 

    def cancel_seat(self): 
        if self.booked_seats > 0:
            self.booked_seats -= 1

    def display_train_info(self): 
        return f"Train ID: {self.train_id}, Name: {self.name}, Available Seats: {self.get_available_seats()}"

class Person: 
    def __init__(self, name, age, gender): 
        self.name = name 
        self.age = age 
        self.gender = gender 

class Passenger(Person): 
    def __init__(self, name, age, gender, pnr, train_id, timestamp): 
        super().__init__(name, age, gender) 
        self.pnr = pnr 
        self.train_id = train_id 
        self.timestamp = timestamp 

    def display_passenger_info(self): 
        return (f"PNR: {self.pnr}, Name: {self.name}, Age: {self.age}, Gender: {self.gender}, "
                f"Train ID: {self.train_id}, Booking Time: {self.timestamp}")
