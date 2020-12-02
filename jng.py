from random import randint

vowels = ["a", "i", "u", "e", "o"]

chars = ["a", "i", "u", "e", "o", "ka", "ki", "ku", "ke", "ko", "sa", "shi", "su", "se", "so", "ta", "chi", "tsu", "te", "to", "na", "ni", "nu", "ne", "no", "ha", "hi", "fu", "he", "ho", "ma", "mi", "mu", "me", "mo", "ya", "yu", "yo", "ra", "ri", "ru", "re", "ro", "wa", "wo", "n", "za", "ji", "zu", "ze", "zo", "pa", "pi", "pu", "pe", "po", "ba", "bi", "bu", "be", "bo", "da", "de", "do", "ga", "gi", "gu", "ge", "go"]

print("Japanese Name Generator (JNG) v1.0 by Weeaboo420 [Dec 02 2020 16:30]\n")
print("Usage: [amount of syllables in name] [amount of names (optional)]\nType \'exit\' to stop\n\nExample: \'3 5\' will return 5 names with 3 syllables in each\n\n")

def get_name(syllables):
    name = ""

    for s in range(syllables):
        newSyllable = chars[randint(0, len(chars)-1)]

        #Add double consonants, such as tto, kko, tte and so on...
        if newSyllable[0] not in vowels and len(name) > 0: #If the new syllable doesn't start with a vowel...
            if randint(0, 1) + randint(0, 1) + randint(0, 1) == 3: #12.5% chance for double consonants
                newSyllable = newSyllable[0] + newSyllable

        name += newSyllable

    return name.capitalize()

while True:
    i = input("> ")

    if len(i) > 0:
        if i.lower() == "exit":
            exit()
        else:
            if " " not in i: #If only the first arg was provided, then generate only ONE name with the specified amount of syllables
                try:
                    int(i)
                    print(get_name(int(i)))
                except:
                    pass

            else: #Second mode, generate a specific amount of names with a specific count of syllables for each of them
                try:
                    data = i.split(" ")
                    syllables = int(data[0])
                    amountOfNames = int(data[1])

                    for x in range(amountOfNames):
                        print(get_name(syllables))
                except:
                    pass
