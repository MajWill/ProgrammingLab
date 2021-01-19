class ExamException(Exception):
    pass

class Diff:

    def __init__(self,ratio=1):
        if((isinstance(ratio, int))==False or ratio<=0):
            raise ExamException("Errore valore di ratio")
        else:
            self.ratio=ratio

    def compute(self, lista):
        controllo = isinstance(lista, list)
        if(lista==None or controllo!=True or len(lista)==0):
            raise ExamException("Errore: lista vuota o errata")
        elif(len(lista)<2):
            raise ExamException("Errore: la lista non soddisfa la lunghezza minima di 2")
        else:
            valori = []
            lung = len(lista) - 1
            for i in range(lung):
                if((isinstance(lista[i],(int,float))==True)) and ((isinstance(lista[i+1],(int,float)))==True):
                    valori.append(float((lista[i+1]-lista[i])/self.ratio))
                else:
                    raise ExamException("Errore: tipo non numerico all'interno della lista")
            return valori

diff = Diff()
result = diff.compute([2,4,8,16])
print(result)
            
