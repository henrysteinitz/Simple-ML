

class Classifier:

	def __init__(self, data=None, labels=None, **hyperparameters):
		self.parameters = list(self.define_parameters())
		self.hyperparameters = # merge hyperparameters with defaults
		if data != None and labels != None:
			self.train(data=data, labels=labels)

	def train(self, data, labels):


	def step(self):
		for p in parameters:

	def define_parameters():
		raise NotImplementedError

	def run(self, x):
		raise NotImplementedError

	def batch_run(self, x):
		raise NotImplementedError

	def loss(self, x):
		
		
	def __call__():
		self.run(*x)