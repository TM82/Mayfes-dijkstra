class Station():
    def __init__(self,name):
        self.name = name
        self.links ={}
        self.is_ok =False
        self.prelabel = float("inf")
        self.label = float("inf")
        self.previous_node = None
        self.coordinate = None