class CSVFile:

    def __init__(self, nome):
        self.nome = nome

    def get_data(self, start=None, end=None):
        valori = [] #creo una lista per i valori
        if(isinstance(self.nome, str)!= True):
            raise Exception('il nome del file non è una stringa')
            return 0

        try:
            my_file = open(self.nome, 'r') #apro il file
        except Exception as e:
            print("Impossibile aprire il file")
            return None
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
        if(start==None and end==None):
            return valori
        elif(start>end):
            return "Valori incorretti per restituzione dati"
        else:
            try:
                return valori[start:end+1]
            except Exception as e:
                print(e)

prova_file = CSVFile('shampoo_sales.csv')
try:
    print(prova_file.get_data(7, 5))
except Exception as e:
    print(e)