# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    dfsFringe = util.Stack()
    start = (problem.getStartState(), [], 0)
    dfsFringe.push(start)
    visited = set()

    while not (dfsFringe.isEmpty()):
        # pop the most recent state in our stack so we can traverse it
        iterNode, currPath, cost = dfsFringe.pop()

        # if the popped node is the goal simply return the node's path
        if (problem.isGoalState(iterNode)):
            return currPath

        # if our iterNode has not been visited we append to visited and push successor of iterNode
        if iterNode not in visited:
            visited.add(iterNode)
            for successor, action, stepCost in problem.getSuccessors(iterNode):
                if successor not in visited:
                    dfsFringe.push((successor, currPath + [action], stepCost))

    return []




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"

    # BFS is exactly the same as DFS except we use a Queue (LIFO) instead of a Stack (FIFO)
    bfsFringe = util.Queue()
    start = (problem.getStartState(), [], 0)
    bfsFringe.push(start)
    visited = set()

    while not (bfsFringe.isEmpty()):
        # pop the most recent state in our stack so we can traverse it
        iterNode, currPath, cost = bfsFringe.pop()

        # if the popped node is the goal simply return the node's path
        if (problem.isGoalState(iterNode)):
            return currPath

        # if our iterNode has not been visited we append to visited and push successor of iterNode
        if iterNode not in visited:
            visited.add(iterNode)
            for successor, action, stepCost in problem.getSuccessors(iterNode):
                if successor not in visited:
                    bfsFringe.push((successor, currPath + [action], stepCost))

    return []

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    ucsFringe = util.PriorityQueue()
    current = (problem.getStartState(), [], 0)
    ucsFringe.push(current, 0)
    visited = set()


    # while the problem is not solved we iterate
    while not (ucsFringe.isEmpty()):

        # pop the most recent state in our stack so we can traverse it
        iterNode, currPath, cost = ucsFringe.pop()

        # check to see if we have arrived at the goal state
        if (problem.isGoalState(iterNode)):
            return currPath

        # if we have not visited iterNode we append it to visited set and add iterNode's children to our fringe
        if iterNode not in visited:
            visited.add(iterNode)

            for successor, action, stepCost in problem.getSuccessors(iterNode):
                if successor not in visited:
                    toPush = (successor, currPath + [action], cost + stepCost)
                    priority = cost + stepCost
                    ucsFringe.push(toPush, priority)

    # no path leads us to goal state so we return an empty array 
    return []


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # basically the same thing as uniform cost search, but we sum up the heurestic with the cost for our priority queue
    aStarFringe = util.PriorityQueue()
    current = (problem.getStartState(), [], 0)
    aStarFringe.push(current, 0)
    visited = set()

    while not (aStarFringe.isEmpty()):
        # pop the most recent state in our stack so we can traverse it
        iterNode, currPath, cost = aStarFringe.pop()
        
        if (problem.isGoalState(iterNode)):
            return currPath

        if iterNode not in visited:
            visited.add(iterNode)

            for successor, action, stepCost in problem.getSuccessors(iterNode):
                if successor not in visited:
                    toPush = (successor, currPath + [action], cost + stepCost)
                    # this is the only line that is logically different, we add our heurestic to our costs
                    priority = cost + stepCost + heuristic(successor, problem) 
                    aStarFringe.push(toPush, priority)
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
