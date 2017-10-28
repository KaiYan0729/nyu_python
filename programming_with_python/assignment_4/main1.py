#!/usr/bin/env python3

import json
import csv
import pprint
import yaml

pp = pprint.PrettyPrinter(indent=4)

def csv_to_list():
	with open('input1.csv', 'r') as csvfile:
		d_reader = csv.DictReader(csvfile)
		csv_list = []
		for x in d_reader:
			csv_list.append(x)
	print('csv list')
	pp.pprint(csv_list)
	return csv_list
	
def json_to_list():
	with open('input1.csv', 'r') as csvfile:
		d_reader = csv.DictReader(csvfile)
		dict_list = list(d_reader)
		headers = d_reader.fieldnames

	with open('input1.json', 'w') as f_json:
		json.dump(dict_list, f_json)

	with open('input1.json', 'r') as jsonfile:
		json_list = []
		json_load = json.load(jsonfile)
		json_list.append(json_load)
	print('json list')
	pp.pprint(json_list)
	return json_list

def yaml_to_list():
	with open('input1.csv', 'r') as csvfile:
		d_reader = csv.DictReader(csvfile)
		dict_list = list(d_reader)
		headers = d_reader.fieldnames

	with open('input1.yaml', 'w') as f_yaml:
		yaml.dump(dict_list, f_yaml)

	with open('input1.yaml', 'r') as yamlfile:
		yaml_list = []
		yaml_load = yaml.load(yamlfile)
		yaml_list.append(yaml_load)
	print('yaml list')
	pp.pprint(yaml_list)
	return yaml_list

def to_one_dict(csv_list, json_list, yaml_list):
    output = {}
    output['csv'] = csv_list
    output['json'] = json_list
    output['yaml'] = yaml_list
    return output

def csv_output(dict):
    csvlist = dict['csv']
    with open('output.csv', 'w') as csv_out:
        fieldnames = ['fname', 'lname', 'year', 'month', 'fcolor', 'fmovie']
        writer = csv.DictWriter(csv_out, fieldnames=fieldnames)
        writer.writeheader()
        for x in csvlist:
            writer.writerow(x)
    return csv_out

def json_output(dict):
    jsonlist = dict['json']
    with open('output.json', 'w') as json_out:
        for x in jsonlist:
            json.dump(x, json_out, indent=4)
    return json_out

def yaml_output(dict):
    yamllist = dict['yaml']
    with open('output.yaml', 'w') as yaml_out:
        yaml.dump_all(yamllist, yaml_out, default_flow_style=False, explicit_start=True)
        for x in yamllist:
            yaml.dump(x, yaml_out)
    return yaml_out

def main():
	csv_list = csv_to_list()
	json_list = json_to_list()
	yaml_list = yaml_to_list()
	dict = to_one_dict(csv_list, json_list, yaml_list)
	csv_out = csv_output(dict)
	json_out = json_output(dict)
	yaml_out = yaml_output(dict)

if __name__ == '__main__':
	main()

'''
file_name_json = 'input1.json'
file_name_csv = 'input1.csv'
file_name_yaml ='input1.yaml'

data = dict()
	
with open(file_name_csv, 'r') as csvfile:
	d_reader = csv.DictReader(csvfile)
	dict_list = []
	headers = d_reader.fieldnames
	print(headers)

	for x in d_reader:
		dict_list.append(x)

	with open(file_name_json, 'w') as f_json:
		json.dump(dict_list, f_json)

    with open(file_name_yaml, 'w') as f_yaml:
		output = yaml.dump(dict_list, default_flow_style=False, explicit_start=True)
		yaml.dump(dict_list, f_yaml)

with open(file_name_yaml, 'r') as f_yaml:
	yaml_str = yaml.load(f_yaml)
	print(type(yaml_str))
'''