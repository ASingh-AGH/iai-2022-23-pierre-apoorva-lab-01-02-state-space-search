from typing import Callable, Optional
from base.problem import Problem
from base.state import State
from solvers.utils import PriorityQueue
from tree import Node, Tree


class BestFirstSearch:
    """
    Type of search that have access to problem definition and to heuristic, that allows it estimate
    which nodes should be searched.
    """

    def __init__(self, problem: Problem, eval_fun: Callable[[Node], float]):
        self.problem = problem
        self.start: State = problem.initial
        self.root = Node(self.start)
        self.frontier: PriorityQueue = PriorityQueue(eval_fun)
        self.visited = {self.start: float(self.root.cost)}
        self.tree = Tree(self.root)

    def solve(self) -> Optional[Node]:
        # TODO:
        # - if the root node is a goal, just return it
        #   tip. use 'is_goal' method from Problem
        # - push root node to the frontier
        # - pop nodes from the frontier as long as there any
        #   - if popped node is a goal, return it
        #   - otherwise go through all its children (expand method of Tree)
        #       - if child has not been visited (check self.visited dictionary)
        #         or its cost is better than the saved one
        #         * update cost in visited
        #         * push child onto frontier
        # - return None if nothing happens
"""
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
                self.visited.update({child.state: child.cost})
                self.frontier.push(child)
        return None

"""
#-----------------------------{
        if self.problem.is_goal(self.root.state):
                return self.root
            
            self.frontier.put(self.root)

            while not self.frontier.empty():
                curr_node = self.frontier.get()
                if self.problem.is_goal(curr_node.state):
                    return curr_node
                
                children = self.tree.expand(curr_node)
                for child in children:
                    if child.state not in self.visited or child.cost < self.visited[child.state]:
                        self.visited[child.state] = child.cost
                        self.frontier.put(child)
#---------------------------------------}
        raise NotImplementedError
