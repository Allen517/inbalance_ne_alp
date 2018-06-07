# -*- coding:utf8 -*-

import sys
import networkx as nx
from collections import defaultdict

def read_net(filepath):
	graph = nx.read_adjlist(filepath, create_using=nx.DiGraph())
	for i,j in graph.edges():
		graph[i][j]['weight'] = 1.
	return graph

def get_node_degree(graph):
	out_degree = defaultdict(int)
	in_degree = defaultdict(int)
	for edge in graph.edges():
		out_degree[edge[0]] += 1
		in_degree[edge[1]] += 1
	return in_degree, out_degree

def shrink_network(graph, in_degree, out_degree, thres):
	cnt = 0
	for nd, deg in out_degree.iteritems():
		if deg>thres:
			continue
		if in_degree[nd]<=thres:
			graph.remove_node(nd)
			cnt += 1
	print 'Remove {} nodes'.format(cnt)
	return graph

def write_network(graph, outfile):
	with open(outfile, 'w') as fout:
		for edge in graph.edges():
			fout.write('{} {}\n'.format(edge[0], edge[1]))

if __name__=='__main__':
	if len(sys.argv)<4:
		print 'please input [network file, output file, shrink threshold]'
		sys.exit(1)
	print 'Reading network...'
	graph = read_net(sys.argv[1])
	print 'Finish loading network'
	print 'Start to get node degree...'
	in_degree,out_degree = get_node_degree(graph)
	print 'Finish geting node degree'
	print 'Start to shrink network...'
	graph = shrink_network(graph, in_degree, out_degree, int(sys.argv[3]))
	print 'Finish shrink network'
	print 'Start to write network...'
	write_network(graph, sys.argv[2])
	print 'Finish writing graph'
