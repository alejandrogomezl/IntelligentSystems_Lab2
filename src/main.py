from readJSON import loadJSON
from randomSearch import SearchNew
from evaluate import Evaluate
from genetic import GeneticAlgorithm
import os

#hola = loadJSON("./sample-problems-lab2/small/calle_condesa_de_trifaldi_albacete_500_0_candidates_18_ns_3.json")
hola = loadJSON("./sample-problems-lab2/medium/calle_agustina_aroca_albacete_500_1_candidates_89_ns_22.json")
print(hola.nstations)

# alo = SearchNew(hola)
# rs=alo.randomSearch(100000)
# print(rs)
# print(alo.getSelectedIds(rs[0]))

problem = hola

ga = GeneticAlgorithm(
    problem=problem,
    population_size=100,
    generations=50,
    mutation_rate=0.1,
)

# Ejecutar el algoritmo
ga.run_with_logging()


# def dirPath(directory):
#     base_path = './sample-problems-lab2/'  # Prefijo para las rutas
#     for root, _, files in os.walk(directory):
#         for file in files:
#             relative_path = os.path.relpath(os.path.join(root, file), start=directory)
#             formatted_path = os.path.join(base_path, relative_path).replace("\\", "/")  # Asegurar separadores '/'
#             print(formatted_path)
#             problem = loadJSON(formatted_path)
#             ga = GeneticAlgorithm(
#                 problem=problem,
#                 population_size=1000,
#                 generations=50,
#                 mutation_rate=0.2
#             )
#             ga.run_with_logging()
#             print("_" * 70)

# dirPath("./sample-problems-lab2")