import random, os

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class person():
        def __init__(self, age, gender, minAge, maxAge):
                self.myGender = gender

                if gender.lower() == "random":
                        gender = random.choice(genders)

                if gender.lower() == "female":
                        self.myName =   random.choice(randomFemaleNames)
                        self.myGender = "Female"
                        
                elif gender.lower() == "male":
                        self.myName = random.choice(randomMaleNames)
                        self.myGender = "Male"

                if age == 0:
                        self.myAge = random.randint(minAge, maxAge)
                elif age > 0:
                        self.myAge = age


genders = ["Male", "Female"]

randomMaleNames = ["James", "Alexander", "Eric", "Matt", "Mattias", "Nolan", "Richard", 
"Duncan", "Peter", "Shaun", "Derrick", "Robert,", "Oliver", "Felix", "Gabriel", "Daniel", "Oscar", "Howard",
"Lucas", "Adam", "Aaron", "Douglas"]

randomFemaleNames = ["Ellen", "Emma", "Elizabeth", "Erica", "Rachel", "Rebecca", "Monica", "Vanessa", "Candace",
"Melissa", "Victoria", "Mia", "Johanna", "Maja", "Jonna", "Josefin", "Anna", "Annie", "Lisa", "Karen"]

def generate(amount, gender, minAge, maxAge):
    for i in range(0, amount):
            newPerson = person(0, gender, minAge, maxAge)
            print(f"{newPerson.myName}, {newPerson.myAge} y/o, {newPerson.myGender}")
    input("Press any key to continue...")
    clear()

while True:
    amount = input("How many people? ")
    if len(amount) > 0:
        try:
            int(amount)
            gender = input("Gender (male/female/random)? ")
            if len(gender) > 0:
                try:
                    int(gender)
                    #this should fail
                except:
                    if gender.lower() == "male" or gender.lower() == "female" or gender.lower() == "random":
                        pass
                    else:
                        gender = "random"
                
                    minAge = input("Minimum age? ")
                    if len(minAge) > 0:
                        try:
                            int(minAge)
                            
                            maxAge = input("Maximum age? ")
                            if len(maxAge) > 0:
                                try:
                                    int(maxAge)
                                    generate(int(amount), gender, int(minAge), int(maxAge))
                                
                                except:
                                    clear()
                            
                            else:
                                clear()
                    
                        except:
                            clear()
                    else:
                        clear()
                
            else:
                clear()
            
        except:
            clear()
    else:
        clear()
