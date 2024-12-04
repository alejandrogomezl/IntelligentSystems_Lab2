from readJSON import loadJSON
from newSearch import SearchNew
from evaluate import Evaluate

hola = loadJSON("./sample-problems-lab2/toy/calle_del_virrey_morcillo_albacete_250_3_candidates_15_ns_4.json")


alo = SearchNew(hola)
rs=alo.randomSearch(100000)
print(rs)
print(alo.getSelectedIds(rs[0]))