menu = {
    "Pastry": {
        "Chocolate Truffle": 90,
        "Strawberry Delight": 85,
        "Black Forest": 95,
        "Red Velvet": 100,
        "Blueberry Cheese Pastry": 105,
        "Choco Lava Cake": 110,
        "Fruit Tart": 95
    },
    "Cold Drinks": {
        "Coke": 50,
        "Pepsi": 50,
        "Sprite": 50,
        "Blue Lagoon": 80,
        "Lemonade": 40,
        "Mojito": 70,
        "Iced Tea (Peach)": 60,
        "Iced Tea (Lemon)": 60
    },
    "Hot Beverages": {
        "Espresso": 70,
        "Americano": 80,
        "Latte": 95,
        "Cappuccino": 90,
        "Mocha": 100,
        "Masala Chai": 55,
        "Ginger Tea": 50,
        "Green Tea": 60,
        "Hot Chocolate": 110
    },
    "Burger": {
        "Veg Burger": 120,
        "Cheese Burger": 140,
        "Paneer Burger": 160,
        "Double Patty Burger": 180,
        "Chicken Burger": 170
    },
    "Pizza": {
        "Margherita": 220,
        "Farmhouse": 270,
        "Paneer Tikka Pizza": 290,
        "Veggie Delight": 250,
        "Chicken Barbeque Pizza": 310
    },
    "Sandwich": {
        "Grilled Cheese": 100,
        "Veg Club Sandwich": 120,
        "Paneer Sandwich": 130,
        "Corn Mayo Sandwich": 110,
        "Chicken Sandwich": 140
    },
    "Pasta": {
        "White Sauce Pasta": 160,
        "Red Sauce Pasta": 160,
        "Mix Sauce Pasta": 180,
        "Cheese Pasta": 190
    },
    "Wraps": {
        "Veg Wrap": 100,
        "Paneer Wrap": 120,
        "Cheese Wrap": 130,
        "Chicken Wrap": 140,
        "Tandoori Wrap": 135
    },
    "Snacks": {
        "French Fries": 100,
        "Garlic Bread": 80,
        "Spring Roll": 90,
        "Cheese Balls": 130,
        "Nachos with Cheese": 140,
        "Samosa": 20
    },
    "ice_cream": {
        "Vanilla Ice Cream (1 scoop)": 70,
        "Chocolate Ice Cream (1 scoop)": 80,
        "Strawberry Ice Cream": 80,
        "Butterscotch Ice Cream": 85,
        "Mango Ice Cream": 75,
        "Kesar Pista Ice Cream": 90,
        "Cookies & Cream Ice Cream": 95,
        "Choco Chip Ice Cream": 90,
        "Black Currant Ice Cream": 85
},
    "desserts": {
        "Cup Cake (Chocolate)": 60,
        "Gulab Jamun (2 pcs)": 40,
        "Waffles with Syrup": 120,
        "Rabri": 100,
        "Donut": 75,
        "Falooda": 130,
        "Brownie with Ice Cream": 150
},
   "pav_bhaji": {
       "Classic Pav Bhaji": 100,
       "Cheese Pav Bhaji": 120,
       "Khada Pav Bhaji": 110,
       "Jain Pav Bhaji": 100,
       "Butter Pav (2 pcs)": 20,
       "Masala Pav": 60,
       "Paneer Pav Bhaji": 130
},
    
    "Combos": {
        "Burger Combo (Veg Burger + Fries + Coke)": 250,
        "Pizza Combo (Farmhouse Pizza + Cold Coffee)": 320,
        "Pastry Combo (Red Velvet + Latte)": 170,
        "Wrap Combo (Paneer Wrap + Lemonade + Donut)": 210,
        "Sandwich Combo (Grilled Cheese + Mojito + Ice Cream)": 230
    }
}


#show all menu card
print("WELCOME TO CAFE".center(70,'*'))

for category, items in menu.items():
    print("\n" + category.center(70,"-"))
    for item, price in items.items():
        print(f"{item:<60} - {price}")

print("1.Take order from customer")
print("2.Qunatity for order")
print("2.Display order")
print("3.Search food items")
print("4.Delete food items from customer order")
print("5.Clear items")
print("6.Total bill")
print("7.Exit")
order={}
while True:

    choice=input("Enter your choice:")
    if(choice == '1'):
        item_n=input("Enter items to order:").strip()
        found = False
        for category,items in menu.items():
             if item_n in items:
                 order[item_n] = order.get(item_n,0)+1
                 print(f"{item_n} Added to order")
                 found = True
        if not found:
            print(f"{item_n}not found")

    elif(choice == '2'):
        if not order:
            print("Your order is empty")
        else:
            for item_n in order:
                while True:
                    try: 
                        quantity=int(input(f"Enter quantity for {item_n}:"))
                        if quantity >= 0:
                           order[item_n]=quantity
                           print(order)
                           print("Quantity is added")
                           break
                        else:
                           print("Please enter valid quantity")
                    except ValueError:
                        print("Invalid input")

    elif (choice == '3'):
        if not order:
            print("Your order is empty.")
        else:
            print("\n------ Your Order ------")
            for item_n, quantity in order.items():
                for category, items in menu.items():
                    if item_n in items:
                        price = items[item_n]
                        print(f"{item_n:<40} Qty: {quantity:<3} x rs{price:<3} = rs{quantity*price}")
                        break

    elif choice == '4':
        search_item = input("Enter the item name to search in menu: ").strip()
        found = False
        for category, items in menu.items():
            if search_item in items:
                print(f"Item Found: {search_item}")
                print(f"Category    : {category}")
                print(f"Price       : rs{items[search_item]}")
                found = True
                break
        if not found:
            print("Item not found in the menu.")

    elif choice == '5':
        a=input("Enter your choice (Yes/No)")
        if (a.lower() == 'yes'):
            print("All items have been removed from your order.",order)
        elif(a == 'no' or a == 'No'):
             print("Your order not removed.")


    elif choice == '6':
        if not order:
            print("Your order is empty.")
        else:
            print("\n" + "------  TOTAL BILL ------".center(70, "-"))
            grand_total = 0
            for item_n, quantity in order.items():
                for category, items in menu.items():
                    if item_n in items:
                        unit_price = items[item_n]
                        total_price = quantity * unit_price
                        grand_total += total_price
                        print(f"{item_n:<40} Qty: {quantity:<3} x rs{unit_price:<3} = rs{total_price}")
                        break
            print("-" * 70)
            print(f"{'TOTAL AMOUNT':<55} = ₹{grand_total}")


    elif choice == '7':
        print("Thank you for visiting our cafe! Have a great day!")
        break
    

