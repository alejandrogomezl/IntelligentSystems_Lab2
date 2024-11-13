from collections import deque
import heapq
from node import Node
import time
import geopy.distance
import itertools

class Search:
    def __init__(self, problem):
        self.problem = problem

    #Breath First Search
    def bfs(self):
        start_time = time.perf_counter()
        frontier = deque([Node(self.problem.get_initial_state())])  # Queue for nodes in frontier (First In Firs Out)
        explored = set()    # Set of explored states
        nodes_generated = 1
        nodes_explored = 0
        
        while frontier:
            node = frontier.popleft()    # Remove the first node from the queue
            nodes_explored += 1        

            # Check if the current node is the goal
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children of the current node
            for child, action in node.state.neighbors:
                # Add child nodes if they are not explored or in the frontier
                if child not in explored and child not in frontier:
                    child = Node(child, node, action, node.cost + action.cost())
                    frontier.append(child)
                    nodes_generated += 1

        return None

    #Depth First Search
    def dfs(self):  
        start_time = time.perf_counter()
        frontier = [Node(self.problem.get_initial_state())] # Stack for nodes in frontier (Last In First Out)
        explored = set()
        nodes_generated = 1
        nodes_explored = 0
        
        while frontier:
            node = frontier.pop()    # Remove the last node from the stack (Last In First Out)
            nodes_explored += 1        

            # Check if the current node is the goal
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children of the current node
            for child, action in node.state.neighbors:
                if child not in explored and child not in frontier:
                    child = Node(child, node, action, node.cost + action.cost())
                    frontier.append(child)
                    nodes_generated += 1

        return None

    
    def heuristic(self, state, goal):
        current = (state.latitude, state.longitude)
        dest = (goal.latitude, goal.longitude)
        dist = geopy.distance.distance(current, dest).meters
        speed = 120 / 3.6
        return dist / speed

    # A* Search
    def a_star(self):
        # comparar por heuristica y si empata por nodo mas viejo (Usar el numero de nodo generado)
        start_time = time.perf_counter()
        counter = itertools.count()

        # Initialize the frontier with the start node and its f(n) = g(n) + h(n)
        frontier = []
        start_node = Node(self.problem.get_initial_state())
        g = 0
        h = self.heuristic(start_node.state, self.problem.goal_state)
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
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children
            for child_state, action in node.state.neighbors:
                # Add to frontier if it's a shorter path to the child
                if child_state not in explored and (child_state not in frontier_cost or node.cost + action.cost() < frontier_cost[child_state]):
                    g = node.cost + action.cost()    # Calculate new g(n) cost
                    h = self.heuristic(child_state, self.problem.goal_state)    # Calculate new h(n) cost
                    f = g + h    # Calculate new f(n) cost

                    child_node = Node(child_state, node, action, g)
                    frontier_cost[child_state] = g
                    heapq.heappush(frontier, (f, next(counter), child_node))
                    nodes_generated += 1

        return None
    
    # Greedy Best First Search
    def best_first(self):
        start_time = time.perf_counter()
        counter = itertools.count()

        # Initialize the frontier with the start node and its f(n) = g(n) + h(n)
        frontier = []
        start_node = Node(self.problem.get_initial_state())
        h = self.heuristic(start_node.state, self.problem.goal_state)
        f = h
        heapq.heappush(frontier, (f, next(counter), start_node))

        explored = set()
        nodes_generated = 1
        nodes_explored = 0

        while frontier:
            _, _, node = heapq.heappop(frontier)   # Remove the node with the lowest f(n)
            nodes_explored += 1

            # Check if the current node is the goal
            if self.problem.is_goal(node.state):
                execution_time = time.perf_counter() - start_time
                return [node.path(), nodes_generated, nodes_explored, node.depth, node.cost, execution_time]

            explored.add(node.state)    # Mark the state as explored

            # Expand children
            for child_state, action in node.state.neighbors:
                # Add to frontier if it's a shorter path to the child
                if child_state not in explored:
                    f = self.heuristic(child_state, self.problem.goal_state)    # Calculate new h(n) cost

                    child_node = Node(child_state, node, action, f)
                    heapq.heappush(frontier, (f, next(counter), child_node))
                    nodes_generated += 1

        return None