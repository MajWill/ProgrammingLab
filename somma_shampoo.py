somma = 0 #variabile per calcolare la somma
valori = [] #variabile per valori delle vendite

#apro e leggo il file linea a linea
my_file = open("shampoo_sales.csv", "r")
for line in my_file:
    elementi = line.split(',')#splitto sulla virgola

    #separo data e valore
    if elementi[0] != 'Date':
        date = elementi[0]
        value= elementi[1]

        #aggiungo alla mia lista solo i valori
        valori.append(float(value))

#eseguo la somma delle vendite
for vendita in valori:
    somma+=vendita

print("la somma delle vendite e': {}".format(somma))



