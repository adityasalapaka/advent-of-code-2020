filename = 'day7.txt'

import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()

for line in open(filename,'r'):
	line = line.split('contain')

	parent = line[0].strip().split()
	parent = (' ').join(parent[0:2])
	G.add_node(parent)

	for child in line[1].strip().split(','):

		if child == 'no other bags.':
			break

		child = child.strip().split()
		weight = int(child[0])

		child = (' ').join(child[1:3])

		G.add_edge(parent, child, weight=weight)

# part 1
def predecesors(G:nx.DiGraph, source:str, nodes:set=set()) -> set:

	for node in G.predecessors(source):
		nodes.add(node)
		predecesors(G,node, nodes)

	return nodes

print(len(predecesors(G,'shiny gold')))

# part 2
def bags(G:nx.DiGraph, source:str) -> int:

	count = 0

	if G.out_degree(source) == 0:
		return 1
	
	for node in G.successors(source):
		count += bags(G, node) * G.edges[source, node]['weight']

	return count + 1 # the +1 is to include the source itself

print(bags(G,'shiny gold')-1) # -1 is to exclude source