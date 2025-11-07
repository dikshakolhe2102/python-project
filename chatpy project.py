import re
import datetime
import random
name=None
l=[ "Why don’t skeletons ever fight each other? ->Because they don’t have the guts.",
    "What’s a computer’s favorite snack?->Microchips.",
    "Why did the scarecrow win an award? ->Because he was outstanding in his field.",
    "Parallel lines have so much in common… ->It’s a shame they’ll never meet.",
    "Why don’t scientists trust atoms? ->Because they make up everything!"
]
def Chatpy(i):
    global name
    p=re.search(r"\b(Hi|Hello|Hey)\b",i,re.I)
    if p:
        return f"{p.group()},What's your name?"
    
    a=re.search(r"\bmy name is (\w+)",i,re.I)
    if a:
        name=a.group(1)
        if name:
            return f"Nice to meet you, {name}! How can I assist you today?"
        else:
            return "Nice to meet you,! How can I assist you today?"

    
    if re.search(r"\b(Who am i?)\b",i,re.I):
        if name:
            return f"You told me your name is {name}."
        else:
            return "You didn't tell me name."
        
    if re.search(r"\b(Tell me a joke)\b",i,re.I):
        return random.choices(l)
    
    if re.search(r"\b(What date|time is it?)\b",i,re.I):
        return f"The current date and time{datetime.datetime.now()}"
    
    if re.search(r"\b(Goodbye|Bye)\b",i,re.I):
        if name:
            return f"Goodbye {name}! Have a wonderful day!"
        else:
            return "Goodbye! Have a wonderful day!"
    
    if re.search(r"\b(Give me regex pattern for mail)\b",i,re.I):
        return(r"^\w+@[a-z A-Z]{2,8}\.[a-z A-Z]{2,3}$")
    
    if re.search(r"\b(Give me regex pattern for mobile number)\b",i,re.I):
        return(r"^[+91]?[7-9][0-9]{9}$")
    
    
    return f"I Am Not Able To Understand, Please Put Correct Information!"
    


print("ChatPy is running!(type 'exit' to quit)")
while True:
    i=input("You: ")
    pattern=re.search("exit|quit",i,re.I)
    if pattern:
        break
    else:
        print("Bot:",Chatpy(i))






