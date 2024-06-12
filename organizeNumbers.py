numeros = [5, 7, 4, 12, 3, 75]
final = []
newNumeros = numeros.copy()

while newNumeros:
    minimo = min(newNumeros)
    final.append(minimo)
    newNumeros.remove(minimo)
    
print(final)
