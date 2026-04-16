# tu datos 

edades = [14,15,17,13]
musica = ["salsa","rock","vallenato","pop","trap"]

# RETO 1    
promedio = sum(edades) / len(edades)
print("promedio de edades:",promedio)

# RETO 2
mayores = [edad for edad in edades if edad > 15]
print("edades >:", mayores )

# RETO 3
fans_rock = [gen for gen in musica if gen == "rock"]
print("total de fans rock: ", len(fans_rock))