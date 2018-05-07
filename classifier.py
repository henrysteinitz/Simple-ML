from torch import nn

class Classifier(nn.Module):

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

	def loss(self, y_data, y_model):
		# cross entropy by default
		return y_data * log(y_model) + (1 - y_data) * log(1 - y_model)
		
	def __call__(self, x):
		self.run(*x)