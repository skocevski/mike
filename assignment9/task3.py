
import pandas as pd
import networkx as nx


def maketuple(x, y):
    r = []
    for i in range(len(y)):
        r.append((x, y[i]))
    return r
    
def findDiameter(G):
    for index, graph in enumerate(G):
        diameter = set()
        for node in graph:
            lenght = nx.single_source_dijkstra_path_length(graph, node)
            diameter.add(lenght[max(lenght, key=lenght.get)])
        print ("Diameter: ", index, max(diameter))
        
#if the graph is not connected make subgraphs
if(nx.is_connected(G)):
    print ("connected")
    findDiameter(G)
else:
    print ("disconnected")
    subgraphs = sorted(nx.connected_component_subgraphs(G), key=len, reverse=True)
    findDiameter(subgraphs)
    
store = pd.HDFStore('store.h5')
df2 = store['df2']

G = nx.Graph()
for row in df2.itertuples():
    G.add_edges_from(maketuple(row[1], row[2]))
print ("Graph is created..")
