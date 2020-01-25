import CollisionCounter


class LinkedHash(object):
	def __init__(self, table_size):
		self._observers = []
		self.table_size = table_size
		self.table = [None] * self.table_size
		for key in range(self.table_size):
			self.table[key] = [] #dovrei creare un dizionario vuoto
	
	def hash_function(self, value):
		#Division method
		key = value % self.table_size
		return key

	def linked_insert(self, value):
		key = self.hash_function(value)
		if self.table[key] != []:
			self.notify()
		self.table[key].insert(0, value)

	def linked_search(self, value):
		key = self.hash_function(value)
		for elements in self.table[key]:
			if elements == value:
				return self.table[key].index(value)
		return None

	def linked_delete(self, value):
		key = self.hash_function(value)
		self.table[key].remove(value)

	def empty_table(self):
		self.table = [None] * self.table_size
		for key in range(self.table_size):
			self.table[key] = [] #dovrei creare un dizionario vuoto

	def print_table(self):
		for key in range(self.table_size):
			print(key, self.table[key])

	#Observer methods
	def attach(self, observer: CollisionCounter):
		self._observers.append(observer)

	def detach(self, observer: CollisionCounter):
		self._observers.remove(observer)

	def notify(self):
		for obs in self._observers:
			obs.update()

	_observers = []


