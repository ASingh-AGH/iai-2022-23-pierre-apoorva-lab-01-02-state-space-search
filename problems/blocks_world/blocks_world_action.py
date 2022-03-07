from dataclasses import dataclass, astuple
from problems.blocks_world.blocks_world_state import BlocksWorldState
from copy import deepcopy

@dataclass
class BlocksWorldAction:
    column_from: int
    column_to: int

    def apply(self, state: BlocksWorldState) -> BlocksWorldState:
        # TODO:
        # - create a new state by applying the action
        #   (move block from 'self.column_from' to 'self.column_to')
        # tip. remember to not modify the current state!
        raise NotImplementedError
    
    def __str__(self) -> str:
        return f"move block from col: {self.column_from} to col: {self.column_to}"

    def __hash__(self):
        return hash(astuple(self))
