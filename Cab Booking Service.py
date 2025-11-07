import sqlite3

try:
    conn=sqlite3.connect("CAB_BOOKING_SYSTEM.db")
    cursor=conn.cursor()
    cursor.execute('''
    create table if not exists Driver (
                driver_id integer primary key autoincrement,
                name text,
                car_model text,
                phone text,
                available text
    )
    ''')
    conn.commit()
    cursor.execute('''
    create table if not exists Booking (
                booking_id integer primary key autoincrement,
                customer_name text,
                pickup text,
                dropoff text,
                distance real,
                fare real,
                driver_id integer,
                status text
    )
    ''')
    conn.commit()
except sqlite3.Error as e:
    print("An error occured:",e)


def Add_Driver():
    name=input("Enter driver name:")
    car_model=input("Enter Car Model:")
    phone=int(input("Enter phone no:"))
    cursor.execute('''
        insert into Driver (name,car_model,phone,available)
        values (?, ?, ?, ?)
        ''',(name,car_model,phone,'Yes',))
    conn.commit()
    if(cursor.rowcount):
        print("Driver added successfully!")

def View_Available_Driver():
    cursor.execute('select * from Driver where available=?',('Yes',))
    rows = cursor.fetchall()
    print("rowcount:",cursor.rowcount)
    print("Driver Records:")
    if not rows:
        print("No drivers avaiable right now.")
    for row in rows:
        print("************************")
        print("Driver_Id:",row[0])
        print("Name:",row[1])
        print("Car_Model:",row[2])
        print("Phone:",row[3])
        print("Available:",row[4])
        print("************************")
    
    conn.commit()

def Book_cab():
    Customer_name=input("Enter customer name:")
    pickup=input("Enter pickup location:")
    drop=input("Enter drop location:")
    distance=int(input("Enter distance:"))
    calculate_fare=distance*10
    print("Total payable amount:",calculate_fare)
    View_Available_Driver()
    driver_id=input("Enter driver id:")
    cursor.execute('select driver_id from driver where driver_id=?',(driver_id,))
    rows=cursor.fetchone()
    if not rows:
        print("Enter valid id!")
    cursor.execute('''
        insert into Booking(customer_name,pickup,dropoff,distance,fare,driver_id,status)
        values (?,?,?,?,?,?,?)
        ''',(Customer_name,pickup,drop,distance,calculate_fare,driver_id,'Booked'))
    conn.commit()
    booking_id=cursor.lastrowid
    cursor.execute('''
    update Driver 
    set available = ?
    where driver_id = ?
    ''',('No',driver_id))
    conn.commit()
    print(f'Cab bookes successfully! Your Booking ID is :{booking_id}. Please save this Booking ID for future reference(to complete or cancel the ride).')

def Complete_Ride():
        book_id=input("Enter Booking Id:")
        cursor.execute('select booking_id,driver_id from Booking where booking_id =?',(book_id,))
        rows=cursor.fetchone()
        if not rows:
            print("Enter valid Booking_id!")
        cursor.execute('''
        update Booking
        set status = ?
        where booking_id = ?
        ''',('Completed',book_id))
        conn.commit()

        cursor.execute('''
        update Driver 
        set available = ?
        where driver_id = ?
        ''',('Yes',rows[1]))
        conn.commit()

def cancel_booking():
    booking_id=input("Enter A Booking ID=")
    cursor.execute("select booking_id,driver_id,status from Booking where booking_id=? ",(booking_id))
    rows=cursor.fetchone()
    if not rows:
        print("Enter a Valid Id")
    if rows[2]=="complete":
        print("ride already complete")
        return
    if rows[2]=="cancelled":
        print("orride cancelled")
        return
    if rows[2]=="booked":
        cursor.execute('''
                    update booking set status=? where booking_id=? 
                    ''',("concelled",rows[0]))
    cursor.execute('''
                    update drivers set available=? where driver_id=? 
                    ''',("Yes",rows[1]))
    conn.commit()

def View_all_bookings():
    cursor.execute("select * from booking")
    booking=cursor.fetchall()
    print("ALL Bookings:")
    print(booking)
def View_active_booking():
    cursor.execute("select * from booking where status='booked'")
    booking=cursor.fetchall()
    print("Active (booked) Rides:")
    print(booking)


while True:
        print("====CAB BOOKING SYSTEM====")
        print("1. Add Driver")
        print("2. View Available Drivers")
        print("3. Book Cab")
        print("4. Complete Ride")
        print("5. Cancel Booking ")
        print("6. View All Bookings ")
        print("7.  View Active Bookings  ")
        print("8. Exit  ")

        choice=int(input("Enter a choice:"))
        if choice==8:
                print("THANKS FOR REACHING US OUT!")
                break
        if choice==1:
            Add_Driver()
        elif choice==2:
            View_Available_Driver()
        elif choice==3:
            Book_cab()
        elif choice==4:
            Complete_Ride()
        elif choice==5:
            cancel_booking()
        elif choice==6:
            View_all_bookings()
        elif choice==7:
            View_active_booking()
        if choice==8:
                print("THANKS FOR REACHING US OUT!")
                break