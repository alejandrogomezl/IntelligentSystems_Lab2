import random
from evaluate import Evaluate
import time

class GeneticAlgorithm:
    def __init__(self, problem, population_size, generations, mutation_rate):
        self.problem = problem
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.evaluate = Evaluate(problem)

        self.cont = 0

    def generate_individual(self):
        nCandidates = len(self.problem.candidates)
        nStations = self.problem.nstations
        individual = [1] * nStations + [0] * (nCandidates - nStations)
        random.shuffle(individual)
        return individual

    def evaluate_population(self, population):
        return [(individual, self.evaluate.evaluate(individual)) for individual in population]

    def selection(self, evaluated_population):
        # Ordenar por fitness (menor es mejor)
        evaluated_population.sort(key=lambda x: x[1])
        # Seleccionar los dos mejores
        return evaluated_population[0][0], evaluated_population[1][0]

    def crossover(self, parent1, parent2):
        point = random.randint(1, len(parent1) - 1)  # Punto de cruce
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return child1, child2

    def mutate(self, individual):
        for i in range(len(individual)):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]  # Cambiar 0 a 1 o 1 a 0
        return individual

    def repair_individual(self, individual):
        """
        Repara un individuo para asegurar que tiene exactamente `nstations` unos.

        Parámetro:
        - individual: Array binario a reparar.

        Devuelve:
        - Un individuo reparado que cumple las restricciones.
        """
        nStations = self.problem.nstations  # Número de estaciones requeridas
        selected = sum(individual)  # Número actual de unos (1s)

        if selected > nStations:
            # Si hay demasiados unos, cambiar algunos a ceros
            indices = [i for i, bit in enumerate(individual) if bit == 1]  # Índices de unos
            random.shuffle(indices)  # Mezclar los índices
            for i in indices[:selected - nStations]:  # Reducir el exceso
                individual[i] = 0

        elif selected < nStations:
            # Si hay pocos unos, cambiar algunos ceros a unos
            indices = [i for i, bit in enumerate(individual) if bit == 0]  # Índices de ceros
            random.shuffle(indices)  # Mezclar los índices
            for i in indices[:nStations - selected]:  # Completar el déficit
                individual[i] = 1

        return individual



    def run(self):
        """
        Ejecuta el algoritmo genético.
        """
        # Generar población inicial
        population = [self.generate_individual() for _ in range(self.population_size)]
        best_individual = None
        best_cost = 100000000000000000

        for generation in range(self.generations):
            # Evaluar población
            evaluated_population = self.evaluate_population(population)

            # Actualizar el mejor individuo encontrado
            for individual, cost in evaluated_population:
                if cost < best_cost:
                    print(f"Best cost: {cost}")
                    best_individual, best_cost = individual, cost

            # Selección
            parent1, parent2 = self.selection(evaluated_population)

            # Reproducción (Crossover)
            offspring = []
            for _ in range(self.population_size // 2):
                child1, child2 = self.crossover(parent1, parent2)
                offspring.append(self.repair_individual(child1))  # Reparar hijo 1
                offspring.append(self.repair_individual(child2))  # Reparar hijo 2

            # Mutación
            population = [self.repair_individual(self.mutate(ind)) for ind in offspring]  # Reparar después de mutación

        return best_individual, best_cost


    def run_with_logging(self):
        """
        Ejecuta el algoritmo genético y genera una salida similar al formato requerido.
        """
        start_time = time.time()

        best_solution, best_cost = self.run()  # Ejecuta el algoritmo genético
        elapsed_time = time.time() - start_time

        # Obtener IDs de las estaciones seleccionadas
        selected_ids = [
            candidate.intersection.identifier
            for candidate, bit in zip(self.problem.candidates, best_solution)
            if bit == 1
        ]

        # Salida formateada
        print(f"total seconds is : {elapsed_time}")
        print()
        print(f"Best Solution: {best_solution}")
        print(f"The {len(selected_ids)} stations will be located in intersections:")
        print("\n".join(map(str, selected_ids)))
        print()
        print(f"Best Solution Fitness: {best_cost}")
        print("A_star calls:")
        print(f"\ttotal --> {self.evaluate.total_a_star_calls}")
        print(f"\treal --> {self.evaluate.real_a_star_calls}")
        print("Evaluated individuals:")
        print(f"\ttotal --> {self.evaluate.total_evaluations}")
        print(f"\treal --> {self.evaluate.real_evaluations}")
        print("_" * 50)
        print()
