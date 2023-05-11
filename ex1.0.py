import itertools
lst1=[10,20,30,40]
lst2=[50,60,70,80]
itr1=iter(lst1)
itr2=iter(lst2)
itr3=itertools.chain(lst1,lst2)
print(itr3)
print(next(itr3))
print(next(itr3))
print(next(itr3))
print(next(itr3))
print(next(itr3))
print(next(itr3))
print(next(itr3))
print(next(itr3))