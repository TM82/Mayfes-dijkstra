def draw_rails(unsearched_node):
    for node in unsearched_node:
        for linked_node,rail in node.links.items():
            stroke(0,0,0)
            strokeWeight(1)
            line(ap_co(node)[0],ap_co(node)[1],ap_co(linked_node)[0],ap_co(linked_node)[1])
            x = (ap_co(node)[0]+ap_co(linked_node)[0])/2
            y = (ap_co(node)[1]+ap_co(linked_node)[1])/2
            fill(0)
            text(rail.distance,x,y)

def draw_stations(unsearched_node):
    for node in unsearched_node:
        fill(255,0,0)
        ellipse(ap_co(node)[0],ap_co(node)[1],40,40)
        fill(0)
        text(unsearched_node.index(node),ap_co(node)[0],ap_co(node)[1])
        text(node.name,ap_co(node)[0]+20,ap_co(node)[1])

def update_draw_stations(decided_node):
    for node in decided_node:
        fill(0,255,0)
        ellipse(ap_co(node)[0],ap_co(node)[1],40,40)
        # fill(0)
        # text(node.name,node.coordinate[1]+20,800-node.coordinate[0])
        
def print_result(start_node,goal_node):
    print('----------------')
    print("start: {0}    goal:{1}".format(start_node.name,goal_node.name))
    print
    print(goal_node.name)
    node = goal_node
    pre_node = goal_node.previous_node
    pre_pre_node = pre_node.previous_node
    while node != start_node:
        if pre_pre_node:
            if pre_pre_node.links[pre_node].name != pre_node.links[node].name:
                print("^  {0}".format(pre_node.links[node].name))
                print(pre_node.name)
                node = pre_node
                pre_node = pre_pre_node
                pre_pre_node = pre_pre_node.previous_node
                is_last_different = True
            else:
                node = pre_node
                pre_node = pre_pre_node
                pre_pre_node = pre_pre_node.previous_node
                is_last_different = False
        else: #last pattern
            print("^  {0}".format(pre_node.links[node].name))
            print(pre_node.name)
            node = pre_node

def draw_result(start_node,goal_node):
    x = 0
    node = goal_node
    fill(255,0,0)
    ellipse(ap_co(node)[0],ap_co(node)[1],40,40)
    pre_node = goal_node.previous_node
    while pre_node:
        x += 1
        fill(255,0,0)
        ellipse(ap_co(pre_node)[0],ap_co(pre_node)[1],40,40)
        fill(0)
        text(x,ap_co(pre_node)[0],ap_co(pre_node)[1])
        node = pre_node
        pre_node = pre_node.previous_node
        
def ap_co(node): #appropriate coordinate
    return node.coordinate[1]*1.6+60 ,800-node.coordinate[0]*0.6-475