from state import State

class Problem:
    def __init__(self, intersections, segments, candidates, nstations):
        self.intersections = (intersections)
        self.segments = segments
        self.candidates = candidates
        self.nstations = nstations

    def actions(self, state):
        return state.neighbors

    def result(self, state, action):
        return action.destination

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + action.cost()
    
