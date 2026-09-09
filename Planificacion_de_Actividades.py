# Planificador de actividades - Version 2.0

PREPARACION = 5
continuar = 'si'

while continuar == 'si':
    actividad = input('Nombre de la actividad: ')
    minutos = int(input('Minutos por actividad: '))
    veces = int(input('Veces que la haras al dia: '))

    subtotal = minutos * veces
    total = subtotal + PREPARACION

    print('--- Resumen ---')
    print('Tarea:', actividad)
    print('Total de minutos con preparacion:', total)

    if total > 60:
        print('Aviso: Requiere mas de 1 hora de tu dia.')
    else:
        print('Aviso: Actividad corta, facil de planificar.')

    print('----------------')
    continuar = input('Quieres planificar otra actividad? (si/no): ')

print('Gracias por usar el planificador.')