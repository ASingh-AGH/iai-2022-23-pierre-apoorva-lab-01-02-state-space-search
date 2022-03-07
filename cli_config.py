import re
from typing import Dict, List, Set, cast
from base.problem import Problem, ReversibleProblem
from base.heuristic import Heuristic
from base.solver import Solver
from problems.blocks_world.blocks_world_heuristic import BlocksWorldNaiveHeuristic
from problems.blocks_world.blocks_world_problem import BlocksWorldProblem

from problems.n_puzzle.n_puzzle_problem import NPuzzleProblem
from problems.n_puzzle.heuristics.n_puzzle_manhattan_heuristic import NPuzzleManhattanHeuristic
from problems.n_puzzle.heuristics.n_puzzle_tiles_out_of_place_heuristic import NPuzzleTilesOutOfPlaceHeuristic

from problems.grid_pathfinding.grid_pathfinding import GridPathfinding
from problems.grid_pathfinding.heuristics.manhattan_heuristic import GridManhattanHeuristic
from problems.grid_pathfinding.heuristics.euclidean_heuristic import GridEuclideanHeuristic
from problems.grid_pathfinding.heuristics.diagonal_heuristic import GridDiagonalHeuristic
from problems.rush_hour.heuristics.indirect_heuristic import RushHourIndirectHeuristic
from problems.rush_hour.rush_hour import RushHourProblem
from problems.rush_hour.heuristics.blocking_cars_heuristic import RushHourBlockingCarsHeuristic
from problems.rush_hour.heuristics.distance_to_exit_heuristic import RushHourDistanceToExitHeuristic
from problems.pancake.pancake_problem import PancakeProblem
from problems.pancake.heuristics.gap_heuristic import PancakeGapHeuristic
from problems.pancake.heuristics.largest_pancake_heuristic import PancakeLargestPancakeHeuristic

from solvers import BFS, DFSIter, DFSRecursive, Dijkstra, Greedy, AStar
from solvers.new_bidrectional_astar import NBAstar


VERSION = "0.42.1 — Lazy Leviathan"


def snake_to_camel(snake: str) -> str:
    return ''.join(x.title() for x in snake.split('_'))


def camel_to_snake(camel: str, useless_suffix: str = '') -> str:
    useful_camel = camel.removesuffix(useless_suffix)
    return re.sub(r'(?<!^)(?=[A-Z])', '_', useful_camel).lower()


problem_heuristics: Dict[type[Problem], Set[type[Heuristic]]] = {
    GridPathfinding: {GridEuclideanHeuristic, GridDiagonalHeuristic, GridManhattanHeuristic},
    NPuzzleProblem: {NPuzzleTilesOutOfPlaceHeuristic, NPuzzleManhattanHeuristic},
    RushHourProblem: {RushHourDistanceToExitHeuristic, RushHourBlockingCarsHeuristic, RushHourIndirectHeuristic},
    BlocksWorldProblem: {BlocksWorldNaiveHeuristic},
    PancakeProblem: {PancakeGapHeuristic, PancakeLargestPancakeHeuristic}
}

avl_problems: Dict[str, type[Problem]] = {camel_to_snake(p.__name__, "Problem"): cast(type[Problem], p) for p in [
    GridPathfinding, NPuzzleProblem, RushHourProblem, BlocksWorldProblem, PancakeProblem]}
avl_algos: Dict[str, type[Solver]] = {a.__name__.lower(): cast(type[Solver], a) for a in [
    DFSRecursive, DFSIter, BFS, Dijkstra, Greedy, AStar, NBAstar]}

all_heuristics: List[type[Heuristic]] = list(set.union(*problem_heuristics.values()))
avl_heuristics: Dict[str, type[Heuristic]] = {camel_to_snake(h.__name__, "Heuristic"): cast(type[Heuristic], h)
                                              for h in all_heuristics}
avl_reversible_problems: list[str] = [ problem_name for problem_name, problem_class in avl_problems.items()
                                       if issubclass(problem_class, ReversibleProblem)]                                               
