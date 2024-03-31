import sys
import csv
from datetime import datetime
import os

class save:
    def __init__(self):
        self.data = []
        self.__path = ""
#        fecha_hora_formateada = fecha_hora_actual.strftime("%Y-%m-%d_%H-%M-%S")
        self.__createDirectory()

    def saveData(self):
        with open(self.__path , "a", newline="") as archivo_csv:
            writer = csv.writer(archivo_csv)

            # Si el archivo está vacío, escribir la cabecera
            if archivo_csv.tell() == 0:
                writer.writerow(["Presion", "Velocidad", "Altura"])

            # Escribir los datos en el archivo CSV
            writer.writerows(self.data)

    def setPath(self):
        path = datetime.now()
        path = path.strftime("%Y-%m-%d_%H-%M-%S")
        self.__path = "Missions/" + path + ".csv"  

    def getPath(self):
        return self.__path
    
    def __createDirectory(self):
        dir = "Missions/"
        if not os.path.exists(dir):
            os.makedirs(dir)
 