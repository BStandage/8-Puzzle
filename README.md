# 8-Puzzle
A python program that implements breadth first search to solve an 8-puzzle. 

### Running the Program
Within "if __ name __ == __ main __:" the user must create an initial state and a goal state. 

To find a solution to the 8-puzzle using breadth first search, the user must call the "testUninformedSearch" function and pass it an initial state, goal state, and limit to stop the program if a solution is not found after a certain number of executions. 

A simple example of how to run the program would be as follows:
    
    if __name__ == "__main__":
      initialState = makeState(1, 2, 3, 4, 5, 6, 7, 8, " ")
      goalState = makeState(1, 2, 3, 4, 5, 6, 7, " ", 8)
      testUninformedSearch(initialState, goalState, 200)
    
And a more complex puzzle:     
   
    if __name__ == "__main__":
      initialState = makeState(" ", 1, 3, 4, 2, 5, 7, 8, 6)
      goalState = makeState(1, 2, 3, 4, 5, 6, 7, 8, " ")
      testUninformedSearch(initialState, goalState, 200)

## Complexity

The worst-case time complexity of breadth first search is O(b<sup>d</sup>) given that d is the depth and b is the number of nodes at that depth.

The worst-case space compledity of breadth first search is also O(b<sup>d</sup>)



