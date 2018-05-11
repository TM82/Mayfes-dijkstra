class Rail():
    rails = {
        1:'yamanote',
        2:'chuo',
        3:'soubu',
        4:'ginza',
        5:'marunouchi',
        6:'hibiya',
        7:'tozai',
        8:'chiyoda',
        9:'yurakucho',
        10:'hanzomon',
        11:'nanboku',
        12:'hukutoshin'
    }

    def __init__(self,name,node1,node2,time):
        self.name = name
        self.stations = [node1,node2]
        self.distance = time