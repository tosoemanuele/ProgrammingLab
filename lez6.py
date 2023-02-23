class CSVFile():
    def __init__(self, name):
        self.name = name
        if type(name) != str:
            raise Exception('Errore 1')
    def __str__(self):
        return 'Nome del file "{}"'.format(self.name)
        
    def get_data(self, start = None, end = None):
        valori = []
        try:
            file = open(self.name,'r')
        except:
            print('Errore 2')
        try:
            start = int(start)
        except: 
            if start == None:
                start = 1
        try:
            end = int(end)
        except:
            pass
        if start <= 0:
            raise Exception('Errore start 0')
        controllo_len = 0
        for line in file:
            controllo_len+=1
        if start > controllo_len:
            raise Exception('Start maggiore del numero di righe') 
        file = open(self.name,'r')
        if end == None:
            end = controllo_len
        if end > controllo_len:
            raise Exception('End maggiore del numero di righe')
        if start > end:
            print('dio poi')
            raise Exception('start > end')

        start-=1    
        for i,line in enumerate(file):
            if i in range(start, end):
                print(line)
                tmp = []
                elementi = line.split(',')
                for item in elementi:
                    try:
                        item = float(item)
                        if elementi[0]!='Date':
                            data = elementi[0]
                            numero = (elementi[1])
                            numero = numero.strip()
                            tmp.append(data)
                            tmp.append(numero)
                            valori.append(tmp)
                    except:
                        print('non è un numero, bensì {}'.format(item))
                
        return valori 

class NumericalCSVFile(CSVFile):
    def get_data(self, *args, **kwargs):
        string_data = super().get_data(*args, **kwargs)
        numerical_data = []
        for string_row in string_data:
            numerical_row = []
            for i,element in enumerate(string_row):
                if i == 0:
                    numerical_row.append(element)
                else:
                    try:
                        numerical_row.append(float(element))
                    except:
                        print('Errore')
                        break
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        return numerical_data

