from classes import *
from helpers import *
clear()

objects = []
playerName = "Player"

#entities
objects.append(NPC(EntityType.NPC, "Dummy NPC", (1, 1), 50, 4))

#walls
objects.append(Wall((-1, -1)))
objects.append(Wall((-1, 0)))
objects.append(Wall((-1, 1)))
objects.append(Wall((-1, 2)))
objects.append(Wall((0, 2)))
objects.append(Wall((1, 2)))
objects.append(Wall((2, 2)))
objects.append(Wall((3, 2)))
objects.append(Wall((3, 0)))
objects.append(Wall((3, -1)))
objects.append(Wall((2, -1)))
objects.append(Wall((1, -1)))
objects.append(Wall((0, -1)))

objects.append(Wall((7, 3)))
objects.append(Wall((7, 2)))
objects.append(Wall((7, -1)))
objects.append(Wall((7, -2)))

objects.append(Player(playerName, (0, 0), 100, 1, 2))
#Add the player last so that it will be drawn on top of any npc or other entity it shares a cell with

#global player
player = objects[len(objects) - 1]

TestRoom = Room("Test Room", (12, 3), (-3, -2), objects)
#TestRoom.Render(True)


while True:	
	TestRoom.Render(True)
	c = input("> ")		
	if c.lower() == "w":
		player.Move((0, 1))
	if c.lower() == "a":
		player.Move((-1, 0))
	if c.lower() == "s":
		player.Move((0, -1))
	if c.lower() == "d":
		player.Move((1, 0))
	
	if c.lower() == "h":
		player.Hurt(10)

	if c.lower() == "talk":		
		inDialog = player.myRoom.CanInteract(player)
		npc = None
		npcNameTag = ""

		if inDialog == True:
			npc = player.myRoom.GetNPC(player)
			npcNameTag = f"{npc.name} (lvl. {npc.level})"
			clear()
		else:
			player.myRoom.SetSustainMessage("There is nobody there")

		while inDialog == True:			
			print(f"{npcNameTag}: Hello there")
			c2 = input("> ")
			if len(c) > 0:
				if c2.lower() == "bye" or c2.lower() == "goodbye":
					print(f"{npcNameTag}: Goodbye")
					input("Press RETURN to continue...")
					inDialog = False
					player.myRoom.SetSustainMessage("")
					clear()

	if c.lower() == "exit" or c.lower() == "quit" or c.lower() == "stop":
		response = input("Are you sure you want to quit (y/n)? ")
		if len(response) > 0:
			if response.lower() == "yes" or response.lower() == "y":
				clear()
				exit()
			else:
				pass
		else:
			pass	
	
