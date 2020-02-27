import random, sys, os

letters = ["a", "b", "c", "d", "e", "f"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
capital = False

#format = xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
#         8,       4,   4,   4,   12

#spits out a random string with the length n,
#uses the lists letters and numbers to generate
#the random string
def spit(n):
	outputString = ""
	for temp in range(n+1):
		randomNumber = random.randint(0, 1)

		#letter
		if randomNumber == 0:
			if(capital == False):
				outputString += random.choice(letters)
			else:
				outputString += random.choice(letters).upper();
		else:
			outputString += random.choice(numbers)

	return outputString


#collect arguments from the cli,
#for example: the user types py guid.py 10,
#the second argument would then be 10 since the
#python file is the first argument in this case
args = sys.argv
print("")

#a variable to store the output filename if it is specified
myFileName = ""


if len(args) > 1:

	#check for the arg that specifies uppercase or not
	try:
		if not os.path.isfile(args[3]):
			myFileName = args[3]
			with open(myFileName, mode="x+") as f:
				f.close()
			#create a file with the specified name
		else:
			print("[ERROR] Invalid file path or the file already exists")
			print("")

	except:
		pass



	try:
		if args[2].lower() == "true":
			capital = True
		else:
			pass
	except:
		pass


	try:
		for temp in range (int(args[1])):
			printedLine = f"{spit(8)}-{spit(4)}-{spit(4)}-{spit(4)}-{spit(12)}"
			print(printedLine)

			if os.path.isfile(myFileName) and myFileName != "":
				with open(myFileName, "a+") as fh:
					fh.write(printedLine + "\n")
					fh.close()

	except:
		print(f"{spit(8)}-{spit(4)}-{spit(4)}-{spit(4)}-{spit(12)}")

else:
	print("Usage: guid [n] [useCaps] [outputFile]")
	print("")
	print("[n | 1 -> infinity] is the amount of guids you wish to create")
	print("[useCaps | true, false] is a bool that forces all letters to be in caps")
	print("[outputFile] is the path to the output file that will be created (*a)")
	print("")

	print("")
	print("Examples:")
	print("guid 10 false --- return 10 guids in lowercase")
	print("guid 3 true --- return 3 guids with uppercase")

	print("")
	print("Legends:")
	print("*a = This program will never overwrite or append to existing files, only create new ones.")
