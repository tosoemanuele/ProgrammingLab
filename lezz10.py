class Model():

    def __init__(self, lenght):
        self.lenght = lenght
        
    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def evaluate(self, data):
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
        print(data[start:end])
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
    
    def __init__(self, lenght):
        super().__init__(lenght)

    def evaluate(self, data):
        fut = []
        diff = 0
        for i in range(len(data)):
            if i < 3:
                fut.append(data[i])
            if i >= 3:
                self.predict(fut)
                print(fut)
                print(fut[i])
                print(data[i])
                diff+=data[i]-fut[i]
        return diff/(len(data)-4)
        
    def predict(self, data):
        diff = super().avg_increment(data, -3, None)
        prev_value = data[-1]
        try:
            diff = (diff) / (len(data[-3:])-1)
            prediction = prev_value + diff
            return prediction
        except:
            print('Non ho valutato alcuna differenza, non posso prevedere nulla!')


class FitIncrementModel(IncrementModel):

    def __init__(self, lenght):
        super().__init__(lenght)

    def evaluate(self, data):
        return super().evaluate(data)
        
    def fit(self, past_data):
        past_avg = super().avg_increment(past_data, None, None)
        past_avg = past_avg/(len(past_data)-1)
        self.past_avg = past_avg
        
        
    def predict(self, rec_data):
        ##for i in range(3):
        recent_avg =super().avg_increment(rec_data, -3, None)
        recent_avg = recent_avg/2
        prediction = rec_data[-1] + ((recent_avg+self.past_avg)/2)
        #calcolami il valore successivo
        #.append del valore alla fine della lista
        rec_data.append(prediction)
        return rec_data[-1]
    

data = FitIncrementModel(12)
data.fit([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24])
a = data.evaluate([25,26,27,28,29,30,31,32,33,34,35,36])
print('{}'.format(a))

#8, 19, 31, 41, 50, 52, 60