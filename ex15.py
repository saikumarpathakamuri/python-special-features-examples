from functools import wraps 
def decorator(func):
	@wraps(func)
	def inner():
		mystring=func()
		return mystring.upper()
	return inner
@decorator
def wish():
	return "hi sandesh how are you"
if __name__ == '__main__':
	print(wish())
	print(wish.__name__)