milista=["Maria", "Pepe", "Martha", "Antonio"]  ## pueden ir numeros, booleans etc

milista.append("Sandra") #agrega al final
milista.insert(2, "Johana") #agrega en la posicion 2
milista.extend(["Ana", "Erika"]) #agrega o extiende la lista

milista.remove("Ana")  #suprime Ana del resultado

milista.pop()  #Elimina el ultimo elemento de la lista

milista=["Maria", "Pepe", "Martha", "Antonio"] * 3 # Podemos imprimir tres veces la lista

print(milista[:])

print(milista.index("Ana")) #devuelve los indices

print("Pepe" in milista)

