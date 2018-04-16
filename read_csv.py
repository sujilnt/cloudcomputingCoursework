import csv
import pprint 
pp = pprint.PrettyPrinter(indent=2)
reader = csv.DictReader(open('sample.csv', 'rb'))
dict_list = []

for line in reader:
	dict_list.append(line)

print dict_list
pp.pprint(dict_list)