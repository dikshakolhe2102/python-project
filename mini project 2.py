#1. display choice
#2. union : science,atrs,commerce
#3. show intersection
#4. add member: 
#5. remove member: clud member
#6. check membership: member club
#7. exit


s=set()
science=set()
commerce=set()
arts=set()
while True:
    print("1.Display choice")
    print("2.Add Member")
    print("3.Union: Science,Atrs and Commerce")
    print("4.Show intersection")
    print("5.Remove member:")
    print("6.Check membership")
    print("7.Exit")

    choice=input("Enter your choice:")

    if choice == '1':
        print("1.Display choice")
        print("2.Add Member")
        print("3.Union: Science,Atrs and Commerce")
        print("4.Show intersection")
        print("5.Remove member:")
        print("6.Check membership")
        print("7.Exit")

    elif choice == '2':
        
        print("Choose club to add member :")
        print("1.Science")
        print("2.Commerce")
        print("3.Arts")
        choiceclub = input("Enter your club:")
        add=input("Enter member:")
        if choiceclub == '1':
           science.add(add)
           print(science)
        elif choiceclub == '2':
           commerce.add(add)
           print(commerce)
        elif choiceclub == '3':
           arts.add(add)
           print(arts)
        else:
            print("Enter valid choice")
        print("Memebrs are added")

    elif choice == '3':
        union=input("enter a club which 2 you want to union:")
        uni=input("enter a club which 2 you want to union:")
        if(union == 'science' or uni == 'SCIENCE' and union == 'commerce' or uni == 'COMMERCE' ):
            print(science.union(commerce))
        elif(union == 'commerce' or uni == 'COMMERCE'and union == 'arts' or uni == 'ARTS'):
            print(commerce.union(arts))
        else:
            print(arts.union(science))
    
    elif choice == '4':
        sect=input("Enter a club which you want to intersection")
        section=input("Enter a club which you want to intersection")
        if(sect == 'science' or section == 'SCIENCE' and union == 'commerce' or uni == 'COMMERCE'):
          print(science.intersection(commerce))
        elif (sect == 'commerce' or section == 'COMMERCE' and union == 'arts' or uni == 'ARTS'):
          print(commerce.intersection(arts))
        else:
            print(arts.intersection(science))

    elif choice == '5':
        c=input("Enter which club you want to remove member:")
        if(c == 'science' or c == 'SCIENCE'):
            user=input("Enter a name you want to remove:")
            science.reomve(user)
            print(science)
        elif (c == 'commerce' or c == 'COMMERCE'):
            user=input("Enter a name you want to remove:")
            commerce.reomve(user)
            print(commerce)
        elif (c == 'arts' or c == 'ARTS'):
            user=input("Enter a name you want to remove:")
            arts.reomve(user)
            print(arts)    

    elif choice == '6':
         a=input("enter which club you want to check member:")
         member=input("enter a member name:")
         if(a == "science"):
             print("It is a member of science club",member in science) 
         elif(a == "commerce"):
             print("It is a member of commerce",member in commerce)
         elif(a == "arts"):
             print("It is a member of arts",member in arts)
         else:
             print("It is a not member")

    elif choice == '7':
        print("Exit")
    

    else :
        print("Invalid Choice! Please try again")
