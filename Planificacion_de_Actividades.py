# Planificador de actividades sencillo

actividad = input('Nombre de la actividad: ')
minutos = int(input('Minutos por actividad: '))
veces = int(input('Veces que la haras al dia: '))

PREPARACION = 5

subtotal = minutos * veces
total = subtotal + PREPARACION

print('Tarea:', actividad)
print('Minutos de trabajo:', subtotal)
print('Total de minutos con preparacion:', total)