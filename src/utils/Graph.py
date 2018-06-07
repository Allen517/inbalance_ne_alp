# -*- coding:utf8 -*-

from collections import defaultdict

class Graph(object):

	def __init__(self):
		self.g = defaultdict(dict)
		self.rev_index = defaultdict(set)

	def add_all(self, nd, n_nd_set):
		if not n_nd_set:
			self.g[nd] = dict()
		for n_nd in n_nd_set:
			self.add(nd, n_nd)

	def add(self, nd, n_nd):
		self.g[nd][n_nd] = 1.
		self.rev_index[n_nd].add(nd)

	def remove_nd(self, rm_nd):
		if rm_nd in self.g:
			self.g.pop(rm_nd)
		if rm_nd in self.rev_index:
			for rel_nd in self.rev_index[rm_nd]:
				if rel_nd in self.g and rm_nd in self.g[rel_nd]:
					self.g[rel_nd].pop(rm_nd)
			self.rev_index.pop(rm_nd)

	def get_graph(self):
		return self.g

	def get_degree(self):
		self.degree = defaultdict(int)
		self.rev_degree = defaultdict(int)
		for k,v in self.g.iteritems():
			self.degree[k] += len(v)
			if v:
				for sub_key in v.keys():
					self.rev_degree[sub_key] += 1

		return self.degree, self.rev_degree