import sys
import csv
from datetime import datetime
import os

class save:
    def __init__(self):
        self.data = []
        self.__path = ""
        self.__createDirectory()

    def save_Mission_Data(self):
        with open(self.__path , "a", newline="") as archivo_csv:
            writer = csv.writer(archivo_csv)
            # Si el archivo está vacío, escribir la cabecera
            if archivo_csv.tell() == 0:
                writer.writerow((["Altitud", 
                                 "Presion_Interna", "Presion_Externa",
                                 "Temperatura_Interna", "Temperatura_Externa",
                                 "Latitud","Longitud",
                                 "Giro_X","Giro_Y","Giro_Z",
                                 "Aceleracion_X","Aceleracion_Y","Aceleracion_z"]))

            # Escribir los datos en el archivo CSV
            writer.writerows(self.data)

    def setPath(self):
        path = datetime.now()
        path = path.strftime("%Y-%m-%d_%H-%M-%S")
        self.__path = "Missions/" + path + ".csv"  

    def add_Data(self,add):
        self.data.append(add)

    def getPath(self):
        return self.__path
    
    def __createDirectory(self):
        dir = "Missions/"
        if not os.path.exists(dir):
            os.makedirs(dir)
 