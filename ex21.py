class checkdiv:
	def __init__(self,func):
		self.func=func
	def __call__(self,*args,**kwargs):
		r=[]
		r=args[1:]
		for i in r:
			if i==0:
				return "division is not possible"
			else:
				return self.func(*args,**kwargs)
@checkdiv
def div(a,b):
	return a/b
@checkdiv
def div1(a,b,c):
	return a/b/c
if __name__ == '__main__':
	print(div(10,2))
	print(div(10,0))
	print(div1(10,2,0))