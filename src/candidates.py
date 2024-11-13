from state import State

class Candidates:
    def __init__(self, intersection, population):
        self.intersection = State
        self.population = population

    def __eq__(self, value: object) -> bool:
        return isinstance(value, Candidates) and self.intersection == value.intersection
    
    def __hash__(self) -> int:
        return hash(self.intersection)
    
    def __repr__(self) -> str:
        return f"Candidates(intersection={self.intersection}, population={self.population})"
    