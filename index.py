import networkx as nx
from algorithms.source import dijkstra_path, dijkstra_path_length, bellman_ford, single_source_dijkstra
from datetime import datetime
import time
import string
import random
from random import randint

for x in range(1,3): 
	G=nx.DiGraph()
	for n in range(1,10):  
	   G.add_edge(random.choice(string.ascii_lowercase),random.choice(string.ascii_lowercase),weight=randint(0,9))
	tstart = time.time()
	print single_source_dijkstra(G,'s')
	print "time"
	diff = time.time() - tstart 
	print diff
	# print dijkstra_path_length(G, 's', 'v')
	tstart = time.time()
	print bellman_ford(G,'s')
	print time.time()-tstart
