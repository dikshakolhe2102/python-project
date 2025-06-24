#Phonebook Application
#1.add contact
#2.search contact
#3.view all
#4.count contact
#5.delete contact
#6.clear all contact
#7.exit


d={}
while True:
    print("Phone Book Application")
    print("1.Add Contact")
    print("2.Search Contact")
    print("3.View All contact")
    print("4.Count Contact")
    print("5.Delete Contact")
    print("6.Clear all Contact")
    print("7.Exit")

    choice=input("Enter your choice:")

    if (choice == '1'):
        print("Add Contact")
        add=input("Enter Name:")
        cont=input("Enter contact no:")
        if add not in d:
            d[add]=[]
        d[add].append(cont)
        print(d)

    elif (choice == '2'):
        print("Search contact")
        search=input("Enter element which you want to search:")
        if(search in d):
            print("Contact is present")
        else:
            print("Not Found!")

    
    elif( choice == '3'):
        print("View all contact")
        print(d)

    elif( choice == '4'):
        print("Count all contact")
        count=len(d)
        print(count)

    elif (choice == '5'):
        print("Delete contact")
        delete=input("Enter contact you want to delete:")
        a=d.pop(delete)
        print("Contact are removed",a)
    
    elif(choice == '6'):
        print("Clear Contact")
        b=input("You want to clear all contact (yes/no):")
        if(b == 'yes' or b == 'YES'):
           clear=d.clear()
           print("All contacts are cleared",clear)

        elif(b == 'no' or b == 'No'):
            print("Do not clear all contact")

    elif(choice == '7'):
        print("Exit")
        break








