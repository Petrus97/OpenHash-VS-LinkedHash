class CollisionCounter(object):
	def __init__(self, name):
		self._collision = 0
		self.name = name

	def update(self):
		#print("Collision detected by ", self.name)
		self._collision += 1
	
	def get_collision(self):
		return self._collision

	def reset_counter(self):
		self._collision = 0

	def printNumberCollision(self):
		print("Number of collison detected by ",self.name," are: ", self._collision)


