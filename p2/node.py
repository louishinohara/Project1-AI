# Node: used for search algorithm
class Node():
    def __init__(self, x: int, y: int, prev=None):
        self.x = x
        self.y = y
        self.prev = prev

# aStarNode: used for A* search. Has extra g(n), h(n), f(n) = g(n) + h(n)
class aStarNode(Node):
    def __init__(self, x: int, y: int, g: int, dim: int, prev=None):
        super().__init__(x, y, prev)
        #   Used for heuristics
        self.g = g                              # g = current cost
        self.dim = dim                          # dim used for goal node
        self.f = g + abs(self.x-(self.dim-1)) + abs(self.y-(self.dim-1))  # h(n) is node's Manhattan distance to goal