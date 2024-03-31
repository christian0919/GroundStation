import sys
from PySide6.QtWidgets import QApplication
from communication import communication
import pyqtgraph as pg
import numpy as np
import time
import serial.tools.list_ports
from configView import configView



uiclass, baseclass = pg.Qt.loadUiType("Main_View.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.missionStatus = False
        self.com = communication()
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

        self.Record_button.setText("Start ")


        self.Record_button.clicked.connect(self.StartMission)
        self.buttonPorts.clicked.connect(self.UpdatePortsList)
        self.button_Config.clicked.connect(self.Show_Config)

        
        self.timer = pg.QtCore.QTimer()


    def StartMission(self):
        if not self.missionStatus:
           if self.comboPorts.count() == 0:        
               self.timer.timeout.connect(self.DummyMode)
               self.timer.start(100)
               self.missionStatus = not self.missionStatus
               self.Record_button.setText("Stop ")
               print("Demo")
           else:
                self.Record_button.setText("Stop ")
                ### prepare module
                self.com = communication()
                self.com.Set_Serial_Port(self.comboPorts.currentText())
                self.com.InitializeLora()
                ### start real mode
                self.timer.timeout.connect(self.RealMode)
                self.timer.start(100)
                self.missionStatus = not self.missionStatus

        else :
            self.Record_button.setText("Start ")
            self.missionStatus = not self.missionStatus
            self.timer.stop()  
            print("stop")

    def RealMode(self):
        data = self.com.Get_Cansat_Data()
        if data != "" :
            splited = data.split(":")
            rnAltitud = int(splited[0])
            rnTemperatureI = int(splited[1])
            rnTemperatureE = int(splited[2])
            rnHum = int(splited[3])
            rnVelocidad = int(splited[4])
            self.UpdateGraphics(rnAltitud,rnTemperatureI ,rnTemperatureE ,rnHum , rnVelocidad)


    def DummyMode(self):
        rnAltitud = np.random.uniform(0, 500)
        rnTemperatureI = np.random.uniform(15, 30)
        rnTemperatureE = np.random.uniform(15, 30)
        rnHum = np.random.uniform(15, 30)
        rnVelocidad = np.random.uniform(0, 100)
        self.UpdateGraphics(rnAltitud,rnTemperatureI ,rnTemperatureE ,rnHum , rnVelocidad)

    def UpdateGraphics(self, rnAltitud,rnTemperatureI ,rnTemperatureE ,rnHum , rnVelocidad):


        self.x.append(len(self.x))
        
        self.y_Altitud.append(rnAltitud)
        self.Graph_Altitud.setData(self.x, self.y_Altitud)

        self.y_InternTemp.append(rnTemperatureI)
        self.Graph_TemperaturaInterna.setData(self.x , self.y_InternTemp)

        self.y_ExTemp.append(rnTemperatureE)
        self.Graph_Temperatura_Externa.setData(self.x , self.y_ExTemp)
        
        self.y_hum.append(rnHum)
        self.Graph_Humedad.setData(self.x , self.y_hum)

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

    def Show_Config(self):
        configutarionView = configView()
        configutarionView.ui.show()  
        configutarionView.exec()
        
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
