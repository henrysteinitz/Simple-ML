from torch import nn

class Model(nn.Module):
	def __init__(self, **kwargs):
		super.__init__()
		self.init_parameters(**kwargs)
		self.init_hyperparameters(**kwargs)
		if 'data' in kwargs:
			self.train(**kwargs)

	def init_parameters(self, **kwargs):
		raise NotImplementedError

	def init_hyperparameters(self, **kwargs):
		raise NotImplementedError

	def train(self, **kwargs):
		raise NotImplementedError

	def run(self, x):
		raise NotImplementedError

	def loss(self, y_data, y_model):
		raise NotImplementedError

	def forward(self, x):
		self.run(x)