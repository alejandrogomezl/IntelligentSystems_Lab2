from search import Search


class Evaluate:
    def __init__(self, problem):
        self.problem = problem
        self.ser = Search(self.problem)

    def evaluate(self, selected):
        selected_states = [cand.intersection for cand, bit in zip(self.problem.candidates, selected) if bit == 1]

        total_weighted_distance = 0
        total_population = 0
        
        for candidate in self.problem.candidates:
            candidate_state = candidate.intersection
            population = candidate.population
            total_population += population

            print(f"place_id={candidate_state.identifier}; citizens = {population}")
            
            if candidate_state in selected_states:
                min_distance = 0
                print(f"to station with id {candidate_state.identifier} = 0")
            else:
                min_distance = 100000000000000000
                for station_state in selected_states:
                    result = self.ser.cached_a_star(candidate_state, station_state)
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

            total_weighted_distance += weighted_distance

        print(f"weighted_distances={total_weighted_distance}")
        print(f"total_citizens == {total_population}")
        result = total_weighted_distance / total_population if total_population > 0 else float('inf')
        print(f"Result: {result}")
        return result

        
