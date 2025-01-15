# searchAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util
from collections import deque 
from game import Agent

##this is example agents 
class LeftTurnAgent(Agent):
  "An agent that turns left at every opportunity"
  
  def getAction(self, state):
    legal = state.getLegalPacmanActions()
    current = state.getPacmanState().configuration.direction
    if current == Directions.STOP: current = Directions.NORTH
    left = Directions.LEFT[current]
    if left in legal: return left
    if current in legal: return current
    if Directions.RIGHT[current] in legal: return Directions.RIGHT[current]
    if Directions.LEFT[left] in legal: return Directions.LEFT[left]
    return Directions.STOP

class GreedyAgent(Agent):
  def __init__(self, evalFn="scoreEvaluation"):
    self.evaluationFunction = util.lookup(evalFn, globals())
    assert self.evaluationFunction != None
        
  def getAction(self, state):
    # Generate candidate actions
    legal = state.getLegalPacmanActions()
    if Directions.STOP in legal: legal.remove(Directions.STOP)
      
    successors = [(state.generateSuccessor(0, action), action) for action in legal] 
    scored = [(self.evaluationFunction(state), action) for state, action in successors]
    bestScore = max(scored)[0]
    bestActions = [pair[1] for pair in scored if pair[0] == bestScore]
    return random.choice(bestActions)


class BFSAgent(Agent):
  """
    Your BFS agent (question 1)
  """
  def __init__(self):
      # deque for staring a path to a goal
      self.path = deque()

  def bfs(self, gameState):
        
    grid = gameState.getWalls() # retrieving the grid for the pacman (environment)
    startState = gameState.getPacmanPosition() # getting the starting position
    finalState = gameState.getFood().asList()[0] # retrieving the food-goal (assuming it is the only goal, not multi) 
    queue = deque() # queue for BFS
    cameFrom = {}  # dictionary to keep track of the parent node (state) for each visited one
    visited = set() # set for marking the visited nodes
    
    print(f"Starting state: {startState}") 
    print(f"Destination (food) state: {finalState}")
        
    # Allowable movements in the agent's environment
    possibleDirections = ['West', 'East', 'North', 'South']
    
    # Projecting all possible direction (dx and dy for each of the 4 cases)
    deltaX = [-1, 1, 0, 0]
    deltaY = [0, 0, 1, -1]

    queue.append(startState) # Adding the startState  
    visited.add(startState) # Marking the startState  

    while len(queue) != 0: # While queue is not empty
      currentState = queue.popleft() 

      for direction in range(len(possibleDirections)): # Going for all possible directions 
        y = currentState[1] + deltaY[direction] 
        x = currentState[0] + deltaX[direction]
                                
        # Verifying and filtering only allowable movements (i.e., array out of bound, lack of obstackles, and already visited nodes)
        if ((0 <= x and x < grid.width) and (0 <= y and y < grid.height) and (grid[x][y] == 0) and ((x,y) not in visited)):
          visited.add((x, y)) # Marking the passed vertex as visited
          queue.append((x, y)) # Adding it to the queue for futher processing 
          cameFrom[(x, y)] = (currentState, possibleDirections[direction]) # Saving the parent node's information for the current one as a pair containing the information for the current state's coordinates, as well as the movement that led to it)

    currentState = finalState 

    while startState is not currentState: # restoring the path to the food

      self.path.appendleft((currentState, cameFrom[currentState][1])) # saving to the path the info about the state, as well as the direction to take to get to it
      currentState = cameFrom[currentState] # updating current state to continue restoring the path
      currentState = currentState[0]

    # Opening the "result.txt" file in write mode and ensure proper file closing and encoding
    with open("result.txt", "w", encoding="utf-8") as file:
      # Define a string format for the coordinates
      coordinate_format = "({0}, {1})\n"
    
      # Writing the starting position to the output file
      start_position = startState
      file.write(coordinate_format.format(*start_position))
  
      # Iterating through the path and writing each position to the output file
      for (x, y) in self.path:
         coordinate = (x, y)
         file.write(coordinate_format.format(*coordinate))
         # Printing the coordinates to the console (optional)
         print(coordinate_format.format(*coordinate), end='')

  def getAction(self, gameState):

    """
      Returns the BFS seracing action using gamestae.getLegalActions()
      
      legal moves can be accessed like below 
      legalMoves = gameState.getLegalActions()
      this method returns current legal moves that pac-man can have in curruent state
      returned results are list, combination of "North","South","West","East","Stop"
      we will not use stop action for this project
     
      Please write code that Pacman traverse map in BFS order. 
      Because Pac-man does not have any information of map, it should move around in order to get 
      information that is needed to reach to the goal.

      Also please print order of x,y cordinate of location that Pac-man first visit in result.txt file with format
      (x,y)
      (x1,y1)
      (x2,y2)
      .
      .
      . 
      (xn,yn)
      note that position that Pac-man starts is considered to be (0,0)
      
      this method is called until Pac-man reaches to goal
      return value should be one of the direction Pac-man can move ('North','South'....)
    """
    '''Code'''

    if not self.path: # if list is empty, run BFS (for multiple targets - FOOD)
      self.bfs(gameState)

    return self.path.popleft()[1] # retrieiving the desired action


