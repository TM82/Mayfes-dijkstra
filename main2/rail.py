class Rail():
    rails = {
        1:'ginza',
        2:'yamanote'
    }
    
    def __init__(self,name,node1,node2):
        self.name = name
        self.stations = [node1,node2]
        self.distance = self.calc_distance(self.stations)
        
    def calc_distance(self,stations):
        x1=stations[0].coordinate[0] 
        x2=stations[1].coordinate[0]
        y1=stations[0].coordinate[1] 
        y2=stations[1].coordinate[1]
        return int(sqrt((x1-x2)**2+(y1-y2)**2))