import math

'''
    Data una lista di numeri ritorna la media.
'''
def calculate_mean(lista):

    somma = 0
    for n in lista:
        somma = somma + n

    return float(somma) / len(lista)

'''
    Date due liste di numeri calcola l'indice di correlazione di Pearson.
'''

def calculate_pearson(x, y):

    mean_x = calculate_mean(x)
    mean_y = calculate_mean(y)

    xy = 0
    x2 = 0
    y2 = 0

    for i in range(len(x)):
        x[i] = x[i] - mean_x
        y[i] = y[i] - mean_y

        xy = xy + x[i]*y[i]
        x2 = x2 + x[i]*x[i]
        y2 = y2 + y[i]*y[i]

    return xy / math.sqrt(x2*y2)

