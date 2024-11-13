from state import State

class Problem:
    def __init__(self, initial_state, goal_state, intersections, segments):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.intersections = (intersections)
        self.segments = segments

    def actions(self, state):
        return state.neighbors

    def result(self, state, action):
        return action.destination

    def goal_test(self, state):
        return state == self.goal_state

    def path_cost(self, cost_so_far, state1, action, state2):
        return cost_so_far + action.cost()
    
    def get_initial_state(self):
        return self.initial_state
    
    def is_goal(self, state):
        return state == self.goal_state