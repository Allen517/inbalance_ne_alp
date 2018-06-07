# -*- coding:utf8 -*-

from collections import defaultdict
import sys

def read_source_net(filepath, outfile):
	net = defaultdict(list)
	batch_size = 100
	with open(filepath, 'r') as fin, open(outfile, 'w') as fout:
		print 'Reading source net file...'
		for ln in fin:
			elems = ln.strip().split()
			net[elems[0]].append(elems[1])
		print 'Finish reading net file'
		print 'Start to format...'
		cnt = 0
		wrtLns = ''
		for nd in net.keys():
			wrtLns += '{} {}\n'.format(nd, ' '.join([fol for fol in net[nd]]))
			cnt += 1
			if cnt%batch_size==0:
				print 'Processing {} records'.format(cnt)
				fout.write(wrtLns)
				wrtLns = ''
		if wrtLns:
			fout.write(wrtLns)

if __name__=='__main__':
	if len(sys.argv)<3:
		print 'please input [pairwise net file, output file]'
		sys.exit(1)
	read_source_net(sys.argv[1], sys.argv[2])