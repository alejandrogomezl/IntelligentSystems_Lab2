from collections import deque
import heapq
from node import Node
import time
import geopy.distance
import itertools
import random
from math import radians, sin, cos, sqrt, atan2

class Search:
    def __init__(self, problem):
        self.problem = problem
        self.cache = {}

    # def heuristic(self, state, goal):
    #     current = (state.latitude, state.longitude)
    #     dest = (goal.latitude, goal.longitude)
    #     dist = geopy.distance.distance(current, dest).meters
    #     speed = 120 / 3.6
    #     return dist / speed

    def heuristic(self, state, goal):
        lat1, lon1 = radians(state.latitude), radians(state.longitude)
        lat2, lon2 = radians(goal.latitude), radians(goal.longitude)
        
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        distance = 6373 * c
        speed = 120 / 3.6

        return distance / speed

    # A* Search
    def a_star(self, initial, goal):
        # comparar por heuristica y si empata por nodo mas viejo (Usar el numero de nodo generado)
        start_time = time.perf_counter()
        counter = itertools.count()

        # Initialize the frontier with the start node and its f(n) = g(n) + h(n)
        frontier = []
        start_node = Node(initial)
        g = 0
        h = self.heuristic(start_node.state, goal)
        f = g + h
        heapq.heappush(frontier, (f, next(counter), start_node))

        explored = set()
        nodes_generated = 1
        nodes_explored = 0

        frontier_cost = {start_node.state: f}    # Dictionary to store the f(n) cost of each node in the frontier

        while frontier:
            _, _, node = heapq.heappop(frontier)   # Remove the node with the lowest f(n)
            nodes_explored += 1

            # Check if the current node is the goal
            if node.state == goal:
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children
            for child_state, action in node.state.neighbors:
                # Add to frontier if it's a shorter path to the child
                if child_state not in explored and (child_state not in frontier_cost or node.cost + action.cost() < frontier_cost[child_state]):
                    g = node.cost + action.cost()    # Calculate new g(n) cost
                    h = self.heuristic(child_state, goal)    # Calculate new h(n) cost
                    f = g + h    # Calculate new f(n) cost

                    child_node = Node(child_state, node, action, g)
                    frontier_cost[child_state] = g
                    heapq.heappush(frontier, (f, next(counter), child_node))
                    nodes_generated += 1

        return None
    
    def cached_a_star(self, start, goal):
        if (start, goal) in self.cache:
            if False: print("Cache hit")
            return self.cache[(start, goal)]
        
        cost = self.a_star(start, goal)
        
        self.cache[(start, goal)] = cost
        return cost
