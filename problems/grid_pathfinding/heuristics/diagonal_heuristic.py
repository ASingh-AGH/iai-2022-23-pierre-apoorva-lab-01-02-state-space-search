from base import Heuristic
from problems.grid_pathfinding.grid_pathfinding import GridPathfinding
from problems.grid_pathfinding.grid import GridCoord


class GridDiagonalHeuristic(Heuristic[GridCoord]):
 
    def __init__(self, problem: GridPathfinding):
        self.problem = problem

    def __call__(self, state: GridCoord) -> float:
        # TODO:
        # Calculate a diagonal distance:
        # - 'state' is the current state 
        # - 'self.problem.goal' is the goal state
        # - 'self.problem.diagonal_weight' is cost of making a diagonal move
        dx=abs(state.x-self.problem.goal.x)
        dy=abs(state.y - self.problem.goal.y)
        return self.problem.diagonal_weight*math.sqrt(dx*dx+dy*dy)
        raise NotImplementedError
