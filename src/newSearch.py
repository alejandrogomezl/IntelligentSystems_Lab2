from evaluate import Evaluate
import random

class SearchNew:
    def __init__(self, problem):
        self.problem = problem


    def generateRandomArray(self):
        nCandidates = len(self.problem.candidates)
        nStations = self.problem.nstations
        

        randomArray = [1] * nStations + [0] * (nCandidates - nStations)
        #random.seed(0)
        random.shuffle(randomArray)
        return randomArray

    def randomSearch(self, n):
        best = None
        best_cost = 100000000000000000
        ev = Evaluate(self.problem)
        for r in range(n):
            current = self.generateRandomArray()
            cost = ev.evaluate(current)
            if cost < best_cost:
                best = current
                best_cost = cost
        return best, best_cost

    def getSelectedIds(self, binary_array):
        selected_ids = [
            cand.intersection.identifier
            for cand, bit in zip(self.problem.candidates, binary_array)
            if bit == 1
        ]
        return selected_ids