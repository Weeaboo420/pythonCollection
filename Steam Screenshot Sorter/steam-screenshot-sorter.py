gamesJsonPath = "games.json"
screenshotsFolder = "../"
outputFolder = "../"
unsortedFolder = "../Unsorted Screenshots"

import json
from shutil import move as moveFile
from os import listdir as listFiles, mkdir as makeDir
from os.path import isfile as fileExists, isdir as dirExists

globGameIDs = {}
globUnfoundGameIDs = []
globUnsortedScreenshots = []

def CheckGamesJson(): #Abort if games json file can't be found
    if not fileExists(gamesJsonPath):
        print(f"\nError: json file \"{gamesJsonPath}\" can't be found. Aborting...\n")
        exit()

def CheckScreenshotsFolder(): #Abort if screenshots folder can't be found
    if not dirExists(screenshotsFolder):
        print(f"\nError: uncompressed screenshots folder \"{screenshotsFolder}\" can't be found. Aborting...\n")
        exit()

def MakeGameFolders():
    global globGameIDs
    
    with open(gamesJsonPath) as jsonFile: #Load game IDs json file and parse to dict
        globGameIDs = json.load(jsonFile)    

    for ID in globGameIDs.keys(): #Create folders for each game
        gameName = globGameIDs[ID]
        if not dirExists(f"{outputFolder}/{gameName}"):
            makeDir(f"{outputFolder}/{gameName}")    

def CopyScreenshots(): 
    global globUnfoundGameIDs
    global globUnsortedScreenshots
    
    print("Sorting screenshots... ", end="")
    
    for screenshot in listFiles(screenshotsFolder): #List all screenshots, extract game ID and move to respective folders
        screenshotNameParts = screenshot.split("_")
        screenshotGameID = screenshotNameParts[0]
        
        gameName = -1
        for ID in globGameIDs.keys(): #Check if the the screenshot's game ID matches the json file's IDs
            if screenshotGameID == ID:
                gameName = globGameIDs[ID]
                break
        
        if gameName == -1: #Add unfound game ID to list for display later
            if screenshotGameID.isdigit(): #Only add integer-based IDs
                globUnfoundGameIDs.append(screenshotGameID)
                globUnsortedScreenshots.append(screenshot)
        
        if gameName != -1: #Only copy screenshots for recognized games
            if not dirExists(f"{outputFolder}/{gameName}"):
                makeDir(f"{outputFolder}/{gameName}")
            
            if not fileExists(f"{outputFolder}/{gameName}/{screenshot}"): #Don't overwrite existing screenshots
                moveFile(f"{screenshotsFolder}/{screenshot}", f"{outputFolder}/{gameName}/{screenshot}")               

    print("Done")

def DisplayWarningUnfoundGameIDs():
    global globUnfoundGameIDs
    global globUnsortedScreenshots
    
    if len(globUnfoundGameIDs) > 0:
        if not dirExists (unsortedFolder): #Create "Unsorted" folder if doesn't exist already
            makeDir(unsortedFolder)
        
        print(f"Unfound game ID(s):\n")
        globUnfoundGameIDs = list(dict.fromkeys(globUnfoundGameIDs)) #Remove duplicate unfound game IDs
        
        for ID in globUnfoundGameIDs:
            print(ID)
        print(f"\nMoving unsorted screenshots to \"{unsortedFolder}\"... ", end="")
        
        for screenshot in globUnsortedScreenshots: #Move unsorted screenshots to their own folder
            if fileExists(f"{screenshotsFolder}/{screenshot}"):
                if dirExists(unsortedFolder):
                    moveFile(f"{screenshotsFolder}/{screenshot}", f"{unsortedFolder}/{screenshot}")
        
        print("Done")
        input("Press RETURN to close this prompt... ")

#Program start
print("Steam Screenshot Sorter\n")
CheckGamesJson()
CheckScreenshotsFolder()
MakeGameFolders()
CopyScreenshots()
DisplayWarningUnfoundGameIDs()