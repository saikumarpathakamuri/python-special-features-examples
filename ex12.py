
class Topten:
	def __init__(self):
		self.num=1
	def __iter__(self):
		return self
	def __next__(self):
		
		if self.num<10:
			data=self.num
			self.num=self.num+1
			return data
		else:
			raise StopIteration




if __name__ == '__main__':
	c=Topten()
	while True:
		try:
			print(next(c))
		except StopIteration:
			break
	'''print(next(c))
	for i in c:
		print((i))'''