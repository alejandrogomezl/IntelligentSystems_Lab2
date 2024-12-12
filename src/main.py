from readJSON import loadJSON
from randomSearch import SearchNew
from evaluate import Evaluate
from genetic import GeneticAlgorithm

hola = loadJSON("./sample-problems-lab2/small/calle_condesa_de_trifaldi_albacete_500_0_candidates_18_ns_3.json")


# alo = SearchNew(hola)
# rs=alo.randomSearch(100000)
# print(rs)
# print(alo.getSelectedIds(rs[0]))

problem = hola

ga = GeneticAlgorithm(
    problem=problem,
    population_size=100,
    generations=102,
    mutation_rate=0.2
)

# Ejecutar el algoritmo
ga.run_with_logging()
