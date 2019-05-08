import random, os
rounds, max_rounds = 1, 5

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")



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

def set_deck():
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

def round():
    print("")
    global rounds

    if rounds == 1:
            r1 = random.randint(0, len(deck)-1)
            myCards.append(deck[r1])
            deck.remove(myCards[0])

            r2 = random.randint(0, len(deck)-1)
            dealerCards.append(deck[r2])
            deck.remove(dealerCards[0])

    elif rounds > 1:

        score, cpu_score = getScore()
        print(f"Round {rounds}")
        print(f"Your score: {score}")

        c = True
        while c:
            choice = input("Do you want to draw another card from the deck (y/n)? ")
            if len(choice) > 0:
                if choice.lower() == "y":
                        r = random.randint(0, len(deck)-1)
                        myCards.append(deck[r])
                        deck.remove(myCards[len(myCards)-1])
                        c = False
                        print("")

                elif choice.lower() == "n":
                    c = False
                    print("")

                else:
                    pass

            else:
                pass

        #here the cpu will choose to pick a new card or not
        cards = len(dealerCards)
        score_per_card = cpu_score / cards

        #if score_per_card  > cards and cpu_score < 21:
        if cpu_score < (21 - cards):
            #r = random.randint(1, 4)
            #removed random factor
            r = 2

            if r > 1 and r < 4:
                #pick a new card
                random_card = random.randint(0, len(deck)-1)
                dealerCards.append(deck[random_card])
                deck.remove(dealerCards[len(dealerCards)-1])

            else:
                pass
        else:
            pass


    myScore, dealerScore = getScore()
    print(f"-You (score: {myScore})-")
    for a in myCards:
        print(a.face)

    print("")

    print(f"-Dealer (score: hidden)-")
    if len(dealerCards) == 1:
        print("1 Card")
    elif len(dealerCards) > 1:
        print(f"{len(dealerCards)} cards")

    print("")
    input("Press ENTER to continue...")
    rounds += 1
    clear()



def rules():
    print("-Blackjack-")
    print("All players choose if they want to take a card")
    print(f"every round. After {max_rounds} rounds the")
    print("player whose sum is closest to 21 wins.")
    print("")
    print("An ace is worth 1, a Jack is worth 11,")
    print("a Queen is 12 and a King is 13. All cards")
    print("between those cards have their printed value,")
    print("a five is worth five and an eight is worth eight")
    print("and so on...")
    print("")
    input("Press ENTER to play...")
    clear()


#program start
clear()
rules()

def play():
    global rounds
    global myCards
    global dealerCards
    global deck

    deck = []
    rounds = 1
    myCards = []
    dealerCards = []
    set_deck()

    for i in range(max_rounds):
        round()

    myScore, dealerScore = getScore()

    clear()
    print("-Match Result-")
    print("")

    print(f"-You (score: {myScore})-")
    for a in myCards:
        print(a.face)

    for x in range(2):
        print("")

    print(f"-Dealer (score: {dealerScore})-")
    for b in dealerCards:
        print(b.face)


    myFinal = 0
    dealerFinal = 0

    if myScore > 21:
        myFinal = myScore - 21

    elif myScore < 21:
        myFinal = 21 - myScore


    if dealerScore > 21:
        dealerFinal = dealerScore - 21

    elif dealerScore < 21:
        dealerFinal = 21 - dealerScore

    print("")
    if myFinal > dealerFinal:
        print("The CPU Wins!")

    elif myFinal < dealerFinal:
        print("The player wins!")

    elif myFinal == dealerFinal:
        print("The game is a draw!")


run = True
games = 0

while run:

    if games == 0:
        play()
        games += 1
    else:
        print("")
        c = input("Would you like to play again (y/n)? ")

        if len(c) > 0:
            if c.lower() == "y":
                clear()
                play()
                games += 1

            elif c.lower() == "n":
                run = False

            else:
                pass

        else:
            pass
