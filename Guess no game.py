import random
Random_no=random.randint(1,5)
print("Guess the number between 1 to 20")
count=0
while True:
    num=int(input("Enter your guess number:"))
    if num < Random_no:
        print("Try Again!")
        count+=1

    elif num > Random_no:
        print("Try Again!")
        count+=1
    else:
        print("Attempts:",count)
        print("Correct! You win")
        break
