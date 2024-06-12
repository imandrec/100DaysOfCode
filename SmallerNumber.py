numeros = [5,7,4,12,3,75]
minimo = float('inf')
largo = len(numeros)

for i in range(largo):
    for j in range(i, largo):
        if numeros[j] < minimo:
            minimo = numeros[j]
print(minimo)
