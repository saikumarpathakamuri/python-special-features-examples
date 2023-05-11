class RemoteControl:
	def __init__(self):
		self.channels=["public tv","HBO","tv9","pogo"]
		self.index=-1
	def __iter__(self):
		return self
	def __next__(self):
		self.index=self.index+1
		if self.index==len(self.channels):
			raise StopIteration
		return self.channels[self.index]


if __name__ == '__main__':
	iter_r=RemoteControl()
	while True:
		try:
			print(next(iter_r))
		except StopIteration:
			break
			