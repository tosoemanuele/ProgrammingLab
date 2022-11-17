def sum_csv(file_name):
    valori = []
    file = open(file_name,'r')
    for line in file:
        elementi = line.split(',')
        if elementi[0]!='Date':
            numero = float(elementi[1])
            valori.append(numero)
    return sum(valori)

