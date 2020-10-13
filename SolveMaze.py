### USER SETTINGS ###
startColor = (66, 75, 245)
endColor = (245, 66, 87)

### INTERNAL SETTINGS - DO NOT MODIFY ###
defaultColors = [(66, 75, 245), (245, 66, 87)]
version = 1.2

try:
    from PIL import Image    
except:
    print("You need to install PIL before using this python program.")
    exit()

try:
    import numpy as np
except:
    print("You need to install Numpy before using this python program.")
    exit()

from os.path import isfile
from time import time

def TupleContainsType(data, expectedType):
    if type(data) is tuple:
        for value in data:
            if type(value) is not expectedType:
                return False
        return True

    else:
        return False

def IsValidColor(color):
    if TupleContainsType(color, int):
        for component in color:
            if component < 0 or component > 255:
                return False

        if len(color) == 3:
            return True

    return False

def ToTuple(arr):
    return (int(arr[0]), int(arr[1]), int(arr[2]))

def FadeColor(color1, color2, percent):
    newColor = np.array(color1) + (np.array(color2) - np.array(color1)) * percent
    return ToTuple(newColor)

def Distance(nodeA, nodeB):
    return ( (nodeA.position[0] - nodeB.position[0]) ** 2 + (nodeA.position[1] - nodeB.position[1]) ** 2 ) ** 0.5

def IsAdjacent(nodeA, nodeB):
    if nodeA.position[0] == nodeB.position[0]:
        if nodeA.position[1] == nodeB.position[1] + 1 or nodeA.position[1] == nodeB.position[1] - 1:
            return True

    elif nodeA.position[1] == nodeB.position[1]:
        if nodeA.position[0] == nodeB.position[0] + 1 or nodeA.position[0] == nodeB.position[0] - 1:
            return True
    
    return False

class Node:
    def __init__(self, position, walkable):
        if type(position) is tuple and len(position) == 2:
            self.position = position
        
        if type(walkable) is bool:
            self.walkable = walkable

        self.distance = float("inf") #Set the node's distance to infinity
        self.parent = None
        self.adjacentNodes = None
        self.pathPercent = 0


def Main(imagePath):
    if not isfile(imagePath):
        print(f"Cannot find file \'{imagePath}\'\n")
        return

    #Each pixel is an rgb tuple, such as (255, 255, 255) for white and (0, 0, 0) for black and so on...
    #We have to consider the possibility of there being an alpha channel, in that case a pixel would be a tuple with four values,
    #like (255, 255, 255, 255).
    rawImageData = [] 
    imageSize = None

    nodes = []

    with Image.open(imagePath) as image:
        rawImageData = list(image.getdata()) #Load the image data into a list of pixels
        imageSize = image.size    

    index = 0
    for y in range(imageSize[1]):
        for x in range(imageSize[0]):

            if rawImageData[index] == (255, 255, 255) or rawImageData[index] == (255, 255, 255, 255):
                nodes.append(Node((x, y), True))
            else:
                nodes.append(Node((x, y), False))

            index += 1

    #Dijkstra's Algorithm stuff
    t1 = time()
    unexplored = nodes.copy()
    print("Calculating...")

    startNode, goalNode = None, None
    for node in nodes:
        if node.walkable and node.position[1] == 0:
            startNode = node            
            startNode.distance = 0
            startNode.pathPercent = 0

        elif node.walkable and node.position[1] == imageSize[1]-1:
            goalNode = node
            goalNode.pathPercent = 1

    finished = False
    foundPath = False

    while finished == False:        

        closestDistance = float("inf")
        currentNode = None

        for node in unexplored:
            if node.walkable:
                if node.distance <= closestDistance:
                    closestDistance = node.distance
                    currentNode = node

        unexplored.remove(currentNode)

        adjacentNodes = []
        for i, node in enumerate(unexplored):

            if node.walkable: #Only look at walkable nodes (nodes that are not walls)
                if IsAdjacent(node, currentNode):
                    adjacentNodes.append((i, node))

        for i, adjacent in adjacentNodes:
            potentialDistance = currentNode.distance + Distance(currentNode, adjacent)
            
            if potentialDistance < adjacent.distance:
                adjacent.distance = potentialDistance
                adjacent.parent = currentNode                

                nodes[i] = adjacent
        
        if len(unexplored) == 0 or goalNode not in unexplored:
            finished = True            
    
    unexplored.clear()
    nodes.clear()

    if goalNode not in unexplored:
        foundPath = True
    
    if foundPath:
        print("\nPath found")
        print(f"Calculation took {round(time() - t1, 4)}s")
        print("Saving output... ", end="", flush=True)

        path = []
        currentNode = None    

        while startNode not in path:
            if len(path) == 0:
                path.append(goalNode)
            else:                        
                path.append(currentNode.parent)
            
            currentNode = path[len(path)-1]
        
        pathPercent = 1
        for node in path:
            if type(node) is Node:
                node.pathPercent = pathPercent
                pathPercent -= (1 / len(path))

        path.reverse() #Reverse the path since it's been loaded in backwards.
        
        #Get a new, unmodified copy of the nodes
        index = 0        
        for y in range(imageSize[1]):
            for x in range(imageSize[0]):

                if rawImageData[index] == (255, 255, 255) or rawImageData[index] == (255, 255, 255, 255):
                    nodes.append(Node((x, y), True))
                else:
                    nodes.append(Node((x, y), False))

                index += 1

        index = 0
        newImageData = []
        for y in range(imageSize[1]):
            for x in range(imageSize[0]):
                
                if nodes[index].walkable:
                    
                    empty = True

                    for pathNode in path:
                        if nodes[index].position == pathNode.position:                        
                            newImageData.append(FadeColor(startColor, endColor, pathNode.pathPercent))
                            empty = False
                            break

                    if empty:                    
                        newImageData.append((255, 255, 255)) #Node that is not part of the path. Has a white color.

                else:                
                    newImageData.append((0, 0, 0)) #Node that is a wall. Has a black color.

                index += 1

        newImage = Image.new("RGB", imageSize)
        newImage.putdata(newImageData)
        newImage = newImage.resize((imageSize[0]*30, imageSize[1]*30), Image.NEAREST)

        newName = "output_" + image.filename

        if isfile(newName):
            print(f"\'{newName}\' already exists. Please choose a new name.")

            dilemma = True
            while dilemma:
                inpt = input("> ")
                if len(inpt) > 0 and not isfile(inpt):                    
                    newImage.save(inpt)
                    print("Done")
                    dilemma = False

        else:            
            newImage.save(newName)
            print("Done")

        print("File saved\n")

    else:
        print("\nCould not calculate a suitable path\n\n")

#Make sure the colors are correct
if not IsValidColor(startColor):
    startColor = defaultColors[0]
if not IsValidColor(endColor):
    endColor = defaultColors[1]

print(f"Weeaboo\'s Maze solver v{version} | Type \'exit\' to cancel\nYou can customize the path colors by editing this file\n")
while True:
    inputBuffer = input("Enter image path: ")

    if len(inputBuffer) > 0:
        if inputBuffer.lower() == "exit":
            exit()
        else:
            try:
                Main(inputBuffer)
            except:
                print("Something went wrong when calculating the path. Make sure the entrances to the maze are at the top and bottom.")
                print("Very large mazes may consume too much memory and then break the program.")