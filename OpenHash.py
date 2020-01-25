import CollisionCounter


class OpenHash(object):
	def __init__(self, table_size):
		self._observers = []
		self.table_size = table_size
		self.table = [None] * self.table_size

	def hash_function(self, value):
		#Division method
		key = value % self.table_size
		return key

	def hash_insert(self, value):
		i = 0
		j = self.linear_probing_hash(value, i)
		while i != self.table_size :
			if self.table[j] == None or self.table[j] == "DEL" :
				self.table[j] = value
				return j
			#new part
			elif self.table[j] != None or self.table[j] != "DEL":
				self.notify()
			i = i + 1
			j = self.linear_probing_hash(value, i)

	def hash_search(self, value):
		i = 0
		j = self.linear_probing_hash(value, i)
		while i == self.table_size :
			if self.table[j] == value :
				return j 
			i = i + 1
			j = self.linear_probing_hash(value, i) 
		return None

	def hash_delete(self, value):
		i = 0
		j = self.linear_probing_hash(value, i)
		while i != self.table_size :
			if self.table[j] == value:
				self.table[j] = "DEL"
				return
			i = i + 1
			j = self.linear_probing_hash(value, hash)

	def linear_probing_hash(self, value, index):
		key = self.hash_function(value)
		new_key = (key + index) % self.table_size
		return new_key

	def empty_table(self):
		self.table = [None] * self.table_size

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
