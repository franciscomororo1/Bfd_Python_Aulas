from functools import reduce

numeros = [2, 3, 4, 5]

print (reduce(lambda x, y: x * y, numeros))