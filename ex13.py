
class Topten:
	def __init__(self,limit):
		self.num=10
		self.limit=limit
	def __iter__(self):
		return self
	def __next__(self):
		
		if self.num>=self.limit:
			raise StopIteration

		else:
			self.num=self.num+1
			return self.num
if __name__ == '__main__':
	c=Topten(limit=19)
	while True:
		try:
			print(next(c))
		except StopIteration:
			break
	'''print(next(c))
	for i in c:
		print((i))'''
#	print(next(c))