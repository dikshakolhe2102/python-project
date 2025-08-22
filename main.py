#import necessary modules 
from management import RailwayManagement
from models import Train
from exceptions import BookingError, PNRNotFoundError


system = RailwayManagement() 

# Preload some trains 
system.add_train(Train(101, "Rajdhani Express", 5)) 
system.add_train(Train(102, "Shatabdi Express", 3)) 
system.add_train(Train(103, "Duronto Express", 2)) 

while True: 
    print("\n===== Railway Management System =====") 
    print("1. Display Trains") 
    print("2. Book Ticket") 
    print("3. Cancel Ticket") 
    print("4. Check PNR Status") 
    print("5. View Passengers by Train") 
    print("6. Exit") 

    choice = input("Enter your choice (1-6): ") 

    try: 
        if choice == '1': 
            # Display all trains with their info
            # if choice == '1':
            print("\n--- Available Trains ---")
            system.display_trains()

        elif choice == '2': 
            """ TODO: 
            1. Get train_id, name, age, gender 
            2. book ticket using system.book_ticket() 
            3. dispplay passenger info on success 
            """ 
            train_id = int(input("Enter Train ID: "))
            name = input("Enter Passenger Name: ")
            age = int(input("Enter Age: "))
            gender = input("Enter Gender: ")
            
            passenger = system.book_ticket(train_id, name, age, gender)
            print("\nTicket booked successfully!")
            print(passenger.display_passenger_info())


        elif choice == '3': 
            """ TODO: 
            1. Get PNR from user. 
            2. Call system.cancel_ticket(pnr) 
            3. Display success message. 
            """ 
            pnr = input("Enter PNR Number: ")
            system.cancel_ticket(pnr)
            print("Ticket cancelled successfully!")


        elif choice == '4': 
            """ TODO: 
            1. Get PNR from user. 
            2. Call system.check_pnr_status(pnr) 
            3. Display status. 
            """ 
            pnr = input("Enter PNR Number: ")
            passenger = system.check_pnr_status(pnr)
            print("\nPNR Status Found:")
            print(passenger.display_passenger_info())

        elif choice == '5': 
            """ TODO: 
            1. Get train_id from user. 
            2. Call system.get_passengers_by_train(train_id) 
            3. Display passengers. 
            """ 
            train_id = int(input("Enter Train ID: "))
            passengers = system.get_passengers_by_train(train_id)
            if passengers:
                print(f"\n--- Passengers for Train {train_id} ---")
                for p in passengers:
                    print(p.display_passenger_info())
            else:
                print("No passengers found for this train.")

        elif choice == '6': 
            print("Thank you for using the Railway Management System.") 
            break 

        else: 
            print("Invalid choice! Please try again.") 

    except BookingError as be:
        print(f"Booking Error: {be}")
    except PNRNotFoundError as pe:
        print(f"PNR Error: {pe}")
    except Exception as e:
        print(f"Unexpected Error: {e}")