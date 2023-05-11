class checkdiv:
	def __init__(self,func):
		self.func=func
	def __call__(self,*args,**kwargs):
		if args[1]==0:
			print("division is not possible")
		else:
			self.func(*args,**kwargs)
@checkdiv
def div(a,b):
	print(a/b)
if __name__ == '__main__':
	div(10,2)
	div(10,0)