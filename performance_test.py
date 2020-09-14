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
	print("Tabella hash di dimensione m = " + str(m))
	# Init hash tabels
	hash = OpenHash.OpenHash(m)
	l_hash = LinkedHash.LinkedHash(m)
	collision_counter = CollisionCounter.CollisionCounter("OpenHash Collision Counter")
	l_collision_counter = CollisionCounter.CollisionCounter("LinkedHash Collision Counter")
	# Attach to observe CollisionCounter
	hash.attach(collision_counter)
	l_hash.attach(l_collision_counter)
	df = pd.DataFrame(columns = ['α','Indirizzamento aperto', 'N° Collisioni IA', 'Concatenamento', 'N° Collisioni C'])
	charge_factor = []
	alpha = 0.1
	while alpha <= 1:
		charge_factor.append('%.2f'%alpha)
		alpha += 0.05
	charge_factor.append('0.98')
	charge_factor.append('0.99')
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
	df['Indirizzamento aperto'] = elapsed
	df['Concatenamento'] = l_elapsed
	df['N° Collisioni IA'] = collisions
	df['N° Collisioni C'] = l_collisions
	print(df)
	plt.xlabel("Fattore di caricamento α")
	plt.ylabel("Numero di collisioni")
	plt.figure(figsize=(12.80, 7.2))
	plt.plot(df["α"], collisions, marker="o")
	plt.plot(df["α"], l_collisions, marker="o")
	plt.legend(['indirizzamento aperto', 'concatenamento'], loc='upper left')
	# plt.title("Collision number")
	# plt.suptitle("OpenHash vs LinkedHash")
	namefile = "collision_test_on_" + str(m) + "_table"
	plt.savefig('figures/' + namefile + ".png")
	plt.clf()
	df.to_latex("results/" + namefile + ".tex", index=False, column_format='|l|l|l|l|')
	list_len = len(df['N° Collisioni C'])
	# avg_insert_time = 1.5269999999985018e-06
	straight_line_x = [df['N° Collisioni C'][0], df['N° Collisioni C'][list_len-1]]
	straight_line_y = [df['Concatenamento'][0], df['Concatenamento'][list_len-1]]
	# straight_line_x = [0, avg_insert_time * m * 0.99]
	# straight_line_y = [0, avg_insert_time * m * 0.99]
	plt.xlabel('Numero collisioni')
	plt.ylabel('Tempo inserimento')
	plt.plot(df['N° Collisioni C'], df['Concatenamento'], marker="o")
	plt.plot(straight_line_x, straight_line_y)
	plt.savefig('linear/' + namefile + ".png")

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