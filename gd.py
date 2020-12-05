#!/usr/bin/env python3
import json
from sys import argv as args
from urllib.request import urlopen

if len(args) >= 2:
    print(f"Looking up \'{args[1]}\'...")

    try:
        data = json.loads(urlopen(f"https://api.dictionaryapi.dev/api/v2/entries/en/{args[1]}").read())
        print("\nDefinition: ", end="")
        print(data[0].get("meanings")[0].get("definitions")[0].get("definition"))
        print("Example: ", end="")
        print(data[0].get("meanings")[0].get("definitions")[0].get("example"))
        print("")
    except Exception as e:
        print(f"Could not find a definition for {args[1]}\n")

else:
    print("\n[v1.0 - Dec 05 2020, Python v3.8.5]")
    print("gd - Unofficial Google Dictionary, based on https://dictionaryapi.dev/\ngd written by Weeaboo420\n\n")
    print("Usage: gd <word>\n")
