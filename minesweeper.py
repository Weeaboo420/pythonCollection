from os import system, name as platform
from random import randint

#GAME SETTINGS
width = 10
height = 10
cursor = (0, height-1)
lives = 3
bombCount = 13
startingBombCount = 0
bombsLeft = 0
run = True

class Tile:
	def __init__(self):
		self.isFlagged = False
		self.isBomb = False
		self.isVisible = False
		self.nearbyBombs = 0

def Clear():
	if platform == "nt":
		system("cls")
	else:
		system("clear")

def Generate():
	data = []
	bombTiles = 0
	global startingBombCount
	global bombsLeft

	#Generate minefield
	for x in range(width):
		data.append([])
		for y in range(height):
			data[x].append(Tile())
			
			if randint(1, 10) >= 8 and bombTiles < bombCount:
				data[x][y].isBomb = True
				bombTiles += 1

	#Calculate nearby bomb count
	for y in range(height-1, -1, -1):
		for x in range(width):
			if not data[x][y].isBomb:
				
				#Check adjacent tiles
				for y2 in range(y+1, y-2, -1):
					for x2 in range(x-1, x+2, 1):
						
						if x2 >= 0 and x2 < width and y2 >= 0 and y2 < height:							
							if data[x2][y2].isBomb:
								data[x][y].nearbyBombs += 1
	
	tilesToClear = randint(7, 21)
	clearedTiles = 0

	while clearedTiles < tilesToClear:
		for y in range(height-1, -1, -1):
			for x in range(width):
				if not data[x][y].isBomb and randint(1, 10+1) > 5 and randint(1, 10+1) > 3:
					data[x][y].isVisible = True
					clearedTiles += 1

	startingBombCount = bombTiles
	bombsLeft = startingBombCount
	return data

def Render(data):
	for y in range(height-1, -1, -1):
		for x in range(width):
			
			cursorLeft = " "
			cursorRight = " "
			if cursor[0] == x and cursor[1] == y:
				cursorLeft = "["
				cursorRight = "]"
			
			tile = data[x][y]
			display = "."

			if tile.isVisible and not tile.isFlagged:
				if tile.isBomb: #Display as bomb
					display = "#"

				elif not tile.isBomb: #Show nearby bombs
					if tile.nearbyBombs > 0:
						display = tile.nearbyBombs
					else:
						display = " "

			elif tile.isFlagged and not tile.isVisible: #Mark as flagged
				display = "+"

			print(f"{cursorLeft}{display}{cursorRight}", end="")
		print("")

def ClampCursor():
	global cursor

	if cursor[0] < 0:
		cursor = (0, cursor[1])
	elif cursor[0] > width-1:
		cursor = (width-1, cursor[1])

	if cursor[1] < 0:
		cursor = (cursor[0], 0)
	elif cursor[1] > height-1:
		cursor = (cursor[0], height-1)

def ReadInput(i):
	global cursor
	global lives
	global bombsLeft

	if len(i) > 0:
		if i.lower() == "exit":
			Clear()
			exit()
		else:
			if i.lower() == "w": #Move up
				cursor = (cursor[0], cursor[1]+1)

			elif i.lower() == "a": #Move left
				cursor = (cursor[0]-1, cursor[1])

			elif i.lower() == "s": #Move down
				cursor = (cursor[0], cursor[1]-1)

			elif i.lower() == "d": #Move right
				cursor = (cursor[0]+1, cursor[1])

			elif i.lower() == "f": #Tile flagging
				tile = board[cursor[0]][cursor[1]]
				if not tile.isVisible:					
					tile.isFlagged = not tile.isFlagged

					if tile.isFlagged and tile.isBomb:
						bombsLeft -= 1
					elif not tile.isFlagged and tile.isBomb:
						bombsLeft += 1

					if bombsLeft == 0:
						Clear()
						Render(board)
						print("\nMission complete - no bombs left")
			
			elif i.lower() == "r": #Tile removal
				tile = board[cursor[0]][cursor[1]]
				if not tile.isFlagged:					
					
					if tile.isBomb and not tile.isVisible: #Remove life if a bomb is revealed
						lives -= 1
						bombsLeft -= 1

						if lives <= 0:
							Clear()
							print("Game Over.")
					
					tile.isVisible = True

			ClampCursor()

def PlayAgainPrompt():
	global lives
	global board
	global cursor
	global run

	choice = input("Would you like to play again (y/n)? ")

	if choice.lower() == "y" or choice.lower() == "yes":
		lives = 3
		board = Generate()
		cursor = (0, height-1)
	elif choice.lower() == "n" or choice.lower() == "no":
		run = False
		Clear()
		exit()

#Game start
board = Generate()

while run:	

	if bombsLeft > 0:
		if lives > 0:
			Clear()
			Render(board)
			print(f"\nControls: WASD + ENTER to move\n\"f\" to flag tile\n\"r\" to remove tile\n\"exit\" to stop\n")
			print(f"Lives left: {lives}")			

			i = input("> ")
			ReadInput(i)
		else:		
			PlayAgainPrompt()
	else:
		PlayAgainPrompt()