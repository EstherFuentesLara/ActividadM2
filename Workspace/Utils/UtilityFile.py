'''  Utilidades de fichero: 
        Tratamiento de ficheros de texto
        Tratamiento de ficheros arff
'''

import numpy as np
from scipy.io import arff
import pandas as pd

#  Abrir un fichero 
def openFile(fichero,modo):
    try:
        file = open(fichero,modo)
        return file
    except OSError as error:
        print("Error al abrir el fichero:" + fichero + " Error {0} ". format(error) )
        return

#  leer un fichero 
def readFile(fichero):
    try:
        return fichero.read()
         
    except OSError as error:
        print("Error al leer el fichero: " + fichero + " Error {0} ".format(error) )
        return
    
#  leer una linea 
def readFine(fichero):
    try:
        return fichero.readline()
         
    except OSError as error:
        print("Error al leer la linea del fichero: " + fichero + " Error {0} ".format(error) )
        return

#  leer una linea 
def readLines(fichero):
    try:
        return fichero.readlines()
         
    except OSError as error:
        print("Error al leer las lineas del fichero: " + fichero + " Error {0} ".format(error) )
        return

#  Escribir un fichero 
def writeFile(fichero,contenido):
    try:
        fichero.write(contenido)
        return 
    except OSError as error:
        print("Error al escribir el fichero: " + fichero + " Error {0} ".format(error) )
        return

#  Cerrar un fichero 
def closeFile(fichero):
    try:
        fichero.close()
        return 
    except OSError as error:
        print("Error al cerrar el fichero: " + fichero + " Error {0} ".format(error) )
        return

# Leer el archivo y devolver en datos la matriz de datos y 
# en metadatos la descripción de los atributos que lo componen tipo ARFF
def readFileArff(fichero):
    try:
        datos,metadatos = arff.loadarff(fichero)
        return datos,metadatos
    except OSError as error:
        print("Error al leer el fichero Arff: " + fichero + " Error {0} ".format(error) )
        return
    
# Leer el archivo y devolver en datos la matriz de datos y 
# en metadatos la descripción de los atributos que lo componen tipo CSV
def readFileCSV(fichero):
    try:
        ficheroCSV=pd.read_csv(fichero) 
        return ficheroCSV
    except OSError as error:
        print("Error al leer el fichero CSV: " + fichero + " Error {0} ".format(error) )
        return 