import OpenHash
import LinkedHash
import CollisionCounter
import pandas as pd
import matplotlib.pyplot as plt
import random
import time
import os
import pickle


def insert_test(m):
	print("Hash table with m = " + str(m))
	# Init hash tabels
	hash = OpenHash.OpenHash(m)
	l_hash = LinkedHash.LinkedHash(m)
	collision_counter = CollisionCounter.CollisionCounter("OpenHash Collision Counter")
	l_collision_counter = CollisionCounter.CollisionCounter("LinkedHash Collision Counter")
	# Attach to observe CollisionCounter
	hash.attach(collision_counter)
	l_hash.attach(l_collision_counter)
	df = pd.DataFrame(columns = ['α','OpenHash', 'HashCollision', 'LinkedHash', 'L_HashCollision'])
	charge_factor = []
	alpha = 0.1
	while alpha <= 1:
		charge_factor.append('%.2f'%alpha)
		alpha += 0.05
	df["α"] = charge_factor
	collisions = []
	l_collisions = []
	elapsed = []
	l_elapsed = []
	values = [] # extract from file the values and put in this array
	file_name = "db/file_test_" + str(m) + ".pickle"
	with open(file_name, "rb") as file_test:
		count = 0
		while count < m:
			try:
				values.append(pickle.load(file_test)) # load values 
				count += 1
			except EOFError:
				break
	#OpenHash
	for alpha in charge_factor:
		n = 0
		start = time.perf_counter()
		while n/hash.table_size <= float(alpha):
			hash.hash_insert(values[n])
			n += 1
		end = time.perf_counter()
		elapsed.append('%.4f'%(end-start))
		collisions.append(collision_counter.get_collision())
		collision_counter.reset_counter()
		hash.empty_table()
	#LinkedHash
	for alpha in charge_factor:
		n = 0
		start = time.perf_counter()
		while n/l_hash.table_size <= float(alpha):
			l_hash.linked_insert(values[n])
			n += 1
		end = time.perf_counter()
		l_elapsed.append('%.4f'%(end-start))
		l_collisions.append(l_collision_counter.get_collision())
		l_collision_counter.reset_counter()
		l_hash.empty_table()
	df["OpenHash"] = elapsed
	df["LinkedHash"] = l_elapsed
	df["HashCollision"] = collisions
	df["L_HashCollision"] = l_collisions
	print(df)
	plt.xlabel("Charging factor α")
	plt.ylabel("Number of collisions")
	plt.figure(figsize=(12.80, 7.2))
	plt.plot(df["α"], collisions, marker="o")
	plt.plot(df["α"], l_collisions, marker="o")
	plt.legend(['open hash', 'linked hash'], loc='upper left')
	plt.title("Collision number")
	plt.suptitle("OpenHash vs LinkedHash")
	namefile = "collision_test_on_" + str(m) + "_table"
	plt.savefig('figures/' + namefile + ".png")
	plt.clf()
	df.to_latex("results/" + namefile + ".tex")


'''
This function generate values for evaluate the insert test
'''
def generate_values(table_dim):
	file_name = "db/file_test_" + str(table_dim) + ".pickle"
	file = open(file_name, 'wb+')
	for i in range (0, table_dim):
		pickle.dump(random.randrange(0, 10000), file)
	file.close()

def start_test():
	print("Start testing")
	prime_numbers = [373, 1499, 3733, 6277, 7603, 14011, 19181] # selected prime numbers
	try:
		os.mkdir("db")
	except FileExistsError:
		print("Directory already exist")
		pass
	if(len(os.listdir("db")) == 0): # init the db files
		for m in prime_numbers:
			generate_values(m)
	for m in prime_numbers:
		insert_test(m)		# call insert test for all prime numbers