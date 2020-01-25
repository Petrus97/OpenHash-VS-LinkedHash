import OpenHash
import LinkedHash
import CollisionCounter
import pandas as pd
import random
import time


def insert_test():
	print("Hash table with m=373")
	hash = OpenHash.OpenHash(373)
	l_hash = LinkedHash.LinkedHash(373)
	collision_counter = CollisionCounter.CollisionCounter("OpenHash Collision Counter")
	l_collision_counter = CollisionCounter.CollisionCounter("LinkedHash Collision Counter")
	hash.attach(collision_counter)
	l_hash.attach(l_collision_counter)
	df = pd.DataFrame(columns = ['Fattore di caricamento','OpenHash', 'HashCollision', 'LinkedHash', 'L_HashCollision'])
	charge_factor = [0.25, 0.50, 0.75, 0.90]
	df["Fattore di caricamento"] = charge_factor
	collisions = []
	l_collisions = []
	elapsed = []
	l_elapsed = []
	#OpenHash
	for alpha in charge_factor:
		n = 0
		start = time.perf_counter()
		while n/hash.table_size <= alpha:
			hash.hash_insert(random.randrange(0, 10000))
			n += 1
		end = time.perf_counter()
		elapsed.append(end - start)
		collisions.append(collision_counter.get_collision())
		collision_counter.reset_counter()
		hash.empty_table()
	#LinkedHash
	for alpha in charge_factor:
		n = 0
		start = time.perf_counter()
		while n/l_hash.table_size <= alpha:
			l_hash.linked_insert(random.randrange(0, 10000))
			n += 1
		end = time.perf_counter()
		l_elapsed.append(end - start)
		l_collisions.append(l_collision_counter.get_collision())
		l_collision_counter.reset_counter()
		l_hash.empty_table()
	df["OpenHash"] = elapsed
	df["LinkedHash"] = l_elapsed
	df["HashCollision"] = collisions
	df["L_HashCollision"] = l_collisions
	print(df)

def search_test():
	m = 97
	hash = OpenHash.OpenHash(m)
	l_hash = LinkedHash.LinkedHash(m)
	collision_counter = CollisionCounter.CollisionCounter("OpenHash Collision Counter")
	l_collision_counter = CollisionCounter.CollisionCounter("LinkedHash Collision Counter")
	hash.attach(collision_counter)
	l_hash.attach(l_collision_counter)
	df = pd.DataFrame(columns = ['Numero','OpenHash', 'LinkedHash'])
	charge_factor = [0.90]#[0.25, 0.50, 0.75, 0.90]
	numbers = [29, 220, 399, 13, 69] #test numbers
	hash_time = []
	l_hash_time = []
	df["Numero"] = numbers
	for alpha in charge_factor:
		n = 0
		while n/m <= alpha:
			x = random.randrange(0, 400)
			hash.hash_insert(x)
			l_hash.linked_insert(x)
			n += 1
		for element in numbers:
			#OpenHash
			start = time.perf_counter()
			found = hash.hash_search(element)
			if found != None:
				end = time.perf_counter()
				hash_time.append(start - end)
			else: 
				end = time.perf_counter()
				hash_time.append("Not found")
			#LinkedHash
			start_l = time.perf_counter()
			l_found = l_hash.linked_search(element)
			if l_found != None:
				end_l = time.perf_counter()
				l_hash_time.append(start_l - end_l)
			else: 
				end_l = time.perf_counter()
				l_hash_time.append("Not found")
		df["OpenHash"] = hash_time
		df["LinkedHash"] = l_hash_time
		print("Table with charge factor =", alpha)
		print(df)
		hash_time = []
		l_hash_time = []
		hash.empty_table()
		l_hash.empty_table()