


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
        result = {}
        for column in range(0, len(goal.columns)):
            if goal.columns[column]:
                for block in goal.columns[column]:
                    result.update({block: column})
        return result


    def _calculate_expected_fundaments(self, goal: BlocksWorldState) -> Dict[str, List[str]]:
        # TODO:
        # return a dict of form:
        # { <block name> : <list of the blocks below it in the goal state> }
        result = {}
        for column in goal.columns:
            for block in range(0, len(column)):
                below = column[:block]
                result.update({column[block]: below})
        return result


    def __call__(self, state: BlocksWorldState) -> int:
        # TODO:
        # - add `1` to the heuristic value per each block placed in an incorrect column
        # - for other blocks, add `2` if their fundament is incorrect 
        # tip. use self.expected_columns and self.expected_fundaments
        current_columns = self._calculate_expected_columns(state)
        current_fundaments = self._calculate_expected_fundaments(state)
        columns_difference = 0
        fundaments_difference = 0
        not_needed_blocks = []
        for block in current_columns:
            if current_columns[block] != self.expected_columns[block]:
                columns_difference += 1
                not_needed_blocks.append(block)

        for block in current_fundaments:
            if block in not_needed_blocks:
                continue
            if current_fundaments[block] != self.expected_fundaments[block]:
                fundaments_difference += 1

        return columns_difference + fundaments_difference * 2

