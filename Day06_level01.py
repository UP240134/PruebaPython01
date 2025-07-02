#Dia 6 de Python
## Un "Tuple" son un conjunto de datos que son inmutables (o no cambiantes), se parece a una lista, con la diferencia que no se pueden modificar
#-------Primer ejercicio-------------
print("Vamos hacer los famosos Tuples de mi family")
hermanos = ("Jorgito","Alejandro")
hermanas= ("Alexa","Pepino")
print ("Mis hermanos son:" , hermanos)
print ("Mis hermanas son:" , hermanas)
Thermanos = hermanos + hermanas
print ("Todos mis hermanos son:" , Thermanos)
print("En total son:", len(Thermanos))
Thermanos = Thermanos[:2]
padres = ("Jorge","Alondra")
family = Thermanos + padres
print("Toda mi familia son:", family)

#-------ejercicio 2...
# primera parte
hermana_menor="Alexa"
hermano_medio ="Alejandro"
hermano_mayor ="Jorgito"
Padre ="Jorge"
Madre ="Alondra"
print ("Mi hermana menor es:",hermana_menor)
print("Mi hermano del medio es:",hermano_medio)
print("Mi hermano mayor es:",hermano_mayor)
print("Mi padre es:",Padre)
print("Mi madre es:",Madre)

#Segunda parte
frutas=("manzana","plátano","naranja", "fresa" , "uva")
verduras= ("lechuga","tomate","zanahoria","brocoli","espinacas")
animal =('pollo', 'carne', 'pescado', 'huevo', 'queso')
print("Las frutas son:",frutas)
print("Las verduras son:",verduras)
print("Los productos animales son:",animal)
Comida = frutas+verduras+animal
print("Comida es:",Comida)

#tercara parte
print("Se va a convertir en lista el tuple comida")
lista = list(Comida)
print("La lista:",lista)

#cuarta parte
def calculo(lista):
    longitud = len(lista)
    if longitud % 2 == 0:
        pr = lista[longitud // 2 - 1]
        pt = lista[longitud // 2]
        medio = [pr, pt]
    else:
        medio = [lista[longitud // 2]]
    return medio

medio = calculo(lista)
print("El valor medio de la lista es:", [m.capitalize() for m in medio])

#quinta parte
print("Ahora vamos a poner los primeros 3 elementos y los últimos 3 elementos de la lista comida en un nuevo tuple...")
primeros_ult = tuple(lista[:3] + lista[-3:])
print("Los primeros 3 y los últimos 3 elementos de la lista comida son: ", primeros_ult)

#Sexta parte
print("Vamos a borrar la lista")
del lista
print("Lista borrada")

#Septima parte
print("Vamos a comprobar si Estonia y/o Iceland están en el turple de países")
paises_nordicos = ("Denmark", "Finland","Iceland", "Norway", "Sweden")
print("Vamos a comprobar si esta Estonia en los paises nordicos:", "Estonia" in paises_nordicos)
print("Vamos a comprobar si esta Iceland en los paises nordicos:", "Iceland" in paises_nordicos)

