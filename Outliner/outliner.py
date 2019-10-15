import os, sys, statistics as stats
tags = []

#Outliner v1.0
#Copyright Richard Gustafsson
#Release: Oct 15 2019

def spc(i=1337):
	if i != 1337:
		print(i)
	print("")

if os.path.isfile("tags.txt"):
	with open("tags.txt") as file:
		tags = [line.strip() for line in file]
		
	print("Tags loaded:")
	for index in range(0, len(tags)):
		if index == len(tags)-1:
			print(tags[index])
		else:
			print(tags[index], end=", ")
	spc()
	
else:
	print("ERROR: Could not find file tags.txt in this directory")
	print("Make a file called tags.txt and write one tag per line")
	input("Press any key to continue...")
	sys.exit()

def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
		
def separate(file):
	with open(file) as f:
		tempFirstLine = f.readline()
		tempFirstLine = tempFirstLine.split()
		
		#reset the file pointer, otherwise the first row would
		#be ignored since it already has been read with f.readline()
		f.seek(0)
		
		#create a list containing each line, with any whitespace and
		#other weird chars like \n removed
		tempList = []
		for line in f.readlines():
			tempList.append(line.rstrip())
		
		return tempList, len(tempFirstLine)

def makeNumber(i):
	try:
		return int(i)
	except:
		return 0
		
def tryPrint(n):
	try:
		print(f"---{tags[n]}---")
	except:
		print("ERROR: UNKNOWN TAG")

def flattenData(fp):
	spc()
	spc()
	data, dataPerRow = separate(fp)
	
	lineCount = 0
	for line in data:
		lineCount += 1

	
	for i in range(1, dataPerRow+1):
		
		totalSum = 0
		medianList = []
		
		for line in data:
			
			tempLine = line.split()
			#if the list is still in range, continue
			try:
				totalSum += makeNumber(tempLine[i-1])
				medianList.append(makeNumber(tempLine[i-1]))
			except:
				pass
			
			
		#Calculate the average and the median
		avg = totalSum / lineCount
		
		med = stats.median(medianList)
		
		#print the content
		tryPrint(i-1)
		print(f"Sum: {totalSum}, Average: {round(avg, 1)}, Median {med}")
		spc()
	spc()
	print("Ready for another round")

while True:
	filePath = input("Name of data file (with extension)? ")
	if len(filePath) > 0:
		if os.path.isfile(filePath):
			flattenData(filePath)
		else:
			spc("ERROR: Not a file")
	else:
		spc("ERROR: Files must contain at least one character")