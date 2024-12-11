from readJSON import loadJSON
from randomSearch import SearchNew
from evaluate import Evaluate
from genetic import GeneticAlgorithm
from hill import HillClimbing

hola = loadJSON("./sample-problems-lab2/small/calle_condesa_de_trifaldi_albacete_500_0_candidates_18_ns_3.json")
hola = loadJSON("./sample-problems-lab2/small/calle_agustina_aroca_albacete_250_0_candidates_75_ns_7.json")

# alo = SearchNew(hola)
# rs=alo.randomSearch(100000)
# print(rs)
# print(alo.getSelectedIds(rs[0]))

problem = hola

ga = GeneticAlgorithm(
    problem=problem,
    population_size=50,
    generations=100,
    mutation_rate=0.1
)

# Ejecutar el algoritmo
ga.run_with_logging()

# hc = HillClimbing(problem)

# # Ejecutar el algoritmo
# best_solution, best_cost = hc.hill_climbing(max_iterations=100)