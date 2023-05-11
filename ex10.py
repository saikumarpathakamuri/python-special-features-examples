class RemoteControl:
	def __init__(self):
		self.channels=["public tv","HBO","tv9","pogo"]
if __name__ == '__main__':
	r=RemoteControl()
	iter_r=iter(r.channels)
	while True:
		try:
			print(next(iter_r))
		except StopIteration:
			break
			