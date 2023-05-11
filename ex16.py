def verifyname(method):
	def inner(self):
		if self.name=="Sandesh":
			print("python trainer name is : ",self.name)
			print(f"{self.name} is one of the trainer in ABC")
		else:
			method(self)
	return inner
class python :
	def __init__(self,name):
		self.name=name
	@verifyname
	def trainer_name(self):
		print("python trainer name is : ",self.name)
if __name__ == '__main__':
	d=python("Sandesh")
	d.trainer_name()
	d1=python("Rishi")
	d1.trainer_name()