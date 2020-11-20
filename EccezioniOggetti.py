class CSVFile:

    def __init__(self, nome):
        self.nome = nome

    def get_data(self):
        valori = [] #creo una lista per i valori
        my_file = open(self.nome, 'r') #apro il file
        for line in my_file: #ciclo le righe
            elementi = line.split(',') #separo i valori
            if elementi[0] != 'Date':  #prendo data e                                   vendite
                try:
                    date = elementi[0]
                    value= elementi[1]
                #aggiungo solo le vendite alla list dei valori
                    valori.append(float(value)) 
                except ValueError:
                    print("Errore nella riga ({}) perchè valore incorretto".format(line))
                
#chiudo il file
        my_file.close()        
        return valori

prova_file = CSVFile('shampoo_sales.csv')
try:
    print(prova_file.get_data())
except Exception as e:
    print("Impossibile aprire il file")