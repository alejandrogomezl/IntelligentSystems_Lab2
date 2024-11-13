import json
from state import State
from action import Action
from problem import Problem
from search import Search

def loadJSON(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    intersections = {}
    for i_data in data["intersections"]:
        inter = State(
            identifier=i_data["identifier"],
            latitude=i_data["latitude"],
            longitude=i_data["longitude"],
        )
        intersections[inter.identifier] = inter

    segments = []
    for seg_data in data["segments"]:
        origin = intersections[seg_data["origin"]]
        destination = intersections[seg_data["destination"]]
        segment = Action(
            origin=origin,
            destination=destination,
            distance=seg_data["distance"],
            speed=seg_data["speed"],
        )
        segments.append(segment)
        origin.neighbors.append((destination, segment))

    initial_state = intersections[data["initial"]]
    goal_state = intersections[data["final"]]

    for state in intersections.values():
        # Sort by id
        state.neighbors.sort(key=lambda x: x[0].identifier, reverse=False)

        # Sort by heuristic
        #state.neighbors.sort(key=lambda x: heuristic(x[0], goal_state), reverse=False)

        #Sort by distance
        #state.neighbors.sort(key=lambda x: x[0].distance, reverse=False)
        


    return Problem(initial_state, goal_state, intersections, segments)
