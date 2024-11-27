class State:
    def __init__(self, identifier, longitude=None, latitude=None):
        """
        identifier: Identificador único de la intersección.
        longitude: Longitud de la intersección (opcional).
        latitude: Latitud de la intersección (opcional).
        """
        self.identifier = identifier
        self.longitude = longitude
        self.latitude = latitude
        self.neighbors = []
    
    def __eq__(self, other):
        return isinstance(other, State) and self.identifier == other.identifier
    
    def __hash__(self):
        return hash(self.identifier)
    
    def __repr__(self):
        return f"State(identifier={self.identifier}, longitude={self.longitude}, latitude={self.latitude})"