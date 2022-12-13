class CSVFile():

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Nome del file "{}"'.format(self.name)

    def get_data(self):
        valori = []
        try:
            file = open(self.name, 'r')
        except:
            print('Errore')
        for line in file:
            tmp = []
            elementi = line.split(',')
            for item in elementi:
                try:
                    item = float(item)
                    if elementi[0] != 'Date':
                        data = elementi[0]
                        numero = (elementi[1])
                        numero = numero.strip()
                        tmp.append(data)
                        tmp.append(numero)
                        valori.append(tmp)
                except:
                    print('Errore')

        return valori


class NumericalCSVFile(CSVFile):

    def get_data(self):
        string_data = super().get_data()
        numerical_data = []
        for string_row in string_data:
            numerical_row = []
            for i, element in enumerate(string_row):
                if i == 0:
                    numerical_row.append(element)
                else:
                    try:
                        numerical_row.append(float(element))
                    except Exception as e:
                        print('Errore')
                        break
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        return numerical_data


a = NumericalCSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(a.name))
print('Dati contenuti nel file: "{}"'.format(a.get_data()))
