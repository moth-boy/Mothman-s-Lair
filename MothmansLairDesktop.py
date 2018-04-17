def showInstructions():
    print("""
Mothman's Lair
==============

You wake up on a comfy bed in a dark cave. There is a large, winged figure
sitting by the entrance. How will you escape?

Commands:
    go [north, south]
    open [object]
    get [item]
    approach [mothman]
""")

def showStatus():
    print("--------------------")
    print("You are in the " + currentRoom)
    print("Inventory: " + str(inventory))
    if "item" in rooms[currentRoom]:
        print("You see a " + rooms[currentRoom]["item"])
    if "container" in rooms[currentRoom]:
        print("You see the " + rooms[currentRoom]["container"])
    if "objective" in rooms[currentRoom]:
        print("You see the Mothman")
    print("--------------------")

inventory = []

rooms = {
    "Garden" : {"south" : "Cave",
                "item" : "bee"},
    "Cave" : {"north" : "Garden",
              "container" : "fridge",
              "objective" : "mothman"}
    }

currentRoom = "Cave"

showInstructions()

while True:

    showStatus()
    
    move = ""
    while move == "":
        move = input("> ")
    move = move.lower().split()

    if move[0] == "go":
        if move [1] in rooms[currentRoom]:
            currentRoom = rooms[currentRoom][move[1]]
        else:
            print("You can't go that way!")

    if move[0] == "get":
        if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
            inventory += [move[1]]
            print(move[1] + " got!")
            del rooms[currentRoom]["item"]

        else:
            print("Can't get " + move[1] + "!")

    if move[0] == "open":
        if "container" in rooms[currentRoom] and move[1] in rooms[currentRoom]["container"]:
            print("You open the fridge and find a sock!")
            inventory += ["sock"]
            
        else:
            print("You cannot open that!")

    if move[0] == "approach":
        if currentRoom == "Cave" and "bee" in inventory and "sock" in inventory:
            print("""
You nervously approach the winged figure and make a small noise.
He turns around suddenly and is very startled! Now what?

Option 1: scream
Option 2: give him the bee and the sock you found
""")

            choice = input("Which option do you choose? ")
            if choice == "1":
                 print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Startled also, you scream back at the monster! He starts crying. :(
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""")

                 showInstructions()
                 
            elif choice == "2":
                 print("""
The Mothman smiles! He eats your sock and puts the bee on his head, then moves aside
so you may leave his cave. Have a good day!
""")
                 break
                    
        else:
            print("Maybe it's not a good idea to talk to him just yet...")
