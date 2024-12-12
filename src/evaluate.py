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
            if self.debug: print("Cache hit")
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
                min_distance = 100000000000000000
                for station_state in selected_states:
                    self.total_a_star_calls += 1
                    result = self.ser.cached_a_star(candidate_state, station_state)
                    if result is None:
                        distance = 100000000000000000
                    else:
                        distance = result[4]
                        self.real_a_star_calls += 1

                    min_distance = min(min_distance, distance)

            total_weighted_distance += min_distance * population

        result = total_weighted_distance / total_population if total_population > 0 else float('inf')
        self.cache[selected_key] = result
        return result
