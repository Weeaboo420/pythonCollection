from enum import Enum
from helpers import *
import os, sys

class Colors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	RED = '\033[31m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class Room():
	def __init__(self, name, positiveBounds, negativeBounds, objects):
		self.name = name
		self.sustainMessage = ""

		if type(objects) is list:
			if len(objects) > 0:
				self.objects = objects
				for obj in objects:
					if type(obj) is Player:
						obj.SetRoom(self)
			else:
				raise ValueError("ERROR: List Objects cannot be empty!")
		else:
			raise TypeError("ERROR: Objects must be a list!")

		if type(positiveBounds) is tuple:
			if type(positiveBounds[0]) is int and positiveBounds[0] > 0 and type(positiveBounds[1]) is int and positiveBounds[1] > 0:
				self.positiveBounds = positiveBounds
			else:
				raise ValueError(f"Invalid positive bounds for room {self.name}")
		else:
			raise TypeError("ERROR: positiveBounds must be a tuple with a length of 2!")

		if type(negativeBounds) is tuple:
			if type(negativeBounds[0]) is int and negativeBounds[0] < 0 and type(negativeBounds[1]) is int and negativeBounds[1] < 0:
				self.negativeBounds = negativeBounds
			else:
				raise ValueError(f"Invalid negative bounds for room {self.name}")
		else:
			raise TypeError("ERROR: negativeBounds must be a tuple with a length of 2!")

	def CanInteract(self, player):
		if type(player) is Player:
			for obj in self.objects:
				if type(obj) is NPC and obj.position == player.position:
					return True
			return False
		else:
			raise TypeError("ERROR: Argument \'player\' has to be of type \'Player\'")

	def GetNPC(self, player):
		if type(player) is Player:
			for obj in self.objects:
				if type(obj) is NPC and obj.position == player.position:
					return obj
			return None
		else:
			raise TypeError("ERROR: Argument \'player\' has to be of type \'Player\'")

	def IsOccupied(self, pos):
		if type(pos) is tuple:
			if IsValidPos(pos):
				for obj in self.objects:
					if obj.position[0] == pos[0] and obj.position[1] == pos[1] and type(obj) is Wall:
						return True
					else:
						pass
				return False

			else:
				raise ValueError("ERROR: Pos must only contain integers")

		else:
			raise TypeError("ERROR: Pos must be a tuple with a length of 2!")

	def SetSustainMessage(self, msg):
		if type(msg) is str:
			self.sustainMessage = msg
		else:
			raise ValueError("ERROR: Argument \'msg\' has to be of type \'str\'!")

	def SetPlayer(self, player):
		if type(player) is Player:
			self.player = player
		else:
			raise TypeError("ERROR: Argument \'player\' has to be of type \'Player\'!")

	def Render(self, displayLegendBool):
		clear()
		if displayLegendBool == True:
			displayLegend(self)

		print(self.sustainMessage)

		for cell_y in range(self.positiveBounds[1], self.negativeBounds[1] - 1, -1):

			for temp in range(2):
				for cell_x in range(self.negativeBounds[0], self.positiveBounds[0] + 1, 1):
					print(f"     | ", end="")
				print("")

			print(" -- ", end="")
			for cell_x in range(self.negativeBounds[0], self.positiveBounds[0] + 1, 1):
				char_to_print = " *  -- "
				#"[ ] -- "
				for obj in self.objects:
					if obj.position[0] == cell_x and obj.position[1] == cell_y:
						if type(obj) is NPC:
							char_to_print = Colors.OKBLUE +  " N " + Colors.ENDC + " -- "
						elif type(obj) is Player:
							char_to_print = Colors.OKGREEN + " P " + Colors.ENDC + " -- "
						elif type(obj) is Wall:
							char_to_print = Colors.RED + "[ ]" + Colors.ENDC + " -- "
						else:
							char_to_print = " *  -- "

				print(char_to_print, end="")
			print("")

			#Last one for this column
			if cell_y == self.negativeBounds[1]:
				for temp in range(2):
					for cell_x in range(self.negativeBounds[0], self.positiveBounds[0] + 1, 1):
						print(f"     | ", end="")
					print("")

class EntityType(Enum):
	Player = 1
	NPC = 2
	Enemy = 3

