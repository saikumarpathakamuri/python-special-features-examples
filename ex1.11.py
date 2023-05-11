import itertools
data=itertools.islice(range(7),5)
print(data)
for i in data:
	print(i)
data=itertools.islice(range(7),2,6)
print(data)
for i in data:
	print(i)
data=itertools.islice(range(7),1,6,2)
print(data)
for i in data:
	print(i)