# -*- coding:utf8 -*-

import sys
sys.path.append('src/utils')
from Graph import Graph

from collections import defaultdict

def read_net(filepath):
	graph = Graph()
	with open(filepath, 'r') as fin:
		for ln in fin:
			elems = ln.strip().split()
			graph.add_all(elems[0],set(elems[1:]))
	return graph

def get_node_degree(graph):
	return graph.get_degree()

def shrink_network(graph, in_degree, out_degree, thres):
	cnt = 0
	for nd, deg in out_degree.iteritems():
		if deg>thres:
			continue
		if in_degree[nd]<=thres:
			print nd, deg, in_degree[nd]
			graph.remove_nd(nd)
			cnt += 1
	print 'Remove {} nodes'.format(cnt)
	return graph

def write_network(graph, outfile):
	with open(outfile, 'w') as fout:
		for edge_from, edge_to_dict in graph.g.iteritems():
			for edge_to in edge_to_dict.keys():
				fout.write('{} {}\n'.format(edge_from, edge_to))

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
