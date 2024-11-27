from readJSON import loadJSON
from search import Search

hola = loadJSON("./sample-problems-lab2/toy/calle_del_virrey_morcillo_albacete_250_3_candidates_15_ns_4.json")

a = list(hola.intersections.values())[0]
b = list(hola.intersections.values())[1]

src = Search(hola)
print(src.cached_a_star(a, b))
print(src.cached_a_star(b, a))