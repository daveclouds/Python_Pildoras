midiccionario={"Alemania":"Berlin", "Francia":"Paris", "Reino Unido":"Londres", "Espana":"Madrid"}

print(midiccionario["Francia"])

midiccionario["Italia"] = "Lisboa"
print(midiccionario)

del midiccionario["Reino Unido"]
print(midiccionario)