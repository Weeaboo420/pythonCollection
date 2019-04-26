import random

alts = ["Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King"]
class Card():
    face = ""

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

        if number > 0:
            if int(number) == 11:
                self.face = f"Jack of {suit} (11)"
            elif int(number) == 12:
                self.face = f"Queen of {suit} (12)"
            elif int(number) == 13:
                self.face = f"King of {suit} (13)"
            elif int(number) == 1:
                self.face = f"Ace of {suit} (1)"


            elif int(number) > 1 and int(number) < 11:
                self.face = f"{alts[number-1]} of {suit}"
                #print(number)

        else:
            print("ERROR: Invalid card number!")


suits = ["Clubs", "Hearts", "Diamonds", "Spades"]
deck = []

for s in suits:
    for n in range(1, 14):
        tempCard = Card(s, n)
        deck.append(tempCard)

#for t in suits:
#    print("")
#    print("")
#    print(f"{t}:")
#    print("")
#    for item in deck:
#        if item.suit == t:
#            print(item.face)

#print("")
#print(f"{len(deck)} cards in the deck")

def getScore():
    p = 0
    d = 0

    for element in myCards:
        p += element.number

    for element in dealerCards:
        d += element.number


    return p, d

myCards = []
dealerCards = []

def deal():
    print("")

    for x in range(2):
        r = random.randint(0, len(deck)-1)
        myCards.append(deck[r])
        deck.remove(myCards[x])

    for y in range(2):
        r = random.randint(0, len(deck)-1)
        dealerCards.append(deck[r])
        deck.remove(dealerCards[y])

    myScore, dealerScore = getScore()

    print(f"You (score: {myScore}): ")
    for a in myCards:
        print(a.face)

    print("")

    print(f"Dealer (score: {dealerScore}): ")
    for b in dealerCards:
        print(b.face)

    print("")

deal()
