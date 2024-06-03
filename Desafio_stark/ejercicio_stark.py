from data_stark import *
from funciones_strak import *

while True:
    print("\nMENU:")
    print("1. Imprimir nombres de todos los superhéroes")
    print("2. Imprimir nombres y alturas de todos los superhéroes")
    print("3. Mostrar el superhéroe más alto")
    print("4. Mostrar el superhéroe más bajo")
    print("5. Mostrar la altura promedio de los superhéroes")
    print("6. Mostrar la identidad del superhéroe más alto")
    print("7. Mostrar la identidad del superhéroe más bajo")
    print("8. Mostrar el superhéroe más pesado")
    print("9. Mostrar el superhéroe menos pesado")
    print("10. Salir")

    opcion = input("Seleccione una opcion: ")

    if opcion == "1":
        imprimir_nombres(lista_personajes)
    elif opcion == "2":
        imprimir_nombres_alturas(lista_personajes)
    elif opcion == "3":
        heroe = heroe_mas_alto(lista_personajes)
        print(f'El superhéroe más alto es {heroe["nombre"]} con una altura de {heroe["altura"]}')
    elif opcion == "4":
        heroe = heroe_mas_bajo(lista_personajes)
        print(f'El superhéroe más bajo es {heroe["nombre"]} con una altura de {heroe["altura"]}')
    elif opcion == "5":
        promedio = altura_promedio(lista_personajes)
        print(f'La altura promedio de los superhéroes es {promedio}')
    elif opcion == "6":
        identidad = identidad_heroe_mas_alto(lista_personajes)
        print(f'La identidad del superhéroe más alto es {identidad}')
    elif opcion == "7":
        identidad = identidad_heroe_mas_bajo(lista_personajes)
        print(f'La identidad del superhéroe más bajo es {identidad}')
    elif opcion == "8":
        heroe = heroe_mas_pesado(lista_personajes)
        print(f'El superhéroe más pesado es {heroe["nombre"]} con un peso de {heroe["peso"]}')
    elif opcion == "9":
        heroe = heroe_menos_pesado(lista_personajes)
        print(f'El superhéroe menos pesado es {heroe["nombre"]} con un peso de {heroe["peso"]}')
    elif opcion == "10":
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Por favor, intenta de nuevo.")





