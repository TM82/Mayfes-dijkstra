from algorithm import *
from station import Station
from rail import Rail
from display import *
from light import createLight

start_node,goal_node,decided_node,unsearched_node = None,None,None,None
num = [str(i) for i in range(10)]
input = []
is_start = False
is_goal = False
#img = createLight(random(0.5, 0.8), random(0.5, 0.8), random(0.5, 0.8))
img = createLight(0, 0.5, 0.5)

def setup():

    blendMode(SCREEN);
    global decided_node,unsearched_node
    decided_node = []
    unsearched_node = make_stations()
    # size(1500,800)
    fullScreen()
    frameRate(10)
    background(0)
    draw_rails(unsearched_node)
    draw_stations(unsearched_node)
    
    print('Enter start station number')

def draw():
    
    global decided_node,unsearched_node,is_start,is_goal
    if is_start and is_goal:
        direct_node = make_direct_node(decided_node,unsearched_node)
        decided_node,unsearched_node = get_min(direct_node,decided_node,unsearched_node)
        update_draw_stations(decided_node)
        if not unsearched_node:
            background(0)
            draw_rails_dark(decided_node)
            update_draw_stations(decided_node)
            
            print_result(start_node,goal_node)
            draw_result(start_node,goal_node)
            draw_result_line(start_node,goal_node)
            is_start,is_goal = False,False
    

def keyPressed():
    global start_node,goal_node,decided_node,unsearched_node,input,is_start,is_goal
    if key == ' ':
        exit()
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
                print('set {0} as a start station'.format(start_node.name))
                is_start = True
                input = []
                print('Enter goal station number')
            except IndexError:
                print('{0} is incorrect number'.format(number))
                number = None
                input = []
        else:
            pass
            # print('{} is not number'.format(key))
    elif not is_goal:
        if key in num:
            input.append(key)
            print('present input {0}'.format(''.join(input)))
        elif key == ENTER:
            number = int(''.join(input))
            try:
                goal_node = unsearched_node[number]
                unsearched_node.remove(start_node)
                print('set {0} as a goal station'.format(goal_node.name))
                is_goal = True
                input = []
            except IndexError:
                print('{0} is incorrect number'.format(number))
                number = None
                input = []
                print()
        else:
            pass
            # print('{} is not number'.format(key))            

def mousePressed():
    img = createLight(random(0.5, 0.8), random(0.5, 0.8), random(0.5, 0.8))