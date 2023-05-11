import itertools
def get_data(person):
	return person["state"]

people=[{"name":"sandesh","city":"mysore","state":"karnataka"}
,{"name":"saikumarpathakamuri","city":"mysore","state":"hyd"},
{"name":"sanketh","city":"mangalore","state":"karnataka"}]


my_data=itertools.groupby(people,get_data)
for i,j in my_data:
	print(i,len(list(j)))
	print(list(j))