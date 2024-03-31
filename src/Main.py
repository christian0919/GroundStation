import sys
from PySide6.QtWidgets import QApplication
import pyqtgraph as pg
import numpy as np
import time
import serial.tools.list_ports

uiclass, baseclass = pg.Qt.loadUiType("Main_View.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        #Graphics axes
        self.x = []
        self.y_hum = []
        self.y_Altitud = []
        self.y_InternTemp = []
        self.y_ExTemp = []
        self.y_vel = []
        #Colors
        lineGraphicsColor = (245, 106, 7)
        #Grapthics Background
        self.Graph_Altitud.setBackground(None)
        self.Graph_TemperaturaInterna.setBackground(None)
        self.Graph_Temperatura_Externa.setBackground(None)
        self.Graph_Velocidad.setBackground(None)
        self.Graph_Humedad.setBackground(None)
        #Asignacion de color a las Graficas
        self.Graph_Altitud = self.Graph_Altitud.plot(pen=lineGraphicsColor)
        self.Graph_TemperaturaInterna = self.Graph_TemperaturaInterna.plot(pen=lineGraphicsColor)
        self.Graph_Temperatura_Externa = self.Graph_Temperatura_Externa.plot(pen=lineGraphicsColor)
        self.Graph_Velocidad = self.Graph_Velocidad.plot(pen=lineGraphicsColor)
        self.Graph_Humedad = self.Graph_Humedad.plot(pen=lineGraphicsColor)

        self.Record_button.clicked.connect(self.StartMission)
        self.buttonPorts.clicked.connect(self.UpdatePortsList)
 

    def StartMission(self):

        if self.comboPorts.count() == 0:        
            self.timer = pg.QtCore.QTimer()
            self.timer.timeout.connect(self.DummyMode)
            self.timer.start(100)
        else:
            print("El ComboBox no está vacío.")


    def DummyMode(self):
        rnAltitud = np.random.uniform(0, 500)
        #print("rnAltitud:", rnAltitud)
        self.y_Altitud.append(rnAltitud)
        self.x.append(len(self.x))
        self.Graph_Altitud.setData(self.x, self.y_Altitud)

        rnTemperatureI = np.random.uniform(15, 30)
        #print("rnTemperatureI:", rnTemperatureI)
        self.y_InternTemp.append(rnTemperatureI)
        self.Graph_TemperaturaInterna.setData(self.x , self.y_InternTemp)

        rnTemperatureE = np.random.uniform(15, 30)
        #print("rnTemperatureE:", rnTemperatureE)
        self.y_ExTemp.append(rnTemperatureE)
        self.Graph_Temperatura_Externa.setData(self.x , self.y_ExTemp)
        
        rnHum = np.random.uniform(15, 30)
        self.y_hum.append(rnHum)
        self.Graph_Humedad.setData(self.x , self.y_hum)
        
        rnVelocidad = np.random.uniform(0, 100)
        #print("rnVelocidad:", rnVelocidad)
        self.y_vel.append(rnVelocidad)
        self.Graph_Velocidad.setData(self.x , self.y_vel)

    def UpdatePortsList(self):
        # Limpiar la lista de puertos antes de actualizarla
        self.comboPorts.clear()
        # Obtener la lista de puertos seriales
        puertos = serial.tools.list_ports.comports()
        print(puertos)

        # Agregar cada puerto a la lista
        for puerto in puertos:
            self.comboPorts.addItem(puerto.device)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
