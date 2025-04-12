print("Necesito ayuda")

#Retorna una resta
def restar(a,b):
    return a - b

#Retorna una multiplicacion
def multi (a:int,b:int):
    return a * b

#Retorna un string
def saludo(d:str)-> str:
    x = "Hola " + d 
    return x

#retorna vacio 
def despedida (a:str)-> None:
    x = "adios socio" + a
    print(x)

###Para que puedan mostarse los resultados
print(restar(10, 2))
print(multi(5,6))

print(saludo("steve"))

d = 9
f = 8

d, f = f, d
print(d, f)

h = [61, 51,5]

busca = 6

if busca in h:
    print("Encontrado")


