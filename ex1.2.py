import itertools
data=[100,200,300,400]
my_data=list(zip(itertools.count(start=1),data))
print(my_data)


my_data1=list(itertools.zip_longest(range(10),data))
print(my_data1)
