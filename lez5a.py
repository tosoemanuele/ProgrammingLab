class CSVFile():
    def __init__(self, name):
        self.name = name
        try:
            open(self.name,'r')
        except:
            print('Errore')
    def __str__(self):
        return 'Nome del file "{}"'.format(self.name)
        
    def get_data(self):
        valori = []
        try:
            file = open(self.name,'r')
        except:
            print('Errore')
        for line in file:
            tmp = []
            elementi = line.split(',')
            if elementi[0]!='Date':
                data = elementi[0]
                numero = (elementi[1])
                numero = numero[0:-1]
                tmp.append(data)
                tmp.append(numero)
                valori.append(tmp)
        return valori 

csvfile = CSVFile('shampoo_sales.csv')
a = csvfile.get_data()
print('{}'.format(a))