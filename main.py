import LinkedHash
import OpenHash
import CollisionCounter
import performance_test as pt
'''
Vogliamo capire qual è il comportamento delle tabelle hash al
crescere del fattore di caricamento α = n/m
Per fare questo scriveremo:
-> Un programma che implementa le tabelle hash con gestione delle
   collisioni basate su concatenamento e su indirizzamento aperto
   (ispezione lineare)
----> La funzione hash deve essere calcolata col metodo delle divisioni
-> Oltre al costruttore devono essere implementati inserimento,
   cancellazione e ricerca per i due metodi
-> Un programma che conta quante collisioni si hanno eseguendo un
   numero variabile di inserimenti in una tabella hash
-> Un programma che esegue gli esperimenti
-> Una relazione
'''
def main():
	#l_hash = LinkedHash.LinkedHash(10)
	#l_hash.linked_insert(15)
	#l_hash.linked_insert(12)
	#l_hash.linked_insert(2)
	#l_hash.linked_insert(22)
	#l_hash.linked_insert(32)
	#l_hash.linked_insert(42)
	#l_hash.linked_delete(12)
	#l_hash.linked_delete(42)
	#if l_hash.linked_search(32) != None:
	#	print("TROVATO")
	#l_hash.print_table()
	#hash =  OpenHash.OpenHash(13)
	##collision_counter = CollisionCounter.CollisionCounter("OpenHash counter")
	##hash.attach(collision_counter)
	#hash.hash_insert(43)
	#hash.hash_insert(85)
	#hash.hash_insert(91)
	#hash.hash_insert(67)
	#hash.hash_insert(78)
	#hash.hash_insert(30)
	#hash.hash_insert(16)
	#hash.hash_insert(9)
	#hash.hash_insert(18)
	#hash.hash_delete(43)
	#found = hash.hash_search(31) 
	#if found != None:
	#	print("############TROVATO in posizione:", found)
	#else: print("Not found")
	#print("Ora inserisco il 4")
	#hash.hash_insert(4)
	#hash.print_table()
	#collision_counter.printNumberCollision()
	#pt.insert_test()
	#pt.search_test() FIXME


main()
