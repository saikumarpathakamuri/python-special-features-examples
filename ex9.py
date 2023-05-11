dic={"name":"sandesh","subject":"python","framework":"Django"}
iter_dic=iter(dic)
while True:
	try :
		#print(next(iter_dic))
		print(iter_dic.__next__())
	except StopIteration:
		break