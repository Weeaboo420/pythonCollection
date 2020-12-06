#!/usr/bin/env python3
from sys import argv as args
factor = 2.2046226218

if len(args) > 1:

    #Attempt to set a specified amount of decimals to display
    decimals = 3
    if len(args) > 2:
        try:
            int(args[2])
            decimals = int(args[2])
        except:
            pass #It fails, then simply ignore it and revert to 3 decimals

    #Attempt to convert the first argument into a mass in lbs that we can then convert to kilograms.
    try:
        float(args[1])

        #If we are supposed to display more than 0 decimals
        if decimals > 0:
            print(f"{round(float(args[1]) / factor, decimals)}kg")

        #If we have set decimals to 0 then we return an int instead because Python is will still return
        #a float even if we use "0" when rounding, so 5 would become 5.0 and so on...
        else: 
            print(f"{round(float(args[1]) / factor)}kg")

    except:
        print("Error")
else:
    print("\n[v1.0 - Dec 06 2020 on Python 3.8.5]\nP2K, \"Pound to Kilogram\" by Weeaboo420\n\n")
    print("Usage: p2k <weight in lbs> <decimal places (optional)>\nSetting decimal places to 0 will round to nearest integer")
