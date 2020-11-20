class CSVFile:

    def __init__(self, nome):
        self.nome = nome

    def get_data(self):
        valori = []
        my_file = open(self.nome, 'r')
        for line in my_file:
            elementi = line.split(',')
            if elementi[0] != 'Date':
                date = elementi[0]
                value= elementi[1]
                valori.append(float(value))
        my_file.close()        
        return valori

prova_file = CSVFile('shampoo_sales.csv')
print(prova_file.get_data())
