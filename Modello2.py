# I dati delle mie vendite di shampoo. In questo caso le sto direttamente scrivendo nel codice,
# ma nella realta' avrei usato l'oggetto CSVFile e caricato i dati dal file. Ma cosi' evito di
# avere troppe cose su cui sto lavorando assieme, e visto che i dati sono piccoli, posso farlo
# ed e' comodo (se avevo migliaia di valori forse era meglio di no).

shampoo_sales = [266.0, 145.9, 183.1, 119.3, 180.3, 168.5, 231.8, 224.5, 192.8, 122.9, 336.5, 185.9, 194.3, 149.5, 210.1, 273.3, 191.4, 287.0, 226.0, 303.6, 289.9, 421.6, 264.5, 342.3, 339.7, 440.4, 315.9, 439.3, 401.3, 437.4, 575.5, 407.6, 682.0, 475.3, 581.3, 646.9]


# Questa  e' la classe base per i nostri modelli. L'avevamo vista via per il corso.
# Ho aggiunto il metodo "__repr__" che se ricordate e' la rappresentazione in stringa di
# un oggetto, e ho fatto in modo che ritorni il nome della classe. Questo  ci tornera' utile
# dopo, quando confronteremo i modelli

class Model(object):

    def fit(self, data):
        pass
    
    def predict(self):
        pass
    
    def __repr__(self):
        # Questa e' una cosa che si usa ma un po' avanzata - vuol dire il nome della classe
        return self.__class__.__name__


# Questo e' il modello di lezione 8 - ovvero quello senza il fit. Ci sono un po' di "print" sparsi qua e la' ed
# ora commentati, che ho usato io stesso per correggere alcuni bug e capire meglio come stafa funzionando il tutto.

class IncrementModel(Model):

    def fit(self, data):
        raise NotImplementedError('Questo modello non prevede un fit')
    
    def predict(self, prev_months):
        
        # Faccio alcuni controlli di sanificazione - NON ESAUSTIVI.
        if not isinstance(prev_months, list):
            raise Exception('Errore: prev_months non di tipo lista')
        if len(prev_months) <= 2:
            raise Exception('Errore: lunghezza di prev_months non sufficiente, servono almeno due elementi per calcolare un incremento')
        
        # Setto il numero di mesi
        n_months = len(prev_months)
        
        #print('Il modello sta venendo eseguito su "{}" mesi'.format(n_months))

        # Preparo una variabile di supporto per calcolare l'incremento medio
        increments = 0
        
        # Processo i mesi in input su cui fare la predizione
        for i in range(n_months):

            # Salto il primo mese in quanto non posso avere definito
            # un incremento se non ho almento due mesi
            if i == 0:
                continue
            else:
                # Calcolo l'incremento tra questo mese ed il precedente
                increments += prev_months[i] - prev_months[i-1]
                #print('Increment: {}'.format(prev_months[i] - prev_months[i-1]))
        
        # Calcolo l'incremento medio divivendo la somam degli incrmenti sul totale dei mesi
        # ma meno uno: sopra ho scartato il primo mese in effetti!
        avg_increment = increments / (n_months-1)
        
        #print('Il modello sta venendo eseguito su "{}" mesi'.format(n_months))
     
        # Torno la predizione
        return prev_months[-1] + avg_increment



# Questo e' il modello di lezione 9 - ovvero quello con il fit. Anche qui ci sono un po' di "print" sparsi qua e la' ed
# ora commentati, che ho usato io stesso per correggere alcuni bug e capire meglio come stafa funzionando il tutto.

