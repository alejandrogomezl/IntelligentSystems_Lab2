from astar import astar

class Evaluate:
    def __init__(self, problem):
        self.problem = problem
        self.ser = astar(self.problem)
        self.debug = False
        
        # Contadores para estadísticas
        self.total_a_star_calls = 0
        self.real_a_star_calls = 0
        self.total_evaluations = 0  # Evaluaciones totales realizadas
        self.real_evaluations = 0   # Evaluaciones reales realizadas (sin caché)
        
        self.cache = {}

    def evaluate(self, selected):
        """
        Evalúa una solución dada y actualiza las estadísticas de evaluación.

        Parámetro:
        - selected: Lista binaria representando las estaciones seleccionadas (1) y no seleccionadas (0).

        Devuelve:
        - El costo asociado a la solución evaluada.
        """
        self.total_evaluations += 1  # Incrementar el número total de evaluaciones

        selected_key = tuple(selected)

        # Verificar si ya se evaluó esta solución (caché)
        if selected_key in self.cache:
            if self.debug:
                print(f"Cache hit for configuration: {selected_key}")
            return self.cache[selected_key]

        self.real_evaluations += 1  # Incrementar el número de evaluaciones reales

        # Obtener intersecciones seleccionadas
        selected_states = [cand.intersection for cand, bit in zip(self.problem.candidates, selected) if bit == 1]

        total_weighted_distance = 0
        total_population = 0

        for candidate in self.problem.candidates:
            candidate_state = candidate.intersection
            population = candidate.population
            total_population += population

            # Si la intersección tiene una estación, la distancia es 0
            if candidate_state in selected_states:
                min_distance = 0
            else:
                min_distance = float('inf')
                for station_state in selected_states:
                    self.total_a_star_calls += 1  # Incrementar llamadas totales a A*
                    result = self.ser.cached_a_star(candidate_state, station_state)

                    if result is None:
                        distance = float('inf')
                    else:
                        self.real_a_star_calls += 1  # Incrementar llamadas reales a A*
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
        self.cache[selected_key] = result  # Guardar en caché

        # Depuración opcional
        if self.debug:
            print(f"Total evaluations: {self.total_evaluations}")
            print(f"Real evaluations: {self.real_evaluations}")

        return result
