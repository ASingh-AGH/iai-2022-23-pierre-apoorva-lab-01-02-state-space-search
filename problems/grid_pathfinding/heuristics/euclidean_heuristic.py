from base import Heuristic
from problems.grid_pathfinding.grid_pathfinding import GridPathfinding
from problems.grid_pathfinding.grid import GridCoord
from math import sqrt


class GridEuclideanHeuristic(Heuristic[GridCoord]):
 
    def __init__(self, problem: GridPathfinding):
        self.problem = problem

    def __call__(self, state: GridCoord) -> float:
        # Calculate an euclidean distance:
        # - 'state' is the current state 
        # - 'self.problem.goal' is the goal state
        
        return sqrt((state.x - self.problem.goal.x) ** 2 + (state.y - self.problem.goal.y) ** 2)
        raise NotImplementedError
  