class FittableIncrementModel(Model):

    def fit(self, data):

        # Faccio alcuni controlli di sanificazione - NON ESAUSTIVI.
        if not isinstance(data, list):
            raise Exception('Errore: data non di tipo lista')
        if len(data) <= 2:
            raise Exception('Errore: lunghezza di data non sufficiente, servono almeno due elementi per calcolare un incremento')
        
        # Setto il numero di mesi
        n_months = len(data)

        # Preparo una variabile di supporto per calcolare l'incremento medio
        fluctuations = 0
        
        # Processo i mesi in input su cui fare il fit
        for i in range(n_months):

            # Salto il primo mese in quanto non posso avere definito
            # un incremento se non ho almento due mesi
            if i == 0:
                continue
            else:
                # Calcolo l'incremento tra questo mese ed il precedente
                fluctuations += (data[i] - data[i-1])
                #print('Fluctuation: {}'.format(abs(data[i] - data[i-1])))
        
        #print('avg fluctuation: "{}"'.format(fluctuations/len(data)))
        self.avg_fluctuation = fluctuations/len(data)
    
    def predict(self, prev_months):

        # Faccio alcuni controlli di sanificazione - NON ESAUSTIVI.
        if not isinstance(prev_months, list):
            raise Exception('Errore: prev_months non di tipo lista')
        if len(prev_months) <= 2:
            raise Exception('Errore: lunghezza di prev_months non sufficiente, servono almeno due elementi per calcolare un incremento')
        
        # Setto il numero di mesi
        n_months = len(prev_months)
        
        #print('Il modello sta venendo eseguito su "{}" mesi'.format(n_months))

        # Preparo una variabile di supporto per calcolare l'incremento medio
        increments = 0
        
        # Processo i mesi in input su cui fare la predizione
        for i in range(n_months):

            # Salto il primo mese in quanto non posso avere definito
            # un incremento se non ho almento due mesi
            if i == 0:
                continue
            else:
                # Calcolo l'incremento tra questo mese ed il precedente
                increments += prev_months[i] - prev_months[i-1]
                #print('Increment: {}'.format(prev_months[i] - prev_months[i-1]))
        
        # Calcolo l'incremento medio divivendo la somam degli incrmenti sul totale dei mesi
        # ma meno uno: sopra ho scartato il primo mese in effetti!
        avg_increment = increments / (n_months-1)
        
        #print('Il modello sta venendo eseguito su "{}" mesi'.format(n_months))
        #print('avg_increment = "{}"'.format(avg_increment))
        # Torno la predizione
        return (prev_months[-1] + ( (avg_increment/2) + (self.avg_fluctuation/2)))


#=========================================#
#        Corpo del programma              #
#=========================================#

# Divido i dati in training e test set
shampoo_sales_train = shampoo_sales[0:-12]   # Primi 24 mesi
shampoo_salels_test =  shampoo_sales[-12:] # Ultimi 12 mesi

# Istanzio il modello senza fit
increment_model = IncrementModel()

# Istanzio il modello con fit e chiamata alla funzione fit
fitted_increment_model = FittableIncrementModel()
fitted_increment_model.fit(shampoo_sales[0:24])

# Metto entrambi i modelli in una lista
models = [increment_model, fitted_increment_model]

# Swicth per il plot
plot = False

for model in models:

    error = 0
    print('') # Lascio una riga bianca
    print('Sto valutando il modello "{}"'.format(model))

    # Predizioni 1 step su test set per modello senza fit
    predictions = []
    for i in range(12):
        prediction = model.predict(shampoo_sales[24+i-3-1:24+i-1])
        print('"{}" vs "{}"'.format(int(prediction), int(shampoo_sales[24+i])))
        predictions.append(prediction)

        error += abs(prediction - shampoo_sales[24+i])
    
    error = error / 12

    print('Errore medio: "{}"'.format(error))

    # Scommentate le righe qui sotto se volete vedere i plot. Siccome non tutti gli ambienti 
    # supportano il plot, ho preferito disabilitirle i plot commentandole "di default"
    from matplotlib import  pyplot
    pyplot.plot(shampoo_sales[0:24] + predictions, color='tab:red')
    pyplot.plot(shampoo_sales, color='tab:blue')
    pyplot.show()