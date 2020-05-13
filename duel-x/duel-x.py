import random, items, os
itemCount = 5
defaultHp = 24
windows = False

if os.system("clear") == 1:
    windows = True

def clear():
    if not windows:
        os.system("clear")
    else:
        os.system("cls")

class player:
    def __init__(self, name, items):
        self.hp = defaultHp
        if type(name) is str and len(name) > 1:
            self.name = name
        else:
            raise TypeError("Name must be a string and longer than 1 character!")
        if type(items) is list and len(items) == itemCount:
            self.items = items
        else:
            raise TypeError(f"Items must be a list and have {itemCount} items!")
        self.inventoryMessage = "Your items:"
        
    def setInventoryMessage(self, message):
        if type(message) is str and len(message) > 0:
            self.inventoryMessage = message
        else:
            raise ValueError("Message must be a string and longer than 0 characters!")

    def decreaseHealth(self, amount):
        if type(amount) is int and amount > -1:
            self.hp -= amount
            if self.hp <= 0:
                self.hp = 0

    def renderInventory(self):
        print("")
        print(self.inventoryMessage)
        nameLength = 0
        atkLength = 0
        defLength = 0

        for item in self.items:
            if len(item.name) > nameLength:
                nameLength = len(item.name)
            if len(str(item.atkpower)) > atkLength:
                atkLength = len(str(item.atkpower))
            if len(str(item.defpower)) > defLength:
                defLength = len(str(item.defpower))

        longestEntry = 0
        entries = []
        for item in self.items:
            nameSpace, atkSpace, defSpace = "", "", ""
            
            if len(item.name) < nameLength:
                for i in range(nameLength - len(item.name)):
                    nameSpace += " "
            
            if len(str(item.atkpower)) < atkLength:
                for i in range(atkLength - len(str(item.atkpower))):
                    atkSpace += " "

            if len(str(item.defpower)) < defLength:
                for i in range(defLength - len(str(item.defpower))):
                    defSpace += " "

            entries.append(f"{self.items.index(item) + 1} {item.name}{nameSpace}  ATK: {item.atkpower}{atkSpace}  DEF: {item.defpower}{defSpace}")
            if len(entries[len(entries)-1]) > longestEntry:
                longestEntry = len(entries[len(entries)-1])
        self.inventoryLongestEntry = longestEntry
        for i in range(longestEntry):
            print("-", end="")
        print("")
        for entry in entries:
            print(entry)

playerObj = player("Player", random.sample(items.db, itemCount))
opponentObj = player("Opponent", random.sample(items.db, itemCount))

currentItem = None
message = None

def results():
    clear()
    global playerObj, opponentObj
    print("--------")
    print("Results:")
    print("")

    if playerObj.hp > opponentObj.hp:
        if opponentObj.hp <= 0:
            print("Your opponent is dead")
        print(f"The player wins with a difference in health of {playerObj.hp - opponentObj.hp} point(s)")

    if opponentObj.hp > playerObj.hp:
        if playerObj.hp <= 0:
            print("You are dead")
        print(f"Your opponent wins with a difference in health of {opponentObj.hp - playerObj.hp} point(s)")

    if playerObj.hp == opponentObj.hp:
        print("Both of you are still alive")
        print("This game is a draw because you have the same amount of health")

    print("")
    input("Press RETURN to continue...")
    playerObj.items = random.sample(items.db, itemCount)
    opponentObj.items = random.sample(items.db, itemCount)
    playerObj.hp = defaultHp
    opponentObj.hp = defaultHp

def play(playerItem):
    global message, playerObj, opponentObj, currentItem

    if playerItem == None:
        message = "You must select an item first"
        return
    if not type(playerItem) is items.item and playerItem != None:
        raise TypeError("playerItem must be of type item!")
    enemyItem = random.choice(opponentObj.items)

    print("")
    print("Battle Result:")
    versusText = f"{playerItem.name} (ATK: {playerItem.atkpower} DEF: {playerItem.defpower}) - VS. - {enemyItem.name} (ATK: {enemyItem.atkpower} DEF: {enemyItem.defpower})"
    for char in versusText:
        print("-", end="")
    print("")
    print(versusText)
    
    messages = []
    damageToPlayer = enemyItem.atkpower - playerItem.defpower
    if damageToPlayer > 0:
        playerObj.decreaseHealth(damageToPlayer)
        msg = f"You take {damageToPlayer} damage from {enemyItem.name}"
        messages.append(msg)

    damageToEnemy = playerItem.atkpower - enemyItem.defpower
    if damageToEnemy > 0:
        opponentObj.decreaseHealth(damageToEnemy)
        msg = f"You deal {damageToEnemy} damage with your {playerItem.name}"
        messages.append(msg)

    print("")
    playerObj.items.remove(playerItem)
    opponentObj.items.remove(enemyItem)
    currentItem = None

    longestMessage = 0
    for msg in messages:
        if len(msg) > longestMessage:
            longestMessage = len(msg)

    if longestMessage > 0:
        for x in range(longestMessage):
            print("-", end="")
        print("")
        for msg in messages:
            print(msg)
        print("")

    phrases = ["amazing!", "wow!", "that\'s so weird.", "you are evenly matched.", "good luck next time!"]

    if len(messages) == 0:
        msg = f"Nothing happened this round, {random.choice(phrases)}"
        for char in msg:
            print("-", end="")
        print("")
        print(msg)
        print("")

    returnText = "Press RETURN to continue..."
    for char in returnText:
        print("-", end="")
    print("")
    input(returnText)

    if len(playerObj.items) == 0 and len(opponentObj.items) == 0 or playerObj.hp <= 0 or opponentObj.hp <= 0:
        results()
    

while True:
    clear()
    print(""" 
    ____             __   _  __
   / __ \__  _____  / /  | |/ /
  / / / / / / / _ \/ /   |   / 
 / /_/ / /_/ /  __/ /   /   |  
/_____/\__,_/\___/_/   /_/|_|  
                              """)
    
    playerObj.renderInventory()
    print("")
    for i in range(playerObj.inventoryLongestEntry):
        print("-", end="")
    print("")
    if currentItem != None:
        print(f"Equipped item: {currentItem.name}")
    else:
        print("Nothing equipped")

    print(f"Your HP: {playerObj.hp}")
    print(f"Opponent\'s HP: {opponentObj.hp}")
    print("")

    for i in range(playerObj.inventoryLongestEntry):
        print("-", end="")
    print("")

    print(f"Type 1 ... {itemCount} to select your item for this round,")
    print("type \'play\' when you are ready,")
    print("type \'exit\' to stop")
    if message != None:
        print(message)
    else:
        print("")
    print("")

    command = input("> ")

    if len(command) > 0:
        if command.lower() == "exit":
            clear()
            exit()
        elif command.lower() == "play":
            clear()
            play(currentItem)
        else:
            try:
                int(command)
                if int(command)-1 >= 0 and int(command)-1 < itemCount:
                    currentItem = playerObj.items[int(command)-1]
                    message = None
                else:
                    message = "Provide a valid item number"
                print("")
            except:
                message = "Provide a valid number"
    else:
        message = None
