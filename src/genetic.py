import random
from evaluate import Evaluate

class GeneticAlgorithm:
    def __init__(self, problem, population_size, generations, mutation_rate):
        self.problem = problem
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.evaluate = Evaluate(problem)

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
        nStations = self.problem.nstations
        selected = sum(individual)
        if selected > nStations:
            # Si hay demasiados unos, cambiar algunos a ceros
            indices = [i for i, bit in enumerate(individual) if bit == 1]
            random.shuffle(indices)
            for i in indices[:selected - nStations]:
                individual[i] = 0
        elif selected < nStations:
            # Si hay pocos unos, cambiar algunos ceros a unos
            indices = [i for i, bit in enumerate(individual) if bit == 0]
            random.shuffle(indices)
            for i in indices[:nStations - selected]:
                individual[i] = 1
        return individual

    def run(self):
        # Inicializar población
        population = [self.generate_individual() for _ in range(self.population_size)]
        best_individual = None
        best_cost = float('inf')

        for generation in range(self.generations):
            # Evaluar población
            evaluated_population = self.evaluate_population(population)

            # Actualizar el mejor individuo encontrado
            for individual, cost in evaluated_population:
                if cost < best_cost:
                    best_individual, best_cost = individual, cost

            # Selección
            parent1, parent2 = self.selection(evaluated_population)

            # Reproducción (Crossover)
            offspring = []
            for _ in range(self.population_size // 2):
                child1, child2 = self.crossover(parent1, parent2)
                offspring.append(self.repair_individual(child1))
                offspring.append(self.repair_individual(child2))

            # Mutación
            population = [self.mutate(ind) for ind in offspring]

        return best_individual, best_cost
