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
    
    rail_colors = {
        'yamanote':(173,255,47),
        'chuo':(193,101,67),
        'soubu':(253,188,0),
        'ginza':(241,154,56),
        'marunouchi':(226,67,64),
        'hibiya':(181,181,173),
        'tozai':(68,153,187),
        'chiyoda':(84,184,137),
        'yurakucho':(189,165,119),
        'hanzomon':(139,118,208),
        'nanboku':(77,169,155),
        'hukutoshin':(147,97,58)
    }
    def __init__(self,name,node1,node2,time):
        self.name = name
        self.stations = [node1,node2]
        self.distance = time
        self.rgb = Rail.rail_colors[self.name]
        