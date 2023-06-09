from base.solver import P
from solvers.utils import Queue
from tree import Node, Tree


class UninformedSearch:
    """
    Type of search, that have access only to problem definition.    
    """

    def __init__(self, problem: P, queue: Queue):
        self.problem = problem
        self.start = problem.initial
        self.frontier = queue
        self.visited = {self.start}
        # using set instead of a dictionary as it was in BestFirstSearch, because in an uninformed you do
        # not have an evalutaion function and as an estimate for cost visit order is used,
        # so nodes once are visited will never have a better cost, so there no need to use more memory and store a dictionary.
        self.root = Node(self.start)
        self.tree = Tree(self.root)

    def solve(self):
        # - if the root node is a goal, just return it
        #   tip. use 'is_goal' method from Problem
        # - push root node to the frontier
        # - pop nodes from the frontier as long as there any
        #   - if popped node is a goal, return it
        #   - otherwise go through all its children (expand method of Tree)
        #       - if child has not been visited (check self.visited set)
        #         * add child to visited
        #         * push child onto frontier
        # - return None if nothing happens
        
        if self.problem.is_goal(self.root.state):
            return self.root
        self.frontier.push(self.root)
        while self.frontier:
            node = self.frontier.pop()
            if self.problem.is_goal(node.state):
                return node
            
            children = self.tree.expand(self.problem, node) 
            for child in children:
                if child.state in self.visited:
                    continue
                self.visited.add(child.state)
                self.frontier.push(child)
        return None
        
        raise NotImplementedError
