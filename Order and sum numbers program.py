#Obtenemos datos, eliminamos espacios con .split
num = input("Escribe los números que ordenar ").split(" ")

#A lista y ordenamos
print("Números ordenados, menor a mayor")
num=list(num)
num.sort()
print(num)

#Ordenamos mayor a menor
print("")
print("Mayor a menor")
num.sort(reverse=True)
print(num)

#Datos en la lista
print("")
print("Número de dígitos")
print(len(num))

#Creamos generador, str a int para operar con él
#R.I.P RAM
num = (int(x) for x in num)
#Operador
print("")
print("Suma de los números")
print(sum(num))
