class OddInf:
	def __init__(self):
		self.num=1
	def __iter__(self):
		return self
	def __next__(self):
		data=self.num
		self.num=self.num+2
		return data
if __name__ == '__main__':
	d=OddInf()
	print(next(d))
	print(next(d))
	print(next(d))
	print(next(d))
	print(next(d))