from queue import *
# from numpy import *
from copy import deepcopy

def solve_puzzle_helper(Board, nextCheck, Destination, globMin, visited, origPath, result, pathVar, Source,dictAttempt):
    if len(visited) == 1:
        if Source == Destination:
            dictAttempt[len(visited)] = visited
            return
        else:
            nextCheck.pop(0)

    elif nextCheck[0] != Source:
        pathVar = nextCheck.pop(0)

        if Destination == pathVar:
            # min() checks the first element in the set, what is returned after a cursive calls/base case
            # comparisons happen in the recursive case

            # pass it into the dictionary as a keypair, returned the dictionary value with matching key at the end
            if Destination not in visited:
                visited.append(Destination)

            dictAttempt[len(visited)] = visited
            return len(visited)

        elif Destination != pathVar:
            test = pathFinder(pathVar, Board, visited)

            if test == False:
                dictAttempt[9000] = []
                return

    # direction array holds information,leading with the value/len(path) for comparison and min(). all directions.
    directionArray = []

    staticVar = deepcopy(pathVar)
    # necessary to use, maintains directional visited path-we make a deep copy of this for every direction
    staticArr = deepcopy(visited)

    pathVar = pathFinder(pathVar, Board, visited)
    # visited as for the pathfinder loop
    # newVisited is for passing everything in, for a cursive calls for each respective new cell
    while pathVar != False:
        if pathVar != Source:
            # pathfinders populates direction array for min() & recursive calls

            # holds all information for individual direction, built in each loop
            actualDirection = []

            # visited is for pathfinder
            if pathVar not in visited:
                visited.append(pathVar)

            # updating values to be added into sets
            newVisited = deepcopy(staticArr)

            if staticVar not in newVisited:
                newVisited.append(staticVar)

            if pathVar not in newVisited:
                # recursive calls require this
                newVisited.append(pathVar)

            nextCheck.append(pathVar)

            # [0] is the path variable, what is to be explored,next cell/////!!!!!!!!!!deliteeliteeliteeliteelite
            # actualDirection.append(pathVar)

            # [0] is the you visited list, actual record of path taken0
            actualDirection.append(newVisited)

            # [1] is the new path queue
            nextCheckDeep = deepcopy(nextCheck)
            actualDirection.append(nextCheckDeep)
            nextCheck.pop(0)

            # gathering iall variables of interest for direction into one list
            directionArray.append(actualDirection)

        pathVar = pathFinder(staticVar, Board, visited)
    while len(directionArray) != 4:
        # populate so we can look in all for directions
        actualDirection = []

        # updating temporary visited list, visited list[0]
        actualDirection.append([(-1, -1), (-1, -1), (-1, -1)])

        # updating temporary queue, new path Queue[1]
        actualDirection.append([(-1, -1)])

        # update directionArray
        directionArray.append(actualDirection)

    # using recursion and minimum function, feeding in different coordinate directions into recursion calls

    # directionArray[#][2] -> tempQuetempVisitue
    # directionArray[#][1] ->  list
    solve_puzzle_helper(Board, directionArray[0][1], Destination, globMin, directionArray[0][0], origPath, result,
                        pathVar, Source,dictAttempt),
    solve_puzzle_helper(Board, directionArray[1][1], Destination, globMin, directionArray[1][0], origPath, result,
                        pathVar, Source,dictAttempt),
    solve_puzzle_helper(Board, directionArray[2][1], Destination, globMin, directionArray[2][0], origPath, result,
                        pathVar, Source,dictAttempt),
    solve_puzzle_helper(Board, directionArray[3][1], Destination, globMin, directionArray[3][0], origPath, result,
                        pathVar, Source,dictAttempt)
    # directionArray

    return result


def solve_puzzle(Board, Source, Destination):
    # map the board
    # graph = Board
    print(Board)
    print(Source)
    print(Destination)

    # for initial comparisons at base cases
    intermediate = 0
    # for each individual recursion path
    visited = []
    # global do not visit list
    globVisit = []
    # ridiculously large number for comparison
    globMin = 9999999999

    origPath = []
    # queue for exploration, each recursion gets their own *!!!!!!!!!! import!!!!!!!!!!
    nextCheck = []
    # what's getting past to the helper and then late recursive function
    nextCheck.append(Source)
    # updating visited for the recursive calls to come
    visited.append(Source)
    result = None
    pathVar = Source

    dictAttempt = dict()

    if nextCheck[0] != Source:
        return []

    solve_puzzle_helper(Board, nextCheck, Destination, globMin, visited, origPath, result, pathVar, Source,dictAttempt)
    #print(dictAttempt)
    # min() all the keys, and return the least
    # list comprehensive to get the minimum key
    result = min([x for x in dictAttempt.keys()])
    result = dictAttempt[result]
    
    if result == []:
        result = None
    return result

def pathFinder(cell, Board, visited):
    # returns an unvisited direction
    # a loop to go over all possible directions
    directions = []
    
    # math to get the directions right, and then to add it to possibilities
    up = (cell[0] - 1, cell[1])
    down = (cell[0] + 1, cell[1])
    left = (cell[0], cell[1] - 1)
    right = (cell[0], cell[1] + 1)
    directions.append(right)
    directions.append(left)
    directions.append(up)
    directions.append(down)
    
    for direction in directions:
        # for loop to check what directions are available,and return direction
        if (direction[0]) >= 0:
            if (direction[1]) >= 0:
                if direction[0] <= (len(Board) - 1):
                    if direction[1] <= (len(Board[0]) - 1):
                        # salt issue or I had to replace direct indexing, needed variable
                        row = direction[0]
                        column = direction[1]
                        if Board[row][column] != '#':
                            if direction not in visited:
                                return direction
    return False

Puzzle = [['-', '-', '-'],
          ['-', '-', '-'],
          ['-', '-', '-'],
          ['-', '-', '-']]

print(solve_puzzle(Puzzle, (0, 2),(3, 0)))
