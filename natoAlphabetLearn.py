import random
natoList = ["alpha", "bravo", "charlie", "delta", "echo", "foxtrot", "golf", 
            "hotel", "india", "juliett", "kilo", "lima", "mike", "november", 
            "oscar", "papa", "sierra", "tango", "uniform", "victor", "whiskey",
            "xray", "yankee", "zulu"]
usrInput = " "
print("NATO Buchstabier Lerner")
while usrInput != "quit":
    checkVar = random.choice(natoList)  # find random nato world
    buchstabe = checkVar[0]             # find first letter
    
    print("\nWie wird der Buchstabe \"" + buchstabe.capitalize() + "\" ausgeschrieben: ")
    usrInput = input().lower()
    if(usrInput == checkVar):
        print("---Das war richtig!---")
    else:
        print("Falsch!!!")
