lista =[]
print(type(lista))
lista = [1,True,"Lola"]
print(lista)

lista_nombres=["Lola","Pedro","Juan","Mara"]
print(lista_nombres)

print(lista_nombres[3])
lista_nombres.append("Luisa")
print(lista_nombres)
lista_nombres[2]="Franco"
print(lista_nombres) 

print(lista_nombres[:3])

lista_nombres.insert(0,"Luis")
print(lista_nombres)
lista_nombres.pop()
print(lista_nombres)
print(lista_nombres.index("Luis"))
