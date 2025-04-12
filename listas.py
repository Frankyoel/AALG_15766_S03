#Meodos para agregar
W = ["10"]
print(W)
W.append(8)
print(W)

W.insert(2, 15)
print(W)

#Metodos para eliminar

del W[1]
print(W)

W.remove("10")
print(W)


#Metodo con letras

w = []

print(w)

w.append("d")

w.insert(0, "b")

w.append("f")


print(w)

print(w.index("d"))

del w[1]

print(w)

w.remove("b")

print(w)


#Listas y tuplas

t = ("j","k","p")
print(t)

v =list("welcome")

print(v)

k = tuple(v)
print(k)

print([0 if k % 3 == 0 else k for k in range(1, 10, 2)])
print(k)
