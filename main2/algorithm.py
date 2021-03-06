from station import Station
from rail import Rail

def make_stations():
        table_cn = loadTable('connection.csv')
        table_cr = loadTable('coordinate.csv')
        station_number = table_cn.getRowCount() - 1
        stations = []
        for i in range(station_number):
            station = Station(table_cn.getString(i+1,0))
            station.coordinate = [(table_cr.getFloat(i+1,1))*0.6+480,(table_cr.getFloat(i+1,2))*1.5+150]
            stations.append(station)
        
        for i in range(station_number):
            for j in range(station_number):
                for k,value in Rail.rails.items():
                    if table_cn.getInt(i+1,j+1) == 0:
                        pass
                    elif table_cn.getInt(i+1,j+1) == k:
                        rail = Rail(value,stations[i],stations[j])
                        stations[i].links[stations[j]] = rail    
        return stations

def make_direct_node(decided_node,unsearched_node): 
    direct_node = []
    for node in decided_node:
        for linked_node in node.links.keys():
            if linked_node in unsearched_node:
                stroke(0,255,0)
                strokeWeight(3)
                line(node.coordinate[1],800-node.coordinate[0],linked_node.coordinate[1],800-linked_node.coordinate[0])
                linked_node = relabel(node,linked_node)
                linked_node.previous_node = node
                direct_node.append(linked_node)
                delay(50)
                stroke(0,0,0)
                strokeWeight(3)
                line(node.coordinate[1],800-node.coordinate[0],linked_node.coordinate[1],800-linked_node.coordinate[0])
    
    return direct_node

def relabel(node,linked_node):
    try:
        pre_prelabel = node.label + linked_node.links[node].distance
        if pre_prelabel < linked_node.prelabel:
            linked_node.prelabel = pre_prelabel
        return linked_node
    except:
        print(node.name)
        print(linked_node.name)
        
def get_min(direct_node,decided_node,unsearched_node):  
    min_node = sorted(direct_node,key=lambda x: x.prelabel)[0]
    min_node.is_ok = True
    min_node.label = min_node.prelabel
    decided_node.append(min_node)
    unsearched_node.remove(min_node)
    
    return decided_node,unsearched_node

def print_result(start_node,goal_node):
    print("start: {0}    goal:{1}".format(start_node.name,goal_node.name))
    print
    print(goal_node.name)
    print("^")
    pre_node = goal_node.previous_node
    #compare pre_node.railname to node
    while pre_node != start_node:
        print(pre_node.name)
        print("^")
        pre_node = pre_node.previous_node
    print(pre_node.name)