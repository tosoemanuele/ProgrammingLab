class ExamException(Exception):
    pass

class MovingAverage():
    def __init__(self, length):
        length1 = self.controllo_length(length)
        self.length = length1
        

    def controllo_length(self, length):
        #controllo se è una stringa e, se possibile, trasformo in float
        if type(length) is str:
            try:
                length = float(length)
            except:
                raise ExamException('il valore di finestra mobile che mi hai dato è un str non convertibile a intero')
        #controllo tutti i valori x.0 e li trasformo in interi
        if type(length) is float:
            if (length - int(length) == 0.0):
                length = int(length)
        #ultima verifica se il numero è intero
        if type(length) is not int:
            raise ExamException('il valore di finestra mobile che mi hai dato non è un numero intero')
        if length < 1:
            raise ExamException('La lunghezza della finestra mobile è minore di 1')
        return length

    def controllo_data(self, data):
        #controllo che sia una lista
        if not isinstance(data,list):
            raise ExamException('Non è una lista')
        #controllo che la lista non sia vuota
        if len(data)==0:
            raise ExamException('La lista è vuota')
        #controllo che la lista sia più lunga della finestra
        if self.length > len(data):
            raise ExamException('la finestra è maggiore della lunghezza della lista')
        #controllo che i valori della lista siano numeri
        for i in range(len(data)):
            if not isinstance(data[i],float) and not isinstance(data[i],int):
                raise ExamException('Il valore nella lista non è un numero')

    def media(self, i, data):
        average = 0
        for j in range(self.length):
            average += data[i+j]
            #fai la media fra data[i+j] per j che varia secondo la finestra mobile
        average = average/self.length
        return average
            
    def compute(self, data):
        self.controllo_data(data)
        result = []
        #la i del for indica l'indice del primo elemento tra quelli da calcolare
        for i in range((len(data) - self.length)+1):
            average = self.media(i, data)
            result.append(average)
            print(i)
        return result

moving_average = MovingAverage(4.0)
result = moving_average.compute([2,4,8,16])
print(result)