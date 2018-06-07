# -*- coding:utf8 -*-

from pymongo import MongoClient
from collections import defaultdict
import re,sys

def store2mongo(datafile, host, port, p_db_name):
	client = MongoClient(host, port)
	batch_size = 100
	p_db = client[p_db_name]
	with open(datafile, 'r') as fin:
		cnt = 0

		db_key = ''
		p_info_type = ''
		has_load_db_key = False
		has_load_uid = False
		has_load_info_type = False

		data = list()
		p_data = dict()

		p1 = re.compile(r'\"(.*?)\"')
		for ln in fin:
			ln = ln.strip()
			if '\"douban\"' in ln or '\"weibo\"' in ln:
				match = p1.search(ln)
				if match:
					db_key = match.group(1)
				has_load_db_key = True
				continue
			if has_load_db_key and '{' in ln:
				match = p1.search(ln)
				if match:
					uid = match.group(1)
				has_load_uid = True
				continue
			if has_load_uid and '[' in ln:
				if 'profile' in ln or 'embedding' in ln:
					match = p1.search(ln)
					if match:
						p_info_type = match.group(1)
					has_load_info_type = True
					continue
			if has_load_info_type and ']' not in ln:
				match = p1.search(ln)
				if match:
					value = match.group(1)
					if p_info_type not in p_data:
						p_data[p_info_type] = list()
					p_data[p_info_type].append(float(value))
			if ']' in ln:
				has_load_info_type = False
				continue
			if '}' in ln:
				has_load_uid = False
				p_data['uid'] = uid
				data.append(p_data)
				p_data = dict()
				cnt += 1
				if cnt%batch_size==0:
					p_db[db_key].insert_many(data)
					data = list()
					print "Store {} {}'s data in mongo".format(cnt, db_key)
		if data:
			p_db[db_key].insert_many(data)

if __name__=='__main__':
	if len(sys.argv)<2:
		print 'please input [data file]'
		sys.exit(1)
	print 'Start to read person data...'
	store2mongo(sys.argv[1], '10.61.1.245', 27017, 'w2d_anchor_pred')
	print 'Finish reading person data'

