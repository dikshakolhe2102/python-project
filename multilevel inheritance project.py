# **Multilevel Inheritance**
# Example :#Example : Base Class- Employee -> emp_id, name, salary, display_info(), calculate_annual_bonus(),promote()
# # class derived1 - Manager -> department, projects_handled, assign_project(), display_manager_info()
# # Class derived2- SeniorManager -> team_size, initial_approved_budget, approve_budget(), display_senior_manager_info()
# o/p
# --- Employee Information ---
# Employee ID : EMP2001
# Name : Ravi Verma
# Salary : 120000
# Department : IT
# Projects Count : 0
# Role : Manager
# Team Size : 15
# Role : Senior Manager
# Annual Bonus : 12000.0

# Ravi Verma promoted! New Salary: 134400.0

# Project assigned to Ravi Verma. Total Projects: 1
# Budget of 500000 approved. Total approved: 700000

# --- Employee Information ---
# Employee ID : EMP2001
# Name : Ravi Verma
# Salary : 134400.0
# Department : IT
# Projects Count : 1
# Role : Manager
# Team Size : 15
# Role : Senior Manager
class Employee:
    def __init__(self,emp_id,name,salary,position="junior"):
        self.emp_id=emp_id
        self.name=name
        self.salary=salary
        self.position=position
    def display_info(self):
        print("---Employee Information---")
        print("Employee Id:",self.emp_id)
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("Position:",self.position)
    def calulate_bonus(self):
        bonus=self.salary*0.10
        print("Annual bonus:",bonus)
        return bonus
    def promote(self):
        if self.position == "junior":
            self.position = "fresher"
        elif self.position == "fresher":
            self.position = "senior"
        elif self.position == "senior":
            self.position = "head"
        else:
            print(f"{self.empname} is already at the highest position.")
    
class manager(Employee):
    def __init__(self,emp_id,name,salary,departement):
        super().__init__(emp_id,name,salary)
        self.dapartement=departement
        self.projects_handled=0
    def assign_project(self):
        self.projects_handled += 1
        print("Project Head:",self.name)
        print("Total Project:",self.projects_handled)
    def display_Manager_info(self):
        print("Departemnt:",self.dapartement)
        print("Project count:",self.projects_handled)
        print("Role:Manager")

class SeniorManager(manager):
    def __init__(self, emp_id, name, salary, departement,team_size):
        super().__init__(emp_id, name, salary, departement)
        self.team_size=team_size
        self.initial_approved_budget=100000
    def approve_budget(self,amount):
        self.initial_approved_budget += amount
        print(f"Budget of {amount} approved. Total approved:{self.initial_approved_budget}")
    def display_senior_manager(self):
        print("Team Size:",self.team_size)
        print("Role: Senoir Manager")


sm=SeniorManager("emp101","Diksha Kolhe",15000,"IT",5)

sm.display_info()
sm.display_Manager_info()
sm.display_senior_manager()
sm.calulate_bonus()
sm.promote()
sm.assign_project()
sm.approve_budget(400000)

sm.display_info()
sm.display_Manager_info()
sm.display_senior_manager()
