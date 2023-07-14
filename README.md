# Refactor

E' davvero così importante scrivere codice efficente ed implementare un efficente algoritmo? 
Quanto questi due fattori possono influenzare sull'eseguibilità del programma?

L'obbiettivo di questo progetto è quello di rispondere a queste due domande sviluppando varie versioni dell'algoritmo che calcola i numei primi più piccoli di un determinato numeo


version1.py: l'algoritmo implementato in questo script va a ciclare su tutti i numeri minori di n per poi cercare quali di essi abbiano divisori oltre ad essi stessi e 1

version2.py: stesso algoritmo semplicemente utilizza delle list comprehension (più veloci)

version3.py: essendo tutti i numeri pari > di 2 multipli di 2 sicuramente non sono primi inoltre se un numero non ha divisori più piccoli della sua radice quadrata
allora è primo. Questo algoritmo utilizza la stessa logica del precedente semplicemente cicla esclusivamente sui dispari e il secondo ciclo viene effettuato esclusviamente
sui dispari più piccoli della radice del numeroù


version4.py: prima versione del crivello di eratostene. Dopo aver creato un set contenente tutti i numeri dispari minori di n gli sottrae iterativamente i multipli di 
tutti i numeri primi (3 è presente nel set ? si, allora tolgo tutti i multipli di 3, 5? stessa cosa, 7? stessa cosa, 9? non è presente perchè multiplo di 3 ......)

version5.py: questo algoritmo invece di cancellare dal set tutti i multipli crea due liste, uno per i multipli e una per i numeri primi 
(tutti i numeri non presenti nei multipli). Iterativamente cicla sui dispari più piccoli di n e se non presenti in multipli li inserisce in numeri_primi e inserisce in
multipli i suoi multipli


version6.py : partendo da un arrey di booleani di lunghezza n, setta a false i mutlipli di ogni valore True e considera esclusivamente i valori True
