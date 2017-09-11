#!/usr/bin/python

# Assignment 1
# Created by: Brian Standage
# Created on: 8/30/17
# Last modified by: Brian Standage
# Last modified on: 9/6/17


# generate a tree. The first shuffeled state rpersents the root node. Available
# moves while avoiding repeats represents the child nodes.


from random import shuffle
import copy

goal = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, ""]]

board = [["", 1, 3],
         [4, 2, 5],
         [7, 8, 6]]

board2 = [["", 1, 3],
         [4, 2, 5],
         [7, 8, 6]]


def makeState(state):
    for row in state:
        print(row)
    print('\n')

def makeNode(state, parent, operator, depth, pathCost):
    return Node(state, parent, operator, depth, pathCost)

def expand_node(node, nodes):
    expanded_nodes = []
    expanded_nodes.append(makeNode(moveUp(node.state, getBlankX(node.state), getBlankY(node.state)), node, "u", node.depth + 1, 0))
    expanded_nodes.append(makeNode(moveDown(node.state, getBlankX(node.state), getBlankY(node.state)), node, "d", node.depth + 1, 0))
    expanded_nodes.append(makeNode(moveLeft(node.state, getBlankX(node.state), getBlankY(node.state)), node, "l", node.depth + 1, 0))
    expanded_nodes.append(makeNode(moveRight(node.state, getBlankX(node.state), getBlankY(node.state)), node, "r", node.depth + 1, 0))

    expanded_nodes = [node for node in expanded_nodes if(node.state != None)]
    return expanded_nodes

def generalSearch(queue, limit, numRuns):
    if queue == []:
        return False
    elif testProcedure(queue[0]):
        outputProcedure(numRuns, queue[0])
    elif limit == 0:
        print ("Limit reached")
    else:
        limit -= 1
        numRuns += 1
        generalSearch(expandProcedure(queue[0],
        queue[1:len(queue)]), limit, numRuns)


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

def main():
    state = copy.deepcopy(board)
    result = bfs(state, goal)

    if(result == None):
        print("No solution found to the given puzzle")
    elif(result == [None]):
        print("The starting node was the goal")
    else:
        
        print(result)
        print(len(result), "moves")
        print("\nSolution: ")
        displaySolution(result)
        

if __name__ == "__main__":
    main()




