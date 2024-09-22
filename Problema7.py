'''Realiza un programa que lea dos números por teclado y permite elegir entre 3 opciones en un menú:
- Mostrar una suma de los dos números
- Mostrar una resta de los dos números (el primero menos el segundo)
- Mostrar una multiplicación de los dos números
- En caso de introducir una opción inválida, el programa informará de que no es correcta.
'''
num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

menu="""
    1.Suma de los dos números
    2.Resta de los dos números
    3.Multiplicación de los dos números
    """
print(menu)
op=int(input("Escoga una opcion: "))
match op:
    case 1:
        suma= num1+num2
        print(f"La suma es {suma}")
    case 2:
        resta= num1-num2
        print(f"La resta es {resta}")
    case 3:
        multi= num1*num2
        print(f"La resta es {multi}")
    case _:
        print("La opcion no es correcta")