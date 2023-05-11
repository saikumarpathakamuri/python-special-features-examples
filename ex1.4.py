from itertools import islice
lst=[10,20,30,40,50,60]
my_iter=iter(lst)
for i in islice(lst,0,7):
	print(i)
for i in islice(lst,0,7):
	print(my_iter.__next__())
