#!/usr/bin/env python3

import json
import yaml
import csv
from pprint import pprint

'''json'''
with open('input.json','r') as data_file:
	data = json.load(data_file)
print('----------------json----------------')	
pprint(data)


'''csv'''
reader = csv.DictReader(open('input.csv', 'r'))
dict_list = []
for line in reader:
	dict_list.append(line)
print('----------------csv----------------')
pprint(dict_list)


'''ymal'''
print('----------------ymal----------------') 
with open("input.yaml", 'r') as data_file:
	try:
		pprint(yaml.load(data_file))
	except yaml.YAMLError as exc:
		print(exc)
