import itertools
letters=["a",'b','c','d']
numbers=[1,2,3]
names=["sandesh","suhas","akash","nuthan","sagar"]
result=itertools.permutations(numbers)
print(result)
for i in result:
	print(i)
result=itertools.combinations_with_replacement(numbers,2)
for i in result:
	print(i)
