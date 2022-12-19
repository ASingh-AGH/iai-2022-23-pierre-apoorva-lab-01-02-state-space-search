


from typing import Dict, List
from base.heuristic import Heuristic
from problems.blocks_world.blocks_world_problem import BlocksWorldProblem, BlocksWorldState

class BlocksWorldNaiveHeuristic(Heuristic):

    def __init__(self, problem: BlocksWorldProblem) -> None:
        super().__init__(problem)
        self.expected_columns = self._calculate_expected_columns(problem.goal)
        self.expected_fundaments = self._calculate_expected_fundaments(problem.goal)

    def _calculate_expected_columns(self, goal: BlocksWorldState) -> Dict[str, int]:
        # TODO:
        # return a dict of form:
        # { <block name> : <index of column in the goal state> }
        columns = {
            "1" : "0",
            "2" : "1",
            "3" : "2",
            "4" : "3",
            "5" : "4",
            "6" : "5",
            "7" : "6",
            "8" : "7"
        }
        return columns
        raise NotImplementedError

    def _calculate_expected_fundaments(self, goal: BlocksWorldState) -> Dict[str, List[str]]:
        # TODO:
        # return a dict of form:
        # { <block name> : <list of the blocks below it in the goal state> }


#------------------{
        Dict[str, List[str]]:
            fundaments = {
                "1": [],
                "2": ["1"],
                "3": ["1", "2"],
                "4": [],
                "5": [],
                "6": [],
                "7": ["6"],
                "8": []
            }
        return fundaments

        raise NotImplementedError

    def __call__(self, state: BlocksWorldState) -> int:
        # TODO:
        # - add `1` to the heuristic value per each block placed in an incorrect column
        # - for other blocks, add `2` if their fundament is incorrect 
        # tip. use self.expected_columns and self.expected_fundaments


#------------------{

        heuristic = 0
        for block in state.columns[0]:
            if self.expected_columns[block] != 0:
                heuristic += 1
        for column in state.columns[1:]:
            for block in column:
                fundament = state.fundament[block]
                if fundament is not None and fundament not in self.expected_fundaments[block]:
                    heuristic += 2
        return heuristic

        raise NotImplementedError
#------------------------------}
