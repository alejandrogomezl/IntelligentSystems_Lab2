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
        """
        Compara dos estados basados en su identificador.
        """
        return isinstance(other, State) and self.identifier == other.identifier
    
    def __hash__(self):
        """
        Permite que los estados sean utilizados en conjuntos y como claves en diccionarios.
        """
        return hash(self.identifier)
    
    def __repr__(self):
        """
        Representación amigable del estado, mostrando el identificador y las coordenadas.
        """
        return f"State(identifier={self.identifier}, longitude={self.longitude}, latitude={self.latitude})"