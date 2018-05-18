from light import createLight
img = createLight(random(0.5, 0.8), random(0.5, 0.8), random(0.5, 0.8))
#img = createLight(0.3, 0.3, 0.7)
imageside = 200


def draw_rails(unsearched_node):
    for node in unsearched_node:
        for linked_node,rail in node.links.items():
            stroke(rail.rgb[0],rail.rgb[1],rail.rgb[2])
            strokeWeight(1)
            line(ap_co(node)[0],ap_co(node)[1],ap_co(linked_node)[0],ap_co(linked_node)[1])
            x = (ap_co(node)[0]+ap_co(linked_node)[0])/2
            y = (ap_co(node)[1]+ap_co(linked_node)[1])/2
            fill(255)
            text(rail.distance,x,y)
            
def draw_rails_dark(unsearched_node):
    for node in unsearched_node:
        for linked_node,rail in node.links.items():
            stroke(50,50,50)
            strokeWeight(1)
            line(ap_co(node)[0],ap_co(node)[1],ap_co(linked_node)[0],ap_co(linked_node)[1])
            x = (ap_co(node)[0]+ap_co(linked_node)[0])/2
            y = (ap_co(node)[1]+ap_co(linked_node)[1])/2
            fill(255)
            text(rail.distance,x,y)

def draw_stations(unsearched_node):
    for node in unsearched_node:
        #fill(0,255,0)
        #ellipse(ap_co(node)[0],ap_co(node)[1],40,40)
        image(img,ap_co(node)[0]-imageside/2,ap_co(node)[1]-imageside/2);
        fill(255,255,255)
        text(unsearched_node.index(node),ap_co(node)[0],ap_co(node)[1])
        fill(255,255,255)
        text(node.name,ap_co(node)[0]+20,ap_co(node)[1])

def update_draw_stations(decided_node):
    for node in decided_node:
        noStroke()
        #fill(0,255,0)
        #ellipse(ap_co(node)[0],ap_co(node)[1],40,40)
        image(img,ap_co(node)[0]-imageside/2,ap_co(node)[1]-imageside/2);
        fill(0,0,0)
        text(decided_node.index(node),ap_co(node)[0],ap_co(node)[1])
        fill(255,255,255)
        text(node.name,ap_co(node)[0]+20,ap_co(node)[1])
        
def update_draw_stations_dark(decided_node):
    for node in decided_node:
        noStroke()
        fill(50,50,50)
        ellipse(ap_co(node)[0],ap_co(node)[1],40,40)
        #image(img,ap_co(node)[0]-imageside/2,ap_co(node)[1]-imageside/2);
        fill(50,50,50)
        text(decided_node.index(node),ap_co(node)[0],ap_co(node)[1])
        fill(50,50,50)
        text(node.name,ap_co(node)[0]+20,ap_co(node)[1])

        
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
    x = -1
    node = goal_node
    while node:
        x += 1
        node = node.previous_node
    node = goal_node
    pre_node = node.previous_node
    while pre_node:
        fill(255,0,0)
        ellipse(ap_co(node)[0],ap_co(node)[1],42,42)
        fill(255)
        text(x,ap_co(node)[0],ap_co(node)[1])
        node = pre_node
        pre_node = pre_node.previous_node
        x -= 1
    fill(255,0,0)
    ellipse(ap_co(node)[0],ap_co(node)[1],42,42)

def draw_result_line(start_node,goal_node):
    x = -1
    node = goal_node
    while node:
        x += 1
        node = node.previous_node
    node = goal_node
    pre_node = node.previous_node
    while pre_node:
        rgb = node.links[node.previous_node].rgb
        stroke(rgb[0],rgb[1],rgb[2])
        strokeWeight(6)
        line(ap_co(pre_node)[0],ap_co(pre_node)[1],ap_co(node)[0],ap_co(node)[1])
        node = pre_node
        pre_node = pre_node.previous_node
        x -= 1
    #fill(255,0,0)
    #ellipse(ap_co(node)[0],ap_co(node)[1],42,42)
        
def ap_co(node): #appropriate coordinate
    return node.coordinate[1]*1.9+150 ,800-node.coordinate[0]-300