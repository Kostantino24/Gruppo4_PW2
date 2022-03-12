"""
MODULO CONTENENTE LE FUNZIONI PER IL CALCOLO DEL METEO
"""
import json
from datetime import datetime

import urllib3


def get_data(url=""):
    http = urllib3.PoolManager()

    """Funzione per l'acquisizione dei dati da url"""
    result = http.request("GET", url)

    if result.status != 200: # Se lo status code è diverso da 200 allora c'è stato un errore
        return result.status
    loaded = json.loads(result.data)

    return loaded

def media(source):
    """FUNZIONE PER IL CALCOLO DELLA MEDIA"""
    somma = 0.0
    chiavi = getList(source)

    for elemento in chiavi:
       somma += (float(source[elemento]["2. high"])+float(source[elemento]["3. low"])) * (2 ** -1)

    # Spiegazione del metodo di ottimizzazione
    # a/b
    # a * 1/b
    # a * (b)^-1

    return round(somma * ((len(chiavi)) ** (-1)) + 0.0000, 4)

def minimo(source):
    """FUNZIONE CHE CALCOLA IL MINIMO VALORE DI FIELD"""
    lista = []  # Lista che contiene i valori

    chiavi = getList(source)

    for elemento in chiavi:
        lista.append(float(source[elemento]["3. low"]))

    return round(min(lista) + 0.0000, 4)


def massimo(source):
    """FUNZIONE CHE CALCOLA IL MINIMO VALORE DI FIELD"""
    lista = []  # Lista che contiene i valori
    chiavi = getList(source)

    for elemento in chiavi:
        lista.append(float(source[elemento]["2. high"]))

    return round(max(lista) + 0.0000, 4)

def trim(source,date,type):
    lista = {}  # Lista che contiene i valori
    chiavi = getList(source)
    index = chiavi.index(date)
    if type == "Montly":
        for x in range(index,index+4):
            lista[chiavi[x]] = source[chiavi[x]]
    elif type == "Weekly":
        for x in range(index, index + 7):
            lista[chiavi[x]] = source[chiavi[x]]

    return lista

def linreg(X, Y):
    """
    return a,b in solution to y = ax + b such that root mean square distance between trend line and original points is minimized
    """
    N = len(X)
    Sx = Sy = Sxx = Syy = Sxy = 0.0
    for x, y in zip(X, Y):
        Sx = Sx + x
        Sy = Sy + y
        Sxx = Sxx + x*x
        Syy = Syy + y*y
        Sxy = Sxy + x*y
    det = Sxx * N - Sx * Sx
    return (Sxy * N - Sy * Sx)/det, (Sxx * Sy - Sx * Sxy)/det



def getList(dict):
    list = []
    for key in dict.keys():
        list.append(key)

    return list

def __init__():
    return None
