for num in range(0, 151):
    print(num)

for num in range(5, 1000, 5):
    print(num)

for num in range (1, 101):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

# Inicializa una variable para almacenar la suma
suma_impares = 0

# Itera a través de los enteros del 0 al 500,000
for num in range(0, 500001):
    # Verifica si el número es impar
    if not num % 2 == 0:
        # Si es impar, agrégalo a la suma
        suma_impares += num

# Imprime la suma final de los enteros impares
print(suma_impares)

for num in range(2018, 0, -4):
    print(num)

lowNum= 3
highNum= 9
mult= 3

for num in range(lowNum, highNum + 1):
    if num % mult == 0:
        print(num)


