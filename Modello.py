class CSVFile:

    def __init__(self, nome):
        self.nome = nome

    def get_data(self, start=None, end=None):
        valori = [] #creo una lista per i valori
        if(isinstance(self.nome, str)!= True):
            raise Exception('il nome del file non è una stringa')

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
        elif(start>end or start<1):
            return "Valori incorretti per restituzione dati"
        else:
            try:
                return valori[start-1:end]
            except Exception as e:
                print(e)

class Model(object):

    def fit(self, data):
        pass

    def predict(self):
        pass

class IncrementModel(Model):

    def fit(self, data):
        raise NotImplementedError('Questo modello non prevede un fit')

    def predict(self, prev_months):
        if not isinstance(prev_months, list):
            raise Exception('Errore: prev_months non di tipo lista')
        if len(prev_months) <= 2:
            raise Exception('Errore: lunghezza di prev_months non sufficiente, servono almeno due elementi per calcolare un incremento')
        n_months = len(prev_months)
        increments = 0
        for i in range(n_months):
            if i == 0:
                continue
            else:
                increments += prev_months[i] - prev_months[i-1]
        avg_increment = increments / (n_months-1)
        return prev_months[-1] + avg_increment


#-------------------
#corpo del programma
#-------------------
prova_file = CSVFile('shampoo_sales.csv')
print(prova_file.get_data(1,4))
Modello = IncrementModel()
print("Prevedo: {}".format(Modello.predict(prova_file.get_data(1,3))))