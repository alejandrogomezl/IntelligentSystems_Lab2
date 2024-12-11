from search import Search
class Evaluate:
    def __init__(self, problem):
        self.problem = problem
        self.ser = Search(self.problem)
        self.debug = False
        self.total_a_star_calls = 0
        self.real_a_star_calls = 0
        self.total_evaluations = 0
        self.real_evaluations = 0
        self.cache = {}

    def evaluate(self, selected):
        selected_key = tuple(selected)

        # Verificar si ya se evaluó esta solución
        if selected_key in self.cache:
            if self.debug: print("Cache hit")
            return self.cache[selected_key]

        self.real_a_star_calls += 1
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
                        distance = result[4]
                    min_distance = min(min_distance, distance)

            # Si no hay camino válido, usar un valor alto
            if min_distance == float('inf'):
                min_distance = 100000000000000000

            total_weighted_distance += min_distance * population

        # Validar población total
        if total_population == 0:
            print("Error: Total population is zero. Returning infinity.")
            return float('inf')

        # Calcular el costo
        result = total_weighted_distance / total_population
        self.cache[selected_key] = result
        return result
