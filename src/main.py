from readJSON import loadJSON
from search import Search
import random

hola = loadJSON("./sample-problems-lab2/toy/calle_del_virrey_morcillo_albacete_250_3_candidates_15_ns_4.json")

a = list(hola.intersections.values())[0]
b = list(hola.intersections.values())[1]

selected = 0
poss = []
for i in range(len(hola.candidates)):
    r = random.randint(0, 1)
    if r == 1 and selected < 4:
        selected += 1
        poss.append(1)
    else:
        poss.append(0)

print(poss)

tosearch=[]
        

for i in tosearch:
    print(i)

for intersection in hola.intersections.items():
    print(intersection)