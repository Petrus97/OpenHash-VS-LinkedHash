# OpenHash-VS-LinkedHash

Vogliamo capire qual è il comportamento delle tabelle hash al
crescere del fattore di caricamento `α = n/m` <br>
Per fare questo scriveremo:
- Un programma che implementa le tabelle hash con gestione delle
   collisioni basate su concatenamento e su indirizzamento aperto
   (ispezione lineare) <br>
   - La funzione hash deve essere calcolata col metodo delle divisioni
- Oltre al costruttore devono essere implementati inserimento,
   cancellazione e ricerca per i due metodi
- Un programma che conta quante collisioni si hanno eseguendo un
   numero variabile di inserimenti in una tabella hash
- Un programma che esegue gli esperimenti
- Una relazione

`TODO` Da aggiungere in relazione questa osservazione: Il numero di collisioni di OpenHash è >> LinkedHash perchè ogni volta che trova/avviene una collisione va alla posizione successiva, se c'è collisione la conta e va a quella successiva ancora ecc...