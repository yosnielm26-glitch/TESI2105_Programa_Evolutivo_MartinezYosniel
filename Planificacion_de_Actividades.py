# Planificador de actividades - Version 3.0
# TESI 2105 | Laboratorio 3

PREPARACION = 5


# 1. Función con parámetros y valor de retorno
def calcular_tiempo_total(minutos, veces):
    subtotal = minutos * veces
    total = subtotal + PREPARACION
    return total


# 2. Función con parámetros y acción sin retorno explícito
def mostrar_resumen(actividad, total):
    print('--- Resumen ---')
    # Uso de la función incorporada len() para contar caracteres del nombre
    print('Tarea:', actividad, f'(Letras en el nombre: {len(actividad)})')
    print('Total de minutos con preparacion:', total)

    # Estructura selectiva conservada de v2.0
    if total > 60:
        print('Aviso: Requiere mas de 1 hora de tu dia.')
    else:
        print('Aviso: Actividad corta, facil de planificar.')

    print('----------------')


# 3. Función de entrada de datos
def pedir_datos():
    actividad = input('Nombre de la actividad: ')
    minutos = int(input('Minutos por actividad: '))
    veces = int(input('Veces que la haras al dia: '))
    return actividad, minutos, veces


# Función principal
def main():
    continuar = 'si'

    # Estructura cíclica conservada de v2.0
    while continuar.lower() == 'si':
        actividad, minutos, veces = pedir_datos()

        # Llamada a la función de cálculo
        total = calcular_tiempo_total(minutos, veces)

        # Llamada a la función de presentación
        mostrar_resumen(actividad, total)

        continuar = input('Quieres planificar otra actividad? (si/no): ')

    print('Gracias por usar el planificador.')


# Ejecución del programa
main()