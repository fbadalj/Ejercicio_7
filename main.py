nombres = []
while True:
    nombre= input("Nombre: ")
    if nombre == "fin":
        break
    telefono = input("Telefono: ")
    lista = {}
    lista["Nombre"] = nombre
    lista["Telefono"] = telefono
    nombres.append(lista)
print("lista nombre:\n", nombres)

