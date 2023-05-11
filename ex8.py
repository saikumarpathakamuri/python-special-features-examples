my_set={"Sandesh","suhas","akash","rahman","bala"}
print(my_set)
for i in my_set:
	print(i)
iter_set=iter(my_set)
print(iter_set)
print(next(iter_set))
print(next(iter_set))
print(next(iter_set))
print(next(iter_set))
print(next(iter_set))



while True:
	try :
		print(next(iter_set))
	except StopIteration:
		break