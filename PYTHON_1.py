#ESERCIZIO 1
#Abbiamo la stringa: nome_scuola = "Epicode" Stampare ogni carattere della stringa, 
#uno su ogni riga, utilizzando un costrutto while.

nome_scuola = "Epicode"
indice = 0
while indice < len(nome_scuola):
    print(nome_scuola[indice])
    indice += 1

#ESERCIZIO 2
#Stampare a video tutti i numeri da 0 a 20 utilizzando il costrutto while.

numero = 0
while numero <= 20:
    print(numero)
    numero += 1

#ESERCIZIO 3
#Calcolare e stampare tutte le prime 10 potenze di 2 (e.g., 2⁰, 2¹, 2², …) utilizzando un ciclo while.
    
esponente = 0
limite_esponente = 10
while esponente < limite_esponente:
    risultato = 2 ** esponente
    print(f"2^{esponente} = {risultato}")
    esponente += 1

#ESERCIZIO 3
#Calcolare e stampare tutte le prime N potenze di 2 utilizzando un ciclo while, domandando all'utente di inserire N.

N = int(input("inserisci il valore di N: "))
esponente = 0
while esponente < N:
    risultato = 2 ** esponente
    print(f"2^{esponente} = {risultato}")
    esponente += 1

#ESERCIZIO 4
#Calcolare e stampare tutte le potenze di 2 minori di 25000.

limite = 25000
esponente = 0
while 2 ** esponente < limite:
    print(f"2^{esponente} = {2 ** esponente}")
    esponente += 1

#ESERCIZIO 5
#Abbiamo due liste, una di studenti e una di corsi: 
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

#Aggiungere i dati mancanti alla lista corsi, sapendo che Emma segue Data Analyst Faith segue Backend Grace segue Frontend Henry segue Cybersecurity 
#Aggiungeremo i dati mancanti uno alla volta con il metodo per appendere in coda alle liste, poi verificheremo che sono della stessa lunghezza e se lo sono stamperemo la lista corsi. Se alcuni dati sono già presenti non vanno aggiunti 

corsi.append("Frontend")
corsi.append("Cybersecurity")

if len(studenti) == len(corsi):
    print("Le liste sono della stessa lunghezza.")
    print("Lista Corsi:", corsi)
else:
    print("Le liste non sono della stessa lunghezza.")

#ESERCIZIO 6
#Scriviamo un programma che chiede in input all'utente una stringa e visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri 
#(Stavolta facciamo attenzione a tutti i casi particolari, ovvero implementare soluzioni ad hoc per stringhe di lunghezza inferiore a 6 caratteri)

input_stringa = input("Inserisci una stringa: ")
lunghezza_stringa = len(input_stringa)
if lunghezza_stringa < 6:
    print("Errore: La stringa deve avere almeno 6 caratteri.")
else:
    primi_3 = input_stringa[:3]
    ultimi_3 = input_stringa[-3:]
    risultato = primi_3 + "..." + ultimi_3
    print("Risultato:", risultato)

#ESERCIZIO 7
#Memorizza e stampa tutti i divisori di un numero dato in input. Esempio: • input: 150 • output: [2, 3, 5, 5]

numero = int(input("inserisci un numero: " ))
divisori = []
indice = 2
while indice <= numero:
    if numero % indice == 0:
        divisori.append(indice)
    indice += 1 
print(f"I divisori di {numero} sono: {divisori}")

#ESERCIZIO 8
#Calcolare (ma non stampare) le prime N potenze di K; ognuna di esse andrà memorizzata in coda a una lista. 
#Alla fine, stampare la lista risultante. Proviamo con diversi valori di K, oppure facciamola inserire all'utente.

K = int(input("inserisci valore di K: "))
N = int(input("Inserisci il valore di N: "))
potenze = []
esponente = 0
while esponente < N:
    potenza = K ** esponente
    potenze.append(potenza)
    esponente += 1
print(f"Le prime {N} potenze di {K} sono: {potenze}")

#ESERCIZIO 9
#Abbiamo una lista con i guadagni degli ultimi 12 mesi: 
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
#usando un costrutto while, calcolare la media dei guadagni e stamparla a video.
somma_guadagni = 0
conteggio_mesi = 0
while conteggio_mesi < len(guadagni):
    somma_guadagni += guadagni[conteggio_mesi]
    conteggio_mesi += 1
if conteggio_mesi > 0:
    media_guadagni = somma_guadagni / conteggio_mesi
    print(f"La media dei guadagni degli ultimi 12 mesi è: {media_guadagni}")
else:
    print("La lista dei guadagni è vuota.")

