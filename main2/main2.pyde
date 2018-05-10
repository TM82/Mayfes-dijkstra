from algorithm import *
from node import Node
from rail import Rail


start_node,goal_node,decided_node,unsearched_node = None,None,None,None
num = [str(i) for i in range(10)]
input = []
is_start = False
is_goal = False

def setup():
    global decided_node,unsearched_node
    decided_node = []
    unsearched_node = make_stations()
    size(1500,800)
    background(255)
    draw_rails()
    draw_stations()
    print('Enter start station number')

def draw():
    #check framerate and set it to link compare speed
    global decided_node,unsearched_node,is_start,is_goal
    if is_start and is_goal:
        direct_node = make_direct_node(decided_node,unsearched_node)
        decided_node,unsearched_node = get_min(direct_node,decided_node,unsearched_node)
        update_draw_stations()
        delay(200)
        if not unsearched_node:
            print_result(start_node,goal_node)
            is_start,is_goal = False,False
    
def draw_rails():
    global unsearched_node
    for node in unsearched_node:
        for keynode,rail in node.links.items():
            stroke(0,0,0)
            strokeWeight(2)
            line(node.coordinate[1],800-node.coordinate[0],keynode.coordinate[1],800-keynode.coordinate[0])
            x = (node.coordinate[1]+keynode.coordinate[1])/2
            y = (800-node.coordinate[0]+800-keynode.coordinate[0])/2
            text(rail.distance,x,y)

def draw_stations():
    for node in unsearched_node:
        fill(255,0,0)
        ellipse(node.coordinate[1],800-node.coordinate[0],40,40)
        fill(0)
        text(node.name,node.coordinate[1]+20,800-node.coordinate[0])

def update_draw_stations():
    global decided_node
    for node in decided_node:
        fill(0,255,0)
        ellipse(node.coordinate[1],800-node.coordinate[0],40,40)
        # fill(0)
        # text(node.name,node.coordinate[1]+20,800-node.coordinate[0])

def keyPressed():
    global start_node,goal_node,decided_node,unsearched_node,input,is_start,is_goal
    if not is_start:
        if key in num:
            input.append(key)
            print('present input {0}'.format(''.join(input)))
        elif key == ENTER:
            number = int(''.join(input))
            try:
                start_node = unsearched_node[number]
                start_node.is_ok = True
                start_node.label = 0
                decided_node.append(start_node)
                unsearched_node.remove(start_node)
                print('set {0} as a start station'.format(start_node.name))
                is_start = True
                input = []
                print('Enter goal station number')
            except IndexError:
                print('{0} is incorrect number'.format(number))
                number = None
                input = []
        else:
            print('{} is not number'.format(key))
    elif not is_goal:
        if key in num:
            input.append(key)
            print('present input {0}'.format(''.join(input)))
        elif key == ENTER:
            number = int(''.join(input))
            try:
                goal_node = unsearched_node[number]
                print('set {0} as a goal station'.format(goal_node.name))
                is_goal = True
                input = []
            except IndexError:
                print('{0} is incorrect number'.format(number))
                number = None
                input = []
                print()
        else:
            print('{} is not number'.format(key))