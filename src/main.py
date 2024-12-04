from readJSON import loadJSON
from search import Search
import random

hola = loadJSON("./sample-problems-lab2/toy/calle_del_virrey_morcillo_albacete_250_3_candidates_15_ns_4.json")

a = list(hola.intersections.values())[0]
b = list(hola.intersections.values())[1]


def generateRandom(nCandidates, nStations):
    randomArray = [1] * nStations + [0] * (nCandidates - nStations)
    random.seed(0)
    random.shuffle(randomArray)
    return randomArray

bin = generateRandom(len(hola.candidates), hola.nstations)
bin = [0,0,0,0,1,0,0,0,1,0,0,0,1,0,1]


def evaluate(problem, selected_stations):
    selected_states = [cand.intersection for cand, bit in zip(problem.candidates, selected_stations) if bit == 1]

    total_weighted_distance = 0
    total_population = 0
    
    for candidate in problem.candidates:
        candidate_state = candidate.intersection
        population = candidate.population
        total_population += population

        print(f"place_id={candidate_state.identifier}; citizens = {population}")
        
        # Calcular la distancia mínima a las estaciones seleccionadas
        if candidate_state in selected_states:
            # Si el candidato es una estación seleccionada, establecer la distancia mínima a 0
            min_distance = 0
            print(f"to station with id {candidate_state.identifier} = 0 (self)")
        else:
            min_distance = 100000000000000000
            for station_state in selected_states:
                # Ejecutar A* para calcular la distancia entre candidate_state y station_state
                result = Search(problem).cached_a_star(candidate_state, station_state)
                print("search")
                if result is None:
                    distance = 100000000000000000
                else:
                    distance = result[4]

                print(f"to station with id {station_state.identifier} = {distance if distance != 100000000000000000 else '100000000000000000'}")
                min_distance = min(min_distance, distance)

        print(f"min_distance --> {min_distance}")
        weighted_distance = min_distance * population
        print(f"accounting for ={weighted_distance}")
        print("_" * 30)

        # Ponderar por la población
        total_weighted_distance += weighted_distance

    # Normalizar por la población total
    print(f"weighted_distances={total_weighted_distance}")
    print(f"total_citizens == {total_population}")
    result = total_weighted_distance / total_population if total_population > 0 else float('inf')
    print(f"Result: {result}")
    return result

        

ev = evaluate(hola, bin)
print(ev)