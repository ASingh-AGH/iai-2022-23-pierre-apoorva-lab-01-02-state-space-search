from problems.n_puzzle import NPuzzleState

from problems.n_puzzle.heuristics.n_puzzle_abstract_heuristic import NPuzzleAbstractHeuristic


class NPuzzleManhattanHeuristic(NPuzzleAbstractHeuristic):

    def __call__(self, state: NPuzzleState) -> float:
        # TODO:
        # Calculate a manhattan distance between tiles and their expected places
        # The result should be sum of those distances. 
        # tip 1.'state' is the current state, 
        # tip 2. you can use self.positions function to get from it a dictionary:
        #   { tile_number : (x_coordinate, y_coordinate) }
        # tip 3. self.goal_coords contains such a dictionary for the goal state

        # return abs(state.x - self.problem.goal.x) + abs(state.y - self.problem.goal.y)

        curr = self.positions(state)
        ans = 0
        for (ct, cc), (gt, gc) in zip(curr, self.goal_coords):
            ans += abs(curr[ct][0] - self.goal_coords[gt][0]) + abs(curr[ct][1] - self.goal_coords[gt][1])
        
        return ans

        raise NotImplementedError