import sys
from PySide6.QtWidgets import QApplication, QVBoxLayout, QFrame , QSizePolicy

from communication import communication
import pyqtgraph as pg
import numpy as np
import time
import serial.tools.list_ports
from configView import configView
from save import save
from cylinder import CylinderWidget
from timer import TimeManager
uiclass, baseclass = pg.Qt.loadUiType("Views/Main_View.ui")

class MainWindow(uiclass, baseclass):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.missionStatus = False
        #Times
        self.timeUpdater = TimeManager()
        self.timer = pg.QtCore.QTimer()
        self.clock = pg.QtCore.QTimer()


        #Communication object
        self.com = communication()
        #Graphics axes
        self.Graphics_Axes()
        #Asignacion de color a las Graficas
        self.Graphics_Colors()
        #Metodos de los botones
        self.Buttons_Methods()
        #Initializa labes
        self.Record_button.setText("Start ")
        #Add Views
        self.Add_Items()
        #Labels Graphics
 
        
    def chronometer(self):
        

        self.time_label.setText(self.timeUpdater.get_Time())

    def SaveMission(self):
        self.saveData = save()
        data = list(zip(self.y_altitud,
                        self.y_presion_Interna,self.y_presion_Externa,
                        self.y_Temperature_Intern,self.y_Temperature_Extern,
                        self.y_latitud , self.y_longitud ,
                        self.y_giro_x ,self.y_giro_y ,self.y_giro_z,
                        self.y_aceleration_x, self.y_aceleration_y, self.y_aceleration_z
                        ))
        self.saveData.setPath()
        self.saveData.add_Data(data)
        self.saveData.save_Mission_Data()


    def StartMission(self):
        if not self.missionStatus:
           #identifica si hay puestos seriales conectados
           if self.comboPorts.count() == 0:        
                self.timer.timeout.connect(self.DummyMode)
                self.timer.start(100)
                #self.clock.timeout.connect(self.chronometer)
                #self.clock.start(10)
                self.missionStatus = not self.missionStatus
                self.Record_button.setText("Stop ")
                print("Demo")
                self.save_button.setEnabled(False)
           else:
                self.Record_button.setText("Stop ")
                ### prepare module
                self.com = communication()
                self.com.Set_Serial_Port(self.comboPorts.currentText())
                self.com.InitializeLora()
                ### start real mode
                self.timer.timeout.connect(self.RealMode)
                self.timer.start(100)
                self.chronometer()
                self.missionStatus = not self.missionStatus
                self.save_button.setEnabled(False)
        else :
            self.timer.stop() 
            #self.clock.stop()
            self.Record_button.setText("Start ")
            self.missionStatus = not self.missionStatus
            print("stop")
            self.save_button.setEnabled(True)

    def RealMode(self):
        data = self.com.Get_Cansat_Data()
        if data != "" :
            
            if ":" in data:
                print("carga primaria")
                self.com.Split_Data(data)
                self.UpdateGraphics(self.com.get_altitud()       , 
                                    self.com.get_Temperature_I() , self.com.get_Temperature_E() ,
                                    self.com.get_latitud()       ,self.com.get_longitud()       ,
                                    self.com.get_Presion_I()     , self.com.get_Presion_E()     ,
                                    self.com.get_aceleracion_x() ,self.com.get_aceleracion_y()  ,self.com.get_aceleracion_z(),
                                    self.com.get_giro_x()        ,self.com.get_giro_y()         ,self.com.get_giro_z(),
                                    self.com.get_battery()
                                    )
            if "^" in data:
                print("carga secundaria")

    def DummyMode(self):
        self.UpdateGraphics(
                        np.random.uniform(0, 500)
                       ,np.random.uniform(15, 30),np.random.uniform(15, 30)
                       , np.random.uniform(0, 500) , np.random.uniform(0, 500)
                       , np.random.uniform(1027, 1030), np.random.uniform(1027, 1030)
                       , np.random.uniform(0, 15), np.random.uniform(0, 15) , np.random.uniform(0, 15)
                       , np.random.uniform(0, 30), np.random.uniform(0, 30), np.random.uniform(0, 30) 
                       , np.random.uniform(0,100)) 

    def UpdateGraphics(self, Altitud = 0
                       ,TemperatureInt = 0,TemperatureExt = 0 
                       , Lat = 0 , Long  = 0
                       , PressionInt = 0, PressionExt = 0
                       , Ax = 0, Ay = 0 , Az = 0
                       , Gx = 0, Gy = 0 , Gz = 0 
                       ,Battery = 0 ):

        self.x.append(len(self.x))
        
        self.y_altitud.append(Altitud)
        self.Graph_Altitud.plot(self.x, self.y_altitud , pen = self.OrangeLines)
        #Temperature
        self.y_Temperature_Intern.append(TemperatureInt)
        self.Graph_Temperatura_Interna.plot(self.x , self.y_Temperature_Intern, pen = self.OrangeLines)

        self.y_Temperature_Extern.append(TemperatureExt)
        self.Graph_Temperatura_Externa.plot(self.x , self.y_Temperature_Extern, pen = self.OrangeLines)
        #Pression
        self.y_presion_Interna.append(PressionInt)
        self.Graph_Presion_Interna.plot(self.x , self.y_presion_Interna, pen = self.OrangeLines)
        
        self.y_presion_Externa.append(PressionExt)
        #self.Graph_Presion_Externa.plot(self.x , self.y_presion_Externa, pen = self.OrangeLines)


        self.Graph_GPS.clear()
        self.Graph_GPS.addLegend()
        self.y_latitud.append(Lat)
        self.y_longitud.append(Long)   
        self.Graph_GPS.plot(self.x , self.y_latitud  , pen = self.BlueLines   , name = 'Latitud')
        self.Graph_GPS.plot(self.x , self.y_longitud , pen = self.OrangeLines , name = 'Longitud')

        self.Graph_Giro.clear()
        self.Graph_Giro.addLegend()
        self.y_giro_x.append(Gx)
        self.y_giro_y.append(Gy) 
        self.y_giro_z.append(Gz)
        self.Graph_Giro.plot(self.x , self.y_giro_x , pen = self.BlueLines   , name = 'X')
        self.Graph_Giro.plot(self.x , self.y_giro_y , pen = self.OrangeLines , name = 'Y')
        self.Graph_Giro.plot(self.x , self.y_giro_z , pen = self.Greenlines  , name = 'Z')

        self.Graph_Aceleraciones.clear()
        self.Graph_Aceleraciones.addLegend()
        self.y_aceleration_x.append(Ax)
        self.y_aceleration_y.append(Ay) 
        self.y_aceleration_z.append(Az)
        self.Graph_Aceleraciones.plot(self.x , self.y_aceleration_x , pen = self.BlueLines   , name = 'X')
        self.Graph_Aceleraciones.plot(self.x , self.y_aceleration_y , pen = self.OrangeLines , name = 'Y')
        self.Graph_Aceleraciones.plot(self.x , self.y_aceleration_z , pen = self.Greenlines  , name = 'Z')

        #self.cylinder_widget.update_orientation()
        self.cylinder_widget.update_orientation(Gx,Gy,Gz)

        

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
    def Buttons_Methods(self):
        self.Record_button.clicked.connect(self.StartMission)
        self.buttonPorts.clicked.connect(self.UpdatePortsList)
        self.button_Config.clicked.connect(self.Show_Config)
        self.save_button.clicked.connect(self.SaveMission)
        self.abort_button.clicked.connect(self.Abort_Mission)

    def Graphics_Axes(self):
        self.x = [] 

        self.y_presion_Interna = []
        self.y_presion_Externa = []

        self.y_altitud= []
        
        self.y_Temperature_Intern = []
        self.y_Temperature_Extern = []

        self.y_latitud = []
        self.y_longitud = []

        self.y_giro_x = []
        self.y_giro_y = []
        self.y_giro_z = []

        self.y_aceleration_x = []
        self.y_aceleration_y = []
        self.y_aceleration_z = []


    def Graphics_Colors(self):
        #Background
        self.Graph_Altitud.setBackground(None)
        self.Graph_Temperatura_Interna.setBackground(None)
        self.Graph_Temperatura_Externa.setBackground(None)
        self.Graph_GPS.setBackground(None)
        self.Graph_Giro.setBackground(None)
        self.Graph_Presion_Interna.setBackground(None)
        #self.Graph_Presion_Externa.setBackground(None)
        self.Graph_GPS_2.setBackground(None)
        self.Graph_Aceleraciones.setBackground(None)
        

        #Lines
        self.OrangeLines = (245, 106, 7)
        self.BlueLines = (51 , 175 , 255)
        self.Greenlines = (51 , 255 , 79)
        #YellowLines = ()
        #PinkLines = ()
        #PurpleLines = ()


    def Add_Items(self):
        ########################## Cilinder
        self.frame_cylinder.setLayout(QVBoxLayout())
        self.cylinder_widget = CylinderWidget(self.frame_cylinder)
        self.frame_cylinder.layout().addWidget(self.cylinder_widget)
        self.frame_cylinder.layout().setContentsMargins(0, 0, 0, 0)  # Eliminar márgenes
        self.cylinder_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        #########################
    def Abort_Mission(self):
        #########################
        connfimr = True
        #connfirm = open view  get value
        if(connfimr):
            #stop timers
            self.timer.stop()
            #self.clock.stop()
            #self.timeUpdater.initialize_Time()
            #self.chronometer()
            #clear axes data
            self.Graphics_Axes()
            self.UpdateGraphics(0,0,0,0,0)
            #clear Graphics
            self.Graph_Altitud.clear()
            self.Graph_Temperatura_Interna.clear()
            self.Graph_Temperatura_Externa.clear()
            self.Graph_GPS.clear()
            self.Graph_Giro.clear()
            self.Graph_Presion_Interna.clear()
            #self.Graph_Presion_Externa.clear()
            self.Graph_GPS_2.clear()
            self.Graph_Aceleraciones.clear()
            #change buttons, and stop mission
            if ( self.missionStatus):
                self.missionStatus = False
            self.time_label.setText(" 00:00:00 ")
            self.Record_button.setText("Start ")
            self.Graphics_Axes() 
        #########################
app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec()
