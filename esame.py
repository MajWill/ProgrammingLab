class ExamException(Exception):
    pass

class MovingAverage:

    def __init__(self, window):
        self.fin = window

    def compute(self, lista):
        controllo = isinstance(lista, list)
        if(len(lista)==0 or lista==None or controllo!=True):
            raise ExamException("Errore: lista vuota")
        elif(len(lista)<self.fin or self.fin<=0):
            raise ExamException("Errore:  la finestra supera la lista oppure è nulla")
        else:
            valori = []
            lung = len(lista) - self.fin + 1
            for i in range(lung):
                finestra = lista[i:i+self.fin]
                #print(finestra)
                somma = 0
                for j in range(len(finestra)):
                    somma = somma + finestra[j]
                valori.append(float(somma/self.fin))
            return valori

moving_average = MovingAverage()
result = moving_average.compute([2,4,8,16])
print(result)