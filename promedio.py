
#!/usr/bin/env python3

# Codigo para que el navegador entienda que es un texto

print("Content-type: text/plain\n")

# Creaciòn de lista de alumnos con sus notas 
alumnos = [{"nombre": "juan", "notas": [7,8,9]},
           {"nombre": "Ana", "notas": [10,9,10]},
           {"nombre": "Luis", "notas": [5,6,4]}
           ]

# Mostramos los promedios

print("Promedio de las notas\n")

for alumno in alumnos:
    promedio = sum(alumno["notas"]) / len(alumno["notas"])
    print(f"{alumno['nombre']}: promedio = {promedio:.2f}")