class Player():
	def __init__(self, name, position, maxHp, level, attackPower):
		self.entityType = EntityType.Player

		if type(name) is str and len(name) > 0:
			self.name = name
		else:
			raise ValueError("ERROR: Argument in constructor, \'name\' must be of type \'str\' and have a length greater than zero characters")

		if type(position) is tuple and IsValidPos(position):
			self.position = position
		else:
			raise ValueError("ERROR: Argument in constructor, \'position\' must be of type \'tuple\'!")

		if type(maxHp) is int and maxHp > 0:
			self.maxHp = maxHp
			self.currentHp = self.maxHp
		else:
			raise ValueError("ERROR: Argument in constructor, \'maxHp\' must be of type \'integer\'!")

		if type(level) is int and level > 0:
			self.level = level
		else:
			raise ValueError("ERROR: Argument in constructor, \'level\' must be of type \'integer\' and greater than zero!")

		if type(attackPower) is int and attackPower > 0:
			self.attackPower = attackPower + (self.level * 2)
		else:
			raise ValueError("ERROR: Argument in constructor, \'attackPower\' must be of type \'integer\' and be greater than zero!")

	def Hurt(self, dmg):
		if type(dmg) is int:
			if dmg >= 10 and dmg <= self.maxHp and dmg % 10 == 0 and self.currentHp > 0:
				self.currentHp -= dmg
		else:
			raise TypeError("ERROR: Argument \'dmg\' has to be of type \'int\'")

	def SetRoom(self, room):
		if type(room) is Room:
			self.myRoom = room
			self.myRoom.SetPlayer(self)

	def Move(self, pos):
		if self.myRoom:
			if IsValidPos(pos):
				moveLength = 0
				for coordinate in pos:
					moveLength += coordinate
				if moveLength >= 2:
					raise ValueError("ERROR: Cannot move more than 1 unit per turn!")
				elif moveLength == 0:
					raise ValueError("ERROR: Cannot move a distance of 0 units!")

				elif moveLength == 1 or moveLength == (-1):
					if type(self.myRoom) is Room and IsInBounds(self.myRoom.negativeBounds, self.myRoom.positiveBounds, (self.position[0] + pos[0], self.position[1] + pos[1])) and self.myRoom.IsOccupied((self.position[0] + pos[0], self.position[1] + pos[1])) == False:
						self.position = (self.position[0] + pos[0], self.position[1] + pos[1])

						if self.myRoom.CanInteract(self):
							self.myRoom.SetSustainMessage("Possible actions: talk")
						else:
							self.myRoom.SetSustainMessage("")
					else:
						if self.myRoom.IsOccupied((self.position[0] + pos[0], self.position[1] + pos[1])) == True:
							self.myRoom.SetSustainMessage("You cannot move through walls")
				else:
					raise ValueError("ERROR: Cannot move that many units")

			else:
				raise ValueError("ERROR: Position is invalid!")
		else:
			raise ValueError("ERROR: myRoom is not defined on this instance of Player")

class NPC():
	def __init__(self, entityType, name, position, maxHp, level):
		self.entityType = entityType
		self.name = name
		self.position = position
		self.maxHp = maxHp
		self.currentHp = self.maxHp
		self.level = level

	def SetRoom(self, room):
		self.myRoom = room

	def Move(self, pos):
		if self.myRoom:
			if IsValidPos(pos):
				moveLength = 0
				for coordinate in pos:
					moveLength += coordinate
				if moveLength >= 2:
					raise ValueError("ERROR: Cannot move more than 1 unit per turn!")
				elif moveLength == 0:
					raise ValueError("ERROR: Cannot move a distance of 0 units!")
				elif moveLength == 1 or moveLength == (-1):
					if type(self.myRoom) is Room and IsInBounds(self.myRoom.negativeBounds, self.myRoom.positiveBounds, (self.position[0] + pos[0], self.position[1] + pos[1])) and self.myRoom.IsOccupied((self.position[0] + pos[0], self.position[1] + pos[1])) == False:
						self.position = (self.position[0] + pos[0], self.position[1] + pos[1])
					else:
						pass
				else:
					raise ValueError("ERROR: Cannot move that many units")

			else:
				raise ValueError("ERROR: Position is valid!")
		else:
			raise ValueError("ERROR: myRoom is not defined on this instance of Player")

class Wall():
	def __init__(self, position):
		if type(position) is tuple:
			if IsValidPos(position):
				self.position = position
			else:
				raise ValueError("ERROR: Position is not valid!")
		else:
			raise TypeError("ERROR: Position must be a tuple with a length of 2!")
