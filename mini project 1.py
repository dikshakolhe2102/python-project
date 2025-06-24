#1 create a list and add names into it
#2 remove from list
#3 show the list
#4 exit 
l=[]
while True:
    print("1.Add names of student to list")
    print("2.Remove name from list")
    print("3.Display the updated list")
    print("4.exit the system")
    ch=input("Enter a choice:")
    if ch=='1':
        element=input("Enter a element:")
        l.append(element)
        print("Elements are added")
    elif ch=='2':
        name=input("Enter a name to be removed:")
        l.remove(name)
        print("Elements are removed")
    elif ch=='3':
        print(l)
    elif ch=='4':
        break
    else:
         print("Enter a correct choice")        




#1 create a stationary list and add items into it
#2 remove items from list
#3 show the updated list
#4 exit 
l=[]
while True:
    print("1.Add stationary items to list")
    print("2.Remove items from list")
    print("3.Display the updated list of stationary items")
    print("4.exit the system")
    ch=input("Enter a choice:")
    if ch=='1':
        item=input("Enter stationary items:")
        l.append(item)
        print("items are added")
    elif ch=='2':
        trash=input("Enter a item to be removed:")
        l.remove(trash)
        print("items are removed")
    elif ch=='3':
        print(l)
    elif ch=='4':
        break
    else:
         print("Enter a correct choice")        