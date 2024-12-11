from readJSON import loadJSON
from newSearch import SearchNew
from evaluate import Evaluate
from genetic import GeneticAlgorithm

hola = loadJSON("./sample-problems-lab2/toy/calle_del_virrey_morcillo_albacete_250_3_candidates_15_ns_4.json")


alo = SearchNew(hola)
rs=alo.randomSearch(100000)
print(rs)
print(alo.getSelectedIds(rs[0]))

problem = hola

ga = GeneticAlgorithm(
    problem=problem,
    population_size=50,
    generations=100,
    mutation_rate=0.1
)

# Ejecutar el algoritmo
best_solution, best_cost = ga.run()

# Imprimir los resultados
print("Mejor solución:", best_solution)
print("Costo asociado:", best_cost)