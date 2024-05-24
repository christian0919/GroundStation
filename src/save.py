import sys
import csv
from datetime import datetime
import os

class save:
    def __init__(self):
        self.data = []
        self.data2 = []
        self.__path = ""
        self.__path2 = ""
        self.lastDate = ""
        self.beginDate = ""
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
        with open(self.__path2 , "a", newline="") as archivo_csv:
            writer = csv.writer(archivo_csv)
            # Si el archivo está vacío, escribir la cabecera
            if archivo_csv.tell() == 0:
                writer.writerow((["latitud","longitud"]))
            # Escribir los datos en el archivo CSV
            writer.writerows(self.data2)

        with open(self.__path3, 'w') as archivo:
            archivo.write("Inicio: "+ self.beginDate + "\n")
            archivo.write("Fin: "   + self.lastDate)
            
    def setPath(self):
        path = datetime.now()
        path = path.strftime("%Y-%m-%d_%H-%M-%S")
        self.lastDate = path
        self.__path = "Missions/Carga1" + path + ".csv"  
        self.__path2 = "Missions/Carga2" + path + ".csv"
        self.__path3 = "Missions/mision" + path + ".txt"
        
        

    def add_Data(self,add,add2):
        self.data.append(add)
        self.data2.append(add2)

    def getPath(self):
        return self.__path
    
    def __createDirectory(self):
        dir = "Missions/"
        if not os.path.exists(dir):
            os.makedirs(dir)

    def SetBeginDate(self, date):
         self.beginDate = date
 