class DFSAgent(Agent):
  """
  Your DFS agent (question 1)
  """
  def __init__(self):
      self.path = deque()

  def dfs(self, gameState):
        
    grid = gameState.getWalls() # retrieving the grid for the pacman (environment)
    startState = gameState.getPacmanPosition() # getting the starting position
    finalState = gameState.getFood().asList()[0] # retrieving the food-goal (assuming it is the only goal, not multi) 
    queue = deque() # queue for DFS
    cameFrom = {}  # dictionary to keep track of the parent node (state) for each visited one
    visited = set() # set for marking the visited nodes
    
    print(f"Starting state: {startState}") 
    print(f"Destination (food) state: {finalState}")
        
    # Allowable movements in the agent's environment
    possibleDirections = ['West', 'East', 'North', 'South']
    
    # Projecting all possible direction (dx and dy for each of the 4 cases)
    deltaX = [-1, 1, 0, 0]
    deltaY = [0, 0, 1, -1]

    queue.append(startState) # Adding the startState  
    visited.add(startState) # Marking the startState  

    while len(queue) != 0: # While queue is not empty
      currentState = queue.pop() # !!! This is the critical part of the DFS's implementation, taking advantage of the fact that the nodes are not ordered (numbered), simply by changing the queue data structure to stack allows us to implement DFS. !!! 

      for direction in range(len(possibleDirections)): # Going for all possible directions 
        y = currentState[1] + deltaY[direction] 
        x = currentState[0] + deltaX[direction]
                                
        # Verifying and filtering only allowable movements (i.e., array out of bound, lack of obstackles, and already visited nodes)
        if ((0 <= x and x < grid.width) and (0 <= y and y < grid.height) and (grid[x][y] == 0) and ((x,y) not in visited)):
          visited.add((x, y)) # Marking the passed vertex as visited
          queue.append((x, y)) # Adding it to the queue for futher processing 
          cameFrom[(x, y)] = (currentState, possibleDirections[direction]) # Saving the parent node's information for the current one as a pair containing the information for the current state's coordinates, as well as the movement that led to it)

    currentState = finalState 

    while startState is not currentState: # restoring the path to the food

      self.path.appendleft((currentState, cameFrom[currentState][1])) # saving to the path the info about the state, as well as the direction to take to get to it
      currentState = cameFrom[currentState] # updating current state to continue restoring the path
      currentState = currentState[0]

    # Opening the "result.txt" file in write mode and ensure proper file closing and encoding
    with open("result.txt", "w", encoding="utf-8") as file:
      # Define a string format for the coordinates
      coordinate_format = "({0}, {1})\n"
    
      # Writing the starting position to the output file
      start_position = startState
      file.write(coordinate_format.format(*start_position))
    
      # Iterating through the path and writing each position to the output file
      for (x, y) in self.path:
         coordinate = (x, y)
         file.write(coordinate_format.format(*coordinate))
         # Printing the coordinates to the console (optional)
         print(coordinate_format.format(*coordinate), end='')

  def getAction(self, gameState):

    """
      Returns the BFS seracing action using gamestae.getLegalActions()
      
      legal moves can be accessed like below 
      legalMoves = gameState.getLegalActions()
      this method returns current legal moves that pac-man can have in curruent state
      returned results are list, combination of "North","South","West","East","Stop"
      we will not use stop action for this project
     
      Please write code that Pacman traverse map in BFS order. 
      Because Pac-man does not have any information of map, it should move around in order to get 
      information that is needed to reach to the goal.

      Also please print order of x,y cordinate of location that Pac-man first visit in result.txt file with format
      (x,y)
      (x1,y1)
      (x2,y2)
      .
      .
      . 
      (xn,yn)
      note that position that Pac-man starts is considered to be (0,0)
      
      this method is called until Pac-man reaches to goal
      return value should be one of the direction Pac-man can move ('North','South'....)
    """
    '''Code'''

    if not self.path: # if list is empty, run DFS (for multiple targets - FOOD)
      self.dfs(gameState)

    return self.path.popleft()[1] # retrieving the desired action