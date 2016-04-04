import networkx as nx
from algorithms.source import dijkstra_path, dijkstra_path_length, bellman_ford, single_source_dijkstra
from random import randint
import time

for x in range(100,1000,100):
    D = nx.complete_graph(x)
    # print(D.edges())
    for (u, v) in D.edges():
        D[u][v]['weight'] = randint(0, 9)
    # for (u, v) in D.edges():
    #     print(D[u][v]['weight'])
    print("size : "),
    print(x)
    start = time.time()
    single_source_dijkstra(D,0)
    print("dijkstra_path : "),
    print(time.time() - start)
    start = time.time()
    print("bellman_ford : "),
    bellman_ford(D,0)
    print(time.time() - start)
