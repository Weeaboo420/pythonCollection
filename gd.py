#!/usr/bin/env python3
import json
from sys import argv as args
from urllib.request import urlopen
version = "1.4"
build_date = "Dec 10 2020"
usage = "Usage: gd <command> OR gd <word> <options>,\nuse \'--help\' to show available commands\n"

if len(args) >= 2:

    #Show patch notes
    if args[1].lower() == "--patch-notes":
        patch_notes = ["* Fixed support for spaces in search queries."]

        print(f"\nNew in gd version {version} ({build_date}):")
        for note in patch_notes:
            print(note)
        print("")

    #Show help information, meaning all available commands and options
    elif args[1].lower() == "--help":
        help_info = [
        "--all [option]\nShow ALL definitions for a search result",
        "--help [command]\nShow a detailed and comprehensive list of commands and options that one can use with gd",
        "--patch-notes [command]\nShow a brief list of additions and changes made since the last version of gd"
        ]
        
        print("\nShowing all available commands and options:\n")
        for entry in help_info:
            
            indent = True
            for char in entry:    

                space = ""
                if indent:
                    space = "  "
                print(f"{space}{char}", end="")

                if char == "\n":
                    indent = True
                else:
                    indent = False
            print("\n")
    else:

        #Allow for words or phrases containing spaces. The API
        #Doesn't seem to have any entries for words or phrases with spaces
        #in them so this feature might get removed in the future.
        word = ""

        for i in range(1, len(args)):
            if "--" not in args[i]:
                word += f"{args[i]} "

        word = word.rstrip() #Remove trailing whitespace
        word = word.lstrip() #Remove leading whitespace

        showAll = False
        allMessage = "" #Message that will change the default "Looking up <word>" into "Looking up ALL DEFINITIONS FOR <word>"
        if "--all" in args: #Enable the display of ALL definitions
            showAll = True
            allMessage = "all definitions for "


        #Make sure that the word isn't empty
        if len(word) > 0:
            print(f"\nLooking up {allMessage}\'{word}\'...")

            #Convert space characters into characters that can be read properly as a URL
            parsedWord = ""
            for char in word:
                if char == " ":
                    parsedWord += "%20" #Add %20 instead of a space
                else:
                    parsedWord += char

            word = parsedWord #Assign the data in parsedWord to word

            try:
                #Get the raw JSON data from the API
                data = json.loads(urlopen(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").read())

                #Load single definition
                if not showAll:
                    print("\nDefinition: ", end="")
                    print(data[0].get("meanings")[0].get("definitions")[0].get("definition"))

                    #Load example. Check if there is an example available or not and show a message accordingly...
                    example = data[0].get("meanings")[0].get("definitions")[0].get("example")
                    if example:
                        print(f"Example: {example}\n")
                    else:
                        print("No example found\n")

                #Load ALL definitions
                else:
                    print("\nDefinitions:\n")
                    definitions = data[0].get("meanings")
                
                    for entry in definitions:
                        #Load definitions and examples
                        definition = entry.get("definitions")[0].get("definition")
                        example = entry.get("definitions")[0].get("example")
                    
                        #If no example is present then we will simply say that there is no example available for that particular definition
                        if not example:
                            example = "No example found"
                    
                        #If there is an example then we insert the text "example" before it
                        else:
                            example = f"Example: {example}"

                        print(f"{definition}\n{example}\n")

            #If a definition isn't found then tell the user
            except Exception as e:
                print(f"No definition found\n")

        #If the word is empty but an option has been specified then there is nothing to search for. Show usage instructions instead.
        else:
            print(f"\n{usage}")

else:
    #Show some info about this program and how to use it
    print(f"\n[v{version} - {build_date}, Python v3.8.5]")
    print("gd - Unofficial Google Dictionary, based on https://dictionaryapi.dev/\ngd written by Weeaboo420, use \'--patch-notes\' for additional information\n")
    print(f"{usage}")
