class Person:
    def __init__(self,name,age,phone_no):
        self.name=name
        self.age=age
        self.phone_no=phone_no
    

class TravelDetails():
    def __init__(self,travel_mode):
        self.travel_mode=travel_mode
    
class Tourist(Person,TravelDetails):
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Mobile Number:",self.phone_no)
        print("Travel Mode:",self.travel_mode)
    
class TouristManagementSystem(Tourist):
    def __init__(self,name,age,phone_no,travel_mode):
        Person.__init__(self,name,age,phone_no)
        TravelDetails.__init__(self,travel_mode)
    def validate_name(self):
        if(self.name.isalpha()):
            return True
            
        return False
            
    def validate_age(self):
        if(self.age>=60 and self.age<=99):
            return True
        
        return False
    def validate_phone(self):
        if(self.phone_no.isdigit() and len(self.phone_no)==10 ):
            return True

        return False
    def validate_travel_mode(self):
        if(self.travel_mode.lower() == 'airway' or self.travel_mode.lower() == 'roadway'):
            return True

        return False
    def generate_tourist_id(self):
        a=self.name[0:2]
        b=self.phone_no[0:2]
        c=self.travel_mode[0:2]
        print("Tourist ID generated sucessfully:",a.upper()+str(self.age)+b+c.upper())


print("Example:")
print("Input:")
name=input("Enter tourist name:")
age=int(input("Enter Age:"))
phone_no=input("Enter Mobile Number:")
travel_mode=input("Enter a mode(Roadway/Airway):")
def main():
    obj=TouristManagementSystem(name,age,phone_no,travel_mode)
    print("---Tourist Information---")
    obj.display()

    if not(obj.validate_name()):
        print("Name Not Valid!")
        return
    if not(obj.validate_age()):
        print("Age Not Valid!")
        return
    if not(obj.validate_phone()):
        print("Mobile Number Not Valid!")
        return
    if not(obj.validate_travel_mode()):
        print("Travel Mode Not Valid!")
        return
    obj.generate_tourist_id()

main()


