class User:
    def __init__(self,username,email):
        self.username=username
        self.email=email
    def display_info(self):
        print("Username:",self.username)
        print("Email ID:",self.email)

class Customer(User):
    def __init__(self,username,email):
        super().__init__(username,email)
        self.cart=[]
        
    def add_to_cart(self):
        self.items=input("Enter items you want to add in cart:")
        self.cart.append(self.items)
    def display(self):
        print(self.cart)
        print(f"{self.username}:{self.cart}")

class Seller(User):
    def __init__(self,username,email):
        super().__init__(username,email)
        self.inventory=[]
    def add_product(self):
        self.item_inventory=input("Enter items to inventory:")
        self.inventory.append(self.item_inventory)
    def view_invebtory(self):
        print(f"Seller Inventory:{self.inventory}")

class admin(User):
    def __init__(self,username,email):
        super().__init__(username,email)
        self.perm=[]
    def permission(self):
        self.perm.append("manage_users")
        self.perm.append("mange_site")
        self.perm.append("view_report")
    def display_permission(self):
        print(self.perm)

obj=Seller("Diksha","diksha54")
obj1=Customer("Kolhe","kolhe12")
obj1.add_to_cart()
obj1.display_info()
obj1.display()


obj.add_product()
obj.display_info()
obj.view_invebtory()

obj2=admin("vedant","vedan122")
obj2.permission()
obj2.display_info()
obj2.display_permission()

