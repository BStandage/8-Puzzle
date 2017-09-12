#!/usr/bin/python

# 8-Puzzle Solver
# Created by: Brian Standage
# Created on: 8/30/17
# Last modified by: Brian Standage
# Last modified on: 9/11/17


from random import shuffle
import copy


# Generates and returns a state based on the given arguments
# Insures that if the user makes a state with " " as a blank
# instead of "", the program will still execute properly (temporary fix)
# *(in process of streamlining the process to convert any coordinate with a value of " " to "")*
def makeState(nw, n, ne, w, c, e, sw, s, se):
    if(nw == " "): nw = ""
    elif(n == " "): n = ""
    elif(ne == " "): ne = ""
    elif(w == " "): w = ""
    elif(c == " "): c = ""
    elif(e == " "): e = ""
    elif(sw == " "): sw = ""
    elif(s == " "): s = ""
    elif(se == " "): se = ""
           
    return [[nw, n, ne],
            [w, c, e],
            [sw, s, se]]

# Creates a new node
def makeNode(state, parent, operator, depth, pathCost):
    return Node(state, parent, operator, depth, pathCost)

# Expands all the nodes and filters out the paths that do not have a solution
def expand_node(node, nodes):
    expanded_nodes = []
    expanded_nodes.append(makeNode(moveUp(node.state, getBlankX(node.state), getBlankY(node.state)), node, "u", node.depth + 1, 0))
    expanded_nodes.append(makeNode(moveDown(node.state, getBlankX(node.state), getBlankY(node.state)), node, "d", node.depth + 1, 0))
    expanded_nodes.append(makeNode(moveLeft(node.state, getBlankX(node.state), getBlankY(node.state)), node, "l", node.depth + 1, 0))
    expanded_nodes.append(makeNode(moveRight(node.state, getBlankX(node.state), getBlankY(node.state)), node, "r", node.depth + 1, 0))

    expanded_nodes = [node for node in expanded_nodes if(node.state != None)]
    return expanded_nodes


# Shifts the blank square left
def moveLeft(state, posx, posy):
    global board
    if(onBoard(posy - 1, posx)):
        new_state = copy.deepcopy(state)
        new_state[posx][posy] = state[posx][posy - 1]
        new_state[posx][posy - 1] = ""
        return new_state

# Shifts the blank square right
def moveRight(state, posx, posy):
    global board
    if(onBoard(posy + 1, posx)):
        new_state = copy.deepcopy(state)
        new_state[posx][posy] = state[posx][posy + 1]
        new_state[posx][posy + 1] = ""
        return new_state

# Shifts the blank square up
def moveUp(state, posx, posy):
    global board
    if(onBoard(posy, posx - 1)):
        new_state = copy.deepcopy(state)
        new_state[posx][posy] = state[posx - 1][posy]
        new_state[posx - 1][posy] = ""
        return new_state

# Shifts the blank square down
def moveDown(state, posx, posy):
    global board
    if(onBoard(posy, posx + 1)):
        new_state = copy.deepcopy(state)
        new_state[posx][posy] = state[posx + 1][posy]
        new_state[posx + 1][posy] = ""
        return new_state
    
# Determines if a location is on the board
def onBoard(posx, posy):
    if(posx < 0 or posx > 2 or posy < 0 or posy > 2):
        return False
    else:
        return True


# Creates a list of all the possible moves 
def possibleMoves(state):
    possible = []
    blankX = getBlankX(state)
    blankY = getBlankY(state)

    if(blankX < 2):
        possible.append('down')
    if(blankX > 0):
        possible.append('up')
    if(blankY < 2):
        possible.append('right')
    if(blankY > 0):
        possible.append('left')
    return possible
    

# Returns the x coordinate of the blank position
def getBlankX(state):
    for i, x in enumerate(state):
        if "" in x:
            return(i)

# Returns the y coordinate of the blank position
def getBlankY(state):
    for i, x in enumerate(state):
        if "" in x:
            return (x.index(""))


# Breadth first search from start to goal
def bfs(start, goal):
    nodes = []
    
    nodes.append(makeNode(start, None, None, 0, 0))

    while(True):
        if (len(nodes) == 0):
            return None
        node = nodes.pop(0)

        if (node.state == goal):
            moves = []
            temp = node
            while (True):
                 moves.insert(0, temp.operator)
                 if (temp.depth == 1):
                     break
                 temp = temp.parent

            return moves
        
        nodes.extend(expand_node(node, nodes))

# Calculates how far each tile is from its goal state, and sums those distances *(not used yet)*
def distanceHeuristic(matrix, goal):
    sum = 0
    for i in range(0, len(goal)):
        for j in range(0, len(goal)):
            tile = goal[i][j]
            for k in range(0, len(matrix)):
                for l in range(0, len(matrix)):
                    if matrix[k][l] == tile:
                        sum += (k - i)*(k - i)+(j - l)*(j - l)
    return sum


# Calculates how many tiles are out of place in terms of the goal state *(not used yet)*
def outOfPlace(state, goal):
    sum = 0
    for i in range(0, len(state)):
        if(sate[i] == goal[i]):
            sum = sum + 1
    return sum


def testUninformedSearch(init, goal, limit):
    result = bfs(init, goal)
    global board
    board = copy.deepcopy(init)
    while(limit >= 0):
        if(result == None):
            print("No solution found to the given puzzle")
            break
        elif(result == [None]):
            print("The starting node was the goal")
            break
        else:       
            print(result)
            print(len(result), "moves")
            print("\nSolution: ")
            displaySolution(result)
            break
        limit = limit - 1
    if(limit < 0):
        print("Limit reached before a solution was found")

# Prints a visual representation of the solution
def displaySolution(result):
    global board
    for row in board:
        print(row)
    print('\n')

    for i in result:
        if(i == 'r'):
            board = copy.deepcopy(moveRight(board, getBlankX(board), getBlankY(board)))
            for row in board:
                print(row)
            print('\n')

        if(i == 'l'):
            board = copy.deepcopy(moveLeft(board, getBlankX(board), getBlankY(board)))
            for row in board:
                print(row)
            print('\n')

        if(i == 'u'):
            board = copy.deepcopy(moveUp(board, getBlankX(board), getBlankY(board)))
            for row in board:
                print(row)
            print('\n')

        if(i == 'd'):
            board = copy.deepcopy(moveDown(board, getBlankX(board), getBlankY(board)))
            for row in board:
                print(row)
            print('\n')



class Node:
    def __init__(self, state, parent, operator, depth, cost):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.depth = depth
        self.cost = cost


if __name__ == "__main__":
    # Simple test to show the desired input and expected output of the program
    initialState = makeState(1, 2, 3, 4, 5, 6, 7, 8, " ")
    goalState = makeState(1, 2, 3, 4, 5, 6, 7, " ", 8)
    testUninformedSearch(initialState, goalState, 200)

