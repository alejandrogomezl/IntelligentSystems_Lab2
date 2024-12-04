from readJSON import loadJSON
from newSearch import SearchNew
from evaluate import Evaluate

hola = loadJSON("./sample-problems-lab2/toy/calle_del_virrey_morcillo_albacete_250_3_candidates_15_ns_4.json")

a = list(hola.intersections.values())[0]
b = list(hola.intersections.values())[1]


# def generateRandom(nCandidates, nStations):
#     randomArray = [1] * nStations + [0] * (nCandidates - nStations)
#     random.seed(0)
#     random.shuffle(randomArray)
#     return randomArray

# bin = generateRandom(len(hola.candidates), hola.nstations)
# bin = [0,0,0,0,1,0,0,0,1,0,0,0,1,0,1]
# bin = [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0]
# bin = [0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1]

# ev = Evaluate(hola)
# print(ev.evaluate(bin))
# print(ev.evaluate(bin))

alo = SearchNew(hola)
print(alo.randomSearch(3000))
