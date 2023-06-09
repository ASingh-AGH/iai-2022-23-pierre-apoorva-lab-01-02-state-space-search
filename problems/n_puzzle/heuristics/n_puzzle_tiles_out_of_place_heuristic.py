from problems.n_puzzle import NPuzzleState
from problems.n_puzzle.heuristics.n_puzzle_abstract_heuristic import NPuzzleAbstractHeuristic



class NPuzzleTilesOutOfPlaceHeuristic(NPuzzleAbstractHeuristic):

    def __call__(self, state: NPuzzleState) -> float:
        # Calculate how many tiles are not on their expected positions
        # tip 1.'state' is the current state, 
        # tip 2. you can use self.positions function to get from it a dictionary:
        #   { tile_number : (x_coordinate, y_coordinate) }
        # tip 3. self.goal_coords contains such a dictionary for the goal state 

        count=0

        curr = self.positions(state)
        for i in curr:
            if curr[i] != self.goal_coords[i]:
                count += 1
        return count

        raise NotImplementedError