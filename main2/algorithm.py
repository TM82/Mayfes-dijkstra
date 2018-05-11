from station import Station
from rail import Rail
from display import ap_co

def make_stations():    
    table_cn = loadTable('connection2.csv')
    table_cr = loadTable('coordinate.csv')
    station_number = table_cn.getRowCount() - 1
    stations = []
    for i in range(station_number):
        station = Station(table_cn.getString(i+1,0))
        station.coordinate = [(table_cr.getFloat(i+1,1)),(table_cr.getFloat(i+1,2))]
        stations.append(station)
    
    for i in range(station_number):
        for j in range(station_number):
            try:
                rail_name = Rail.rails[load_cn(table_cn,i+1,j+1)[0]]
            except KeyError:
                continue
            rail_time = load_cn(table_cn,i+1,j+1)[1]
            rail = Rail(rail_name,stations[i],stations[j],rail_time)
            stations[i].links[stations[j]] = rail    
    return stations

def load_cn(table_cn,i,j):
    data = table_cn.getString(i,j)
    data = map(lambda x:int(x),data[1:-1].split(","))
    print(data)
    return data
    
def make_direct_node(decided_node,unsearched_node): 
    direct_node = []
    for node in decided_node:
        for linked_node in node.links.keys():
            if linked_node in unsearched_node:
                stroke(0,255,0)
                strokeWeight(3)
                line(ap_co(node)[0],ap_co(node)[1],ap_co(linked_node)[0],ap_co(linked_node)[1])
                linked_node = relabel(node,linked_node)
                linked_node.previous_node = node
                direct_node.append(linked_node)
                stroke(0,0,0)
                strokeWeight(3)
                line(ap_co(node)[0],ap_co(node)[1],ap_co(linked_node)[0],ap_co(linked_node)[1])
    
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