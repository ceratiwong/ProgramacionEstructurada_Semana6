edades = [10, 15, 20, 30, 50]
print(edades)

clon = edades 
print(clon)

edades.append(25)
print(edades)

print(clon)

clon.append(35)
print(edades)

perro = clon
print(perro)

perro.append(45)
print(edades)

perro.remove(45)
print(clon)

