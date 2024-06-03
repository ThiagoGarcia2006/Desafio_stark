from data_stark import *


def imprimir_nombres(lista: list) -> None:
    for heroe in lista:
        print(heroe["nombre"])

def imprimir_nombres_alturas(lista: list) -> None:
    for heroe in lista:
        print(f'{heroe["nombre"]} - {heroe["altura"]}')

def heroe_mas_alto(lista: list) -> float:
    max_altura = float(lista[0]["altura"])
    heroe_mas_alto = lista[0]
    for heroe in lista:
        if float(heroe["altura"]) > max_altura:
            max_altura = float(heroe["altura"])
            heroe_mas_alto = heroe
    return heroe_mas_alto

def heroe_mas_bajo(lista: list) -> float:
    min_altura = float(lista[0]["altura"])
    heroe_mas_bajo = lista[0]
    for heroe in lista:
        if float(heroe["altura"]) < min_altura:
            min_altura = float(heroe["altura"])
            heroe_mas_bajo = heroe
    return heroe_mas_bajo

def altura_promedio(lista: list) -> float:
    suma_alturas = 0
    for heroe in lista:
        suma_alturas += float(heroe["altura"])
    return suma_alturas / len(lista)

def identidad_heroe_mas_alto(lista: list) -> str:
    return heroe_mas_alto(lista)["identidad"]

def identidad_heroe_mas_bajo(lista: list) -> str:
    return heroe_mas_bajo(lista)["identidad"]

def heroe_mas_pesado(lista: list) -> float:
    max_peso = float(lista[0]["peso"])
    heroe_mas_pesado = lista[0]
    for heroe in lista:
        if float(heroe["peso"]) > max_peso:
            max_peso = float(heroe["peso"])
            heroe_mas_pesado = heroe
    return heroe_mas_pesado

def heroe_menos_pesado(lista: list) -> float:
    min_peso = float(lista[0]["peso"])
    heroe_menos_pesado = lista[0]
    for heroe in lista:
        if float(heroe["peso"]) < min_peso:
            min_peso = float(heroe["peso"])
            heroe_menos_pesado = heroe
    return heroe_menos_pesado
