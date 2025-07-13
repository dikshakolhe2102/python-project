#class employee 
#1create employee(using construtor)
#in constructor empname,id,position,department
#2promotion 
#if position= fresher-junior, junior to senior ,senior to head
#3 departement
#branch is at pune-hydrabad, hydrabad-mumbai, mumbai-banglore
#4 display
#5take emp id that validate using static method
#starting with emp and its length is 6
#if emp id is validate then create object
#create 2 object

class Employee:
    def __init__(self,a,b,c,d):
        self.empname=a
        self.id=b
        self.position=c
        self.department=d
    def promote(self):
        if self.position == "fresher":
            self.position = "junior"
        elif self.position == "junior":
            self.position = "senior"
        elif self.position == "senior":
            self.position = "head"
        else:
            print(f"{self.empname} is already at the highest position.")
    def transfer_department(self):
        if self.department == "pune":
            self.department = "hyderabad"
        elif self.department == "hyderabad":
            self.department = "mumbai"
        elif self.department == "mumbai":
            self.department = "bangalore"
        else:
            print(f"No transfer available from {self.department}.")
    def display(self):
        print("Name:",self.empname)
        print("ID:",self.id)
        print("Position:",self.position)
        print("Department:",self.department)
    @staticmethod
    def validate_empid(empid):
        return empid.startswith("emp") and len(empid) == 6

empid1 = "emp01a"
empid2 = "emp02b"

if Employee.validate_empid(empid1):
    emp1 = Employee("Diksha", empid1, "fresher", "pune")
else:
    print("Invalid ID for employee 1")

if Employee.validate_empid(empid2):
    emp2 = Employee("Ravi", empid2, "junior", "hyderabad")
else:
    print("Invalid ID for employee 2")

emp1.promote()
emp1.transfer_department()
emp1.display()
emp2.promote()
emp2.transfer_department()
emp2.display()