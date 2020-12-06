#!/usr/bin/env python3
import json
from sys import argv as args
from urllib.request import urlopen
version = 1.2

if len(args) >= 2:

    #Show patch notes
    if args[1].lower() == "--patch-notes":
        patch_notes = ["+ Added message for when there is no example available", "+ Added patch notes system"]

        print(f"\nNew in gd version {version}:")
        for note in patch_notes:
            print(note)
        print("")

    else:

        #Allow for words or phrases containing spaces. The API
        #Doesn't seem to have any entries for words or phrases with spaces
        #in them so this feature might get removed in the future.
        word = ""
        for i in range(1, len(args)):
            if (i+1) < len(args):
                word += f"{args[i]} "
            else:
                word += f"{args[i]}"

        print(f"Looking up \'{word}\'...")

        try:
            #Get the raw JSON data from the API
            data = json.loads(urlopen(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}").read())

            #Load definition
            print("\nDefinition: ", end="")
            print(data[0].get("meanings")[0].get("definitions")[0].get("definition"))

            #Load example. Check if there is an example available or not and show a message accordingly...
            example = data[0].get("meanings")[0].get("definitions")[0].get("example")
            if example:
                print(f"Example: {example}\n")
            else:
                print("No example found\n")

        #If a definition isn't found then tell the user
        except Exception as e:
            print(f"Could not find a definition for \'{word}\'\n")

else:
    #Show some info about this program and how to use it
    print(f"\n[v{version} - Dec 06 2020, Python v3.8.5]")
    print("gd - Unofficial Google Dictionary, based on https://dictionaryapi.dev/\ngd written by Weeaboo420, use \'--patch-notes\' for additional information\n")
    print("Usage: gd <word>\n")
