from astar import astar

class Evaluate:
    def __init__(self, problem):
        self.problem = problem
        self.ser = astar(self.problem)
        self.debug = False
        
        self.total_a_star_calls = 0
        self.real_a_star_calls = 0
        self.total_evaluations = 0
        self.real_evaluations = 0
        
        self.cache = {}

    def evaluate(self, selected):
        self.total_evaluations += 1

        selected_key = tuple(selected)

        if selected_key in self.cache:
            if self.debug:
                print(f"Cache hit for configuration: {selected_key}")
            return self.cache[selected_key]

        self.real_evaluations += 1

        selected_states = [cand.intersection for cand, bit in zip(self.problem.candidates, selected) if bit == 1]

        total_weighted_distance = 0
        total_population = 0

        for candidate in self.problem.candidates:
            candidate_state = candidate.intersection
            population = candidate.population
            total_population += population

            if candidate_state in selected_states:
                min_distance = 0
            else:
                min_distance = float('inf')
                for station_state in selected_states:
                    self.total_a_star_calls += 1
                    result = self.ser.cached_a_star(candidate_state, station_state)

                    if result is None:
                        distance = float('inf')
                    else:
                        self.real_a_star_calls += 1
                        distance = result[4]

                    min_distance = min(min_distance, distance)

            if min_distance == float('inf'):
                min_distance = 100000000000000000

            total_weighted_distance += min_distance * population

        if total_population == 0:
            print("Error: Total population is zero. Returning infinity.")
            return float('inf')

        result = total_weighted_distance / total_population
        self.cache[selected_key] = result

        if self.debug:
            print(f"Total evaluations: {self.total_evaluations}")
            print(f"Real evaluations: {self.real_evaluations}")

        return result
