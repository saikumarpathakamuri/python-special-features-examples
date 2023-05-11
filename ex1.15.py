from itertools import islice
class fibo:
	def __init__(self):
		self.prev=0
		self.curr=1
		print(self.prev)
		print(self.curr)
	def __iter__(self):
		return self
	def __next__(self):
		self.prev,self.curr=self.curr,self.prev+self.curr
		return self.curr
if __name__ == '__main__':
	d=fibo()
	print(next(d))
	print(next(d))
	print(next(d))
	print(next(d))
	print(next(d))
	print(next(d))