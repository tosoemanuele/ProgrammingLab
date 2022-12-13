class Model():
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')
        
    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')

    def controllo_start_end(self, data, start, end):
        try:
            start = int(start)
        except: 
            if start == None:
                start = 0
        try:
            end = int(end)
        except:
            pass
        controllo_len = 0
        for item in data:
            controllo_len+=1
        if start > controllo_len:
            raise Exception('Start maggiore del numero di righe') 
        if end == None:
            end = controllo_len
        if end > controllo_len:
            raise Exception('End maggiore del numero di righe')
        

    def avg_increment(self, data, start, end):

        self.controllo_start_end(data, start, end)
        
        prev_value = None
        avg_increment = 0
        if type(data) is not list:
            raise TypeError('Errore')
        if len(data) < 2:
            raise Exception('Errore, lista troppo corta')
        for item in data[start:end]:
            if type(item) is not int and type(item) is not float:
                raise TypeError('non è un numero')
            if prev_value == None:
                prev_value = item
            else:
                avg_increment = avg_increment + (item-prev_value)
                prev_value = item
        return avg_increment


class IncrementModel(Model):
    def predict(self, data):
        
        diff = super().avg_increment(data, -3, None)
        prev_value= data[-1]
        try:
            diff = (diff) / (len(data[-3:])-1)
            prediction = prev_value + diff
            return prediction
        except:
            print('Non ho valutato alcuna differenza, non posso prevedere nulla!')


class FitIncrementModel(IncrementModel):
    def predict(self, data):
        #for i in range(3):
        recent_avg = super().super().avg_increment(data, -3, None)
        past_avg = super().super().avg_increment(data, 0, -3)
        prediction = data[-1] + ((recent_avg+past_avg)/2)
        #calcolami il valore successivo
        #.append del valore alla fine della lista
        data.append(prediction)
           # i += 1
    


data = FitIncrementModel()
a = data.predict([8, 19, 31, 41, 50, 52, 60])
print('{}'.format(a))
    