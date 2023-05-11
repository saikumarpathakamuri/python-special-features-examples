import itertools
letters=["a",'b','c','d']
numbers=[1,2,3]
names=["sandesh","suhas","akash","nuthan","sagar"]
result=itertools.chain(letters,numbers,names)
for i in result:
	print(i)