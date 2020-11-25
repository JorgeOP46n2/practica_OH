import random


class EA(object):

	"""docstring for EA"""

	def __init__(self, function, mybounds, number):
			#super(EA, self).__init__()
		self.function=function
		self.mybounds=mybounds
		self.number=number
		conjunto_x=[]
		self.generacion=[]
		self.best=None


		for i in range(number):
			min=mybounds[i % len(mybounds)].__getitem__(0)
			max=mybounds[i % len(mybounds)].__getitem__(1)
			conjunto_x.append(min + random.random() * (max - min))

		self.generacion[0] = conjunto_x



	def run(self,iteraciones):


		for i in range(iteraciones):








	def best(self):
		return self.best()

