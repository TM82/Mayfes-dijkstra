def draw_rails(unsearched_node):
    for node in unsearched_node:
        for keynode,rail in node.links.items():
            stroke(0,0,0)
            strokeWeight(1)
            line(node.coordinate[1],800-node.coordinate[0],keynode.coordinate[1],800-keynode.coordinate[0])
            x = (node.coordinate[1]+keynode.coordinate[1])/2
            y = (800-node.coordinate[0]+800-keynode.coordinate[0])/2
            fill(0)
            text(rail.distance,x,y)

def draw_stations(unsearched_node):
    for node in unsearched_node:
        fill(255,0,0)
        ellipse(node.coordinate[1],800-node.coordinate[0],40,40)
        fill(0)
        text(unsearched_node.index(node),node.coordinate[1]-5,800-node.coordinate[0])
        text(node.name,node.coordinate[1]+20,800-node.coordinate[0])

def update_draw_stations(decided_node):
    for node in decided_node:
        fill(0,255,0)
        ellipse(node.coordinate[1],800-node.coordinate[0],40,40)
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
    ellipse(node.coordinate[1],800-node.coordinate[0],40,40)
    pre_node = goal_node.previous_node
    while pre_node:
        x += 1
        fill(255,0,0)
        ellipse(pre_node.coordinate[1],800-pre_node.coordinate[0],40,40)
        fill(0)
        text(x,pre_node.coordinate[1],800-pre_node.coordinate[0])
        node = pre_node
        pre_node = pre_node.previous_node