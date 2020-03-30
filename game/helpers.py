import os
import classes

def clear():
	os.system("cls || clear")

def getHealth(player):
    if type(player) is classes.Player:

        hitPoints = 0

        for ticks in range(0, player.currentHp, 10):
            if ticks % 10 == 0:
                hitPoints += 1

        healthString = ""
        suffix = ""

        if player.currentHp > 0:
            healthString = "["
            for hp in range(0, hitPoints, 1):
                healthString += "="

            if hitPoints < 10:
                for missingHp in range(0, 10 - hitPoints, 1):
                    healthString += " "

            healthString += "]"
            #health = "[==========]" + suffix
        else:
            healthString = "[   DEAD   ]" + suffix

        return classes.Colors.OKGREEN + healthString + classes.Colors.ENDC
    else:
        raise TypeError("ERROR: Argument \'player\' has to be of type \'Player\'!")

def displayLegend(room):
	if type(room) is classes.Room:
		print(f"---[{classes.Colors.WARNING}{room.name}{classes.Colors.ENDC}]---")
		print("")
		print(f"{classes.Colors.OKGREEN}P = Player{classes.Colors.ENDC}, {classes.Colors.OKBLUE}N = NPC{classes.Colors.ENDC}")
		print("[w, a, s, d] + [RETURN] to move")
		print("")
		print(f"HP: {getHealth(room.player)} ({room.player.currentHp})")
		print(f"ATK: {room.player.attackPower}")
		print("")
	else:
		raise TypeError("ERROR: argument \'room\' must be of type Room!")

#Checks if the values in a tuple are integers
def IsValidPos(pos):
	if type(pos[0]) is int and type(pos[1]) is int:
		return True
	else:
		return False

def IsInBounds(negBounds, posBounds, pos):
	if type(negBounds) is tuple and type(posBounds) is tuple and type(pos) is tuple:
		if pos[0] >= negBounds[0] and pos[0] <= posBounds[0] and pos[1] >= negBounds[1] and pos[1] <= posBounds[1] and IsValidPos(pos) and IsValidPos(negBounds) and IsValidPos(posBounds):
			return True
		else:
			return False
	else:
		raise ValueError("All positions provided must be tuples")
