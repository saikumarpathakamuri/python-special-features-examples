
class python :
	def __init__(self,name):
		self.name=name
	def __call__(self):
		print("python trainer name is : ",self.name)
if __name__ == '__main__':
	d=python("Sandesh")
	d()