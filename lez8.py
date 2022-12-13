class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
        
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')




class IncrementModel(Model):
    def predict(self, data):
        
        prev_value = None
        diff = 0
        if type(data) is not list:
            raise TypeError('Errore')
        if len(data) < 2:
            raise Exception('Errore, lista troppo corta')
        for item in data[-3:]:
            if type(item) is not int and type(item) is not float:
                raise TypeError('non è un numero')
            if prev_value == None:
                prev_value = item
            else:
                diff = diff + (item-prev_value)
                prev_value = item
        try:
            diff = (diff) / (len(data[-3:])-1)
            prediction = prev_value + diff
            return prediction
        except:
            print('Non ho valutato alcuna differenza, non posso prevedere nulla!')



data = IncrementModel()
a = data.predict([50, 52, 60])
print('{}'.format(a))
    