from .Animal import Animal

class Alien(Animal):

	def __init__(self, alien=None, position=None, world=None):
		super(Alien, self).__init__(alien, position, world)

	def clone(self):
		return Alien(self, None, None)

	def initParams(self):
		self.power = 0
		self.initiative = 20
		self.liveLength = 10
		self.powerToReproduce = 9
		self.sign = 'A'

	def getNeighboringPositions(self):
		self.power -= 1
		self.liveLength += 1
		return self.world.filterFreePositions(self.world.allPositions())
