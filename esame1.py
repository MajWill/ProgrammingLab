class ExamException(Exception):
    pass

class MovingAverage:

    def __init__(self, window):
        if((isinstance(window, int))==False or window<=0):
            raise ExamException("Errore valore della finestra")
        else:
            self.fin = window

    def compute(self, lista):
        controllo = isinstance(lista, list)
        if(lista==None or controllo!=True or len(lista)==0):
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
                    if ((isinstance(finestra[j],(int,float)))==True):
                        somma = somma + finestra[j]
                    else:
                        raise ExamException("Errore: tipo non numerico")
                valori.append(float(somma/self.fin))
            return valori

#moving_average = MovingAverage()
#result = moving_average.compute([2,4,8,16])
#print(result)