'''En los Estados Unidos, se acostumbra dejar una propina a su mesero después de cenar en un
restaurante, generalmente una cantidad igual al 15% o más del costo de su comida.
Escriba un programa que pregunte al usuario cuánto fue su consumo en el restaurante y que
porcentaje de propina desea dejar al mesero. Su programa debe devolver la cantidad de dinero a
dejar como propina.'''

consumo = float(input(("¿Cuánto fue el consumo en el restaurante?: ")))
propina = float(input(("¿Que porcentaje de propina desea dejar al mesero?: ")))
resultado = consumo*propina/100
print(f"{resultado} soles")

