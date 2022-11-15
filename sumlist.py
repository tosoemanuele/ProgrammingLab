def sum_list(lista):
    if len(lista) == 0:
        return None
    else:
        sum = 0
    
        for item in lista:
            sum = sum + item
        return sum

lista = [1, 2, 3]
print('il valore della somma è {}'.format(sum_list(lista)))