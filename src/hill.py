import time
from evaluate import Evaluate
import random

class HillClimbing:
    def __init__(self, problem):
        self.problem = problem
        self.ev = Evaluate(self.problem)

    def generate_random_solution(self):
        """
        Genera una solución inicial aleatoria.
        """
        n_candidates = len(self.problem.candidates)
        n_stations = self.problem.nstations
        solution = [1] * n_stations + [0] * (n_candidates - n_stations)
        random.shuffle(solution)
        return solution

    def generate_neighbors(self, solution):
        """
        Genera todas las soluciones vecinas intercambiando bits.
        """
        neighbors = []
        for i in range(len(solution)):
            for j in range(len(solution)):
                if solution[i] != solution[j]:  # Solo intercambiar 1 ↔ 0
                    neighbor = solution[:]
                    neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
                    neighbors.append(neighbor)
        return neighbors

    def hill_climbing(self, max_iterations=1000):
        """
        Ejecuta el algoritmo Hill Climbing.
        """
        start_time = time.perf_counter()  # Iniciar temporizador
        current_solution = self.generate_random_solution()
        current_cost = self.ev.evaluate(current_solution)

        # Estadísticas acumuladas
        total_astar_calls = self.ev.total_a_star_calls
        real_astar_calls = self.ev.real_a_star_calls
        total_evaluated = 1  # La solución inicial ya se evaluó

        for iteration in range(max_iterations):
            neighbors = self.generate_neighbors(current_solution)

            best_neighbor = None
            best_neighbor_cost = float('inf')

            for neighbor in neighbors:
                neighbor_cost = self.ev.evaluate(neighbor)

                # Actualizar estadísticas después de la evaluación
                total_astar_calls = self.ev.total_a_star_calls
                real_astar_calls = self.ev.real_a_star_calls
                total_evaluated += 1

                if neighbor_cost < best_neighbor_cost:
                    best_neighbor = neighbor
                    best_neighbor_cost = neighbor_cost


            if best_neighbor_cost < current_cost:
                current_solution = best_neighbor
                current_cost = best_neighbor_cost
            else:
                break  # Termina si no hay vecinos mejores

        # Fin del algoritmo
        end_time = time.perf_counter()
        total_time = end_time - start_time

        # Mostrar resultados
        selected_ids = [
            cand.intersection.identifier
            for cand, bit in zip(self.problem.candidates, current_solution)
            if bit == 1
        ]

        print(f"total seconds is : {total_time:.6f}")
        print("\nBest Solution:", current_solution)
        print(f"The {self.problem.nstations} stations will be located in intersections:")
        print("\n".join(map(str, selected_ids)))
        print("\nBest Solution Fitness:", current_cost)
        print("A_star calls:")
        print(f"\ttotal --> {total_astar_calls}")
        print(f"\treal --> {real_astar_calls}")
        print("Evaluated individuals:")
        print(f"\ttotal --> {total_evaluated}")
        print(f"\treal --> {real_astar_calls}")
        print("_" * 50)

        return current_solution, current_cost

