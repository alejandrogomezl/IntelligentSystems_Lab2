class Node:
    def __init__(self, state, parent=None, depth=0, cost=0):
        self.state = state
        self.parent = parent
        self.depth = 0 if parent is None else parent.depth + 1
        self.cost = cost
    
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.state == other.state
        return False
    
    def __hash__(self):
        return hash(self.state)
    
    def __repr__(self):
        return f"Node(state={self.state}, depth={self.depth}, cost={self.cost})"
    
    def expand(self, problem):
        return [Node(next_state, self, self.depth + 1) for next_state in problem.get_successors(self.state)]
    
    def path(self):
        node, path_back = self, []
        while node:
            path_back.append(node.state.identifier)
            node = node.parent
        return list(reversed(path_back))