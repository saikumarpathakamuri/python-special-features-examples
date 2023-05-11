class python:
	def __init__(self,func):
		self.func=func
	def __call__(self):
		mystring=self.func()
		return mystring.upper()


@python
def wish():
	return "hi Sandesh"
if __name__ == '__main__':
	print(wish())