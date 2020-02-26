import random, sys

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

if len(args) > 1:

	#check for the arg that specifies uppercase or not
	if args[2]:
		try:
			if args[2].lower() == "true":
				capital = True
			else:
				pass
		except:
			pass


	try:
		for temp in range (int(args[1])):
			print(f"{spit(8)}-{spit(4)}-{spit(4)}-{spit(4)}-{spit(12)}")
	except:
		print(f"{spit(8)}-{spit(4)}-{spit(4)}-{spit(4)}-{spit(12)}")

else:
	print(f"{spit(8)}-{spit(4)}-{spit(4)}-{spit(4)}-{spit(12)}")
