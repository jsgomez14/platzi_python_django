# num_1 = int(input('Escoge un entero: '))
# num_2 = int(input('Escoge otro entero: '))

# if num_1 > num_2:
#     print("El primer numero es mayor al segundo")
# elif num_1 < num_2:
#     print("El segundo numero es mayor al primero")
# else:
#     print("Los dos numeros son iguales")

print("Ejercicio")

nombre_1 = input('Ingresa nombre del usuario: ')
num_1 = int(input('Ingresa edad del usuario: '))

nombre_2 = input('Ingresa el nombre del otro usuario: ')
num_2 = int(input('Ingresa la edad del otro usuario: '))

if num_1 > num_2:
    print(f"{nombre_1} es mayor que {nombre_2}")
elif num_1 < num_2:
    print(f"{nombre_2} es mayor que {nombre_1}")
else:
    print(f"{nombre_1} y {nombre_2} cuentan con la misma edad")