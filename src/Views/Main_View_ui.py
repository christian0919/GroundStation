# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Main_View.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QLabel,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(886, 573)
        font = QFont()
        font.setFamilies([u"Hack Nerd Font"])
        font.setBold(True)
        Dialog.setFont(font)
        Dialog.setWindowTitle(u"\ud83d\udc3a Ground Station \ud83d\udc7e")
        self.horizontalLayout_2 = QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(Dialog)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_7 = QGroupBox(self.frame_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.Graph_GPS = PlotWidget(self.groupBox_7)
        self.Graph_GPS.setObjectName(u"Graph_GPS")

        self.horizontalLayout_7.addWidget(self.Graph_GPS)

        self.Graph_GPS_2 = PlotWidget(self.groupBox_7)
        self.Graph_GPS_2.setObjectName(u"Graph_GPS_2")

        self.horizontalLayout_7.addWidget(self.Graph_GPS_2)


        self.gridLayout.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.frame_2)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMinimumSize(QSize(0, 200))
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, -1, -1)
        self.groupBox_16 = QGroupBox(self.groupBox_8)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.horizontalLayout_15 = QHBoxLayout(self.groupBox_16)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.Graph_Giro = PlotWidget(self.groupBox_16)
        self.Graph_Giro.setObjectName(u"Graph_Giro")

        self.horizontalLayout_15.addWidget(self.Graph_Giro)


        self.horizontalLayout_6.addWidget(self.groupBox_16)

        self.groupBox_17 = QGroupBox(self.groupBox_8)
        self.groupBox_17.setObjectName(u"groupBox_17")
        self.horizontalLayout_16 = QHBoxLayout(self.groupBox_17)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.Graph_Aceleraciones = PlotWidget(self.groupBox_17)
        self.Graph_Aceleraciones.setObjectName(u"Graph_Aceleraciones")

        self.horizontalLayout_16.addWidget(self.Graph_Aceleraciones)


        self.horizontalLayout_6.addWidget(self.groupBox_17)

        self.frame_cylinder = QFrame(self.groupBox_8)
        self.frame_cylinder.setObjectName(u"frame_cylinder")
        self.frame_cylinder.setMinimumSize(QSize(100, 0))
        self.frame_cylinder.setAutoFillBackground(False)
        self.frame_cylinder.setFrameShape(QFrame.StyledPanel)
        self.frame_cylinder.setFrameShadow(QFrame.Raised)
        self.frame_cylinder.setLineWidth(0)

        self.horizontalLayout_6.addWidget(self.frame_cylinder)


        self.gridLayout.addWidget(self.groupBox_8, 5, 0, 1, 2)

        self.groupBox_5 = QGroupBox(self.frame_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.Graph_Altitud = PlotWidget(self.groupBox_5)
        self.Graph_Altitud.setObjectName(u"Graph_Altitud")

        self.horizontalLayout_3.addWidget(self.Graph_Altitud)


        self.gridLayout.addWidget(self.groupBox_5, 0, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.frame_2)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.groupBox_13 = QGroupBox(self.groupBox_9)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.horizontalLayout_12 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.Graph_Presion_Interna = PlotWidget(self.groupBox_13)
        self.Graph_Presion_Interna.setObjectName(u"Graph_Presion_Interna")

        self.horizontalLayout_12.addWidget(self.Graph_Presion_Interna)


        self.horizontalLayout_5.addWidget(self.groupBox_13)


        self.gridLayout.addWidget(self.groupBox_9, 1, 1, 1, 1)

        self.groupBox_6 = QGroupBox(self.frame_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.groupBox_11 = QGroupBox(self.groupBox_6)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setMinimumSize(QSize(0, 100))
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.Graph_Temperatura_Interna = PlotWidget(self.groupBox_11)
        self.Graph_Temperatura_Interna.setObjectName(u"Graph_Temperatura_Interna")

        self.horizontalLayout_10.addWidget(self.Graph_Temperatura_Interna)


        self.horizontalLayout_4.addWidget(self.groupBox_11)

        self.groupBox_12 = QGroupBox(self.groupBox_6)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.Graph_Temperatura_Externa = PlotWidget(self.groupBox_12)
        self.Graph_Temperatura_Externa.setObjectName(u"Graph_Temperatura_Externa")

        self.horizontalLayout_11.addWidget(self.Graph_Temperatura_Externa)


        self.horizontalLayout_4.addWidget(self.groupBox_12)


        self.gridLayout.addWidget(self.groupBox_6, 1, 0, 1, 1)


        self.horizontalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(200, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.groupBox_4 = QGroupBox(self.frame)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.verticalLayout = QVBoxLayout(self.groupBox_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_3 = QLabel(self.groupBox_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label_3)

        self.frame_3 = QFrame(self.groupBox_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.comboPorts = QComboBox(self.frame_3)
        self.comboPorts.setObjectName(u"comboPorts")
        font1 = QFont()
        font1.setFamilies([u"Hack Nerd Font"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.comboPorts.setFont(font1)

        self.horizontalLayout_8.addWidget(self.comboPorts, 0, Qt.AlignTop)

        self.buttonPorts = QPushButton(self.frame_3)
        self.buttonPorts.setObjectName(u"buttonPorts")
        self.buttonPorts.setMaximumSize(QSize(25, 24))
        font2 = QFont()
        font2.setFamilies([u"Hack Nerd Font"])
        font2.setPointSize(13)
        font2.setBold(True)
        self.buttonPorts.setFont(font2)

        self.horizontalLayout_8.addWidget(self.buttonPorts, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_4 = QFrame(self.groupBox_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(16777215, 200))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 20)
        self.Record_button = QPushButton(self.frame_4)
        self.Record_button.setObjectName(u"Record_button")
        self.Record_button.setEnabled(True)
        font3 = QFont()
        font3.setFamilies([u"Hack Nerd Font"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.Record_button.setFont(font3)

        self.verticalLayout_2.addWidget(self.Record_button)

        self.save_button = QPushButton(self.frame_4)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setFont(font3)

        self.verticalLayout_2.addWidget(self.save_button)

        self.abort_button = QPushButton(self.frame_4)
        self.abort_button.setObjectName(u"abort_button")
        self.abort_button.setFont(font3)

        self.verticalLayout_2.addWidget(self.abort_button)


        self.verticalLayout.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.groupBox_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_5)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout_3.addWidget(self.label)

        self.time_label = QLabel(self.frame_5)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setMinimumSize(QSize(0, 20))
        self.time_label.setMaximumSize(QSize(16777215, 30))
        font4 = QFont()
        font4.setFamilies([u"Hack Nerd Font"])
        font4.setPointSize(14)
        font4.setBold(True)
        self.time_label.setFont(font4)
        self.time_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.time_label)


        self.verticalLayout.addWidget(self.frame_5)

        self.label_2 = QLabel(self.groupBox_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))

        self.verticalLayout.addWidget(self.label_2, 0, Qt.AlignBottom)

        self.button_Config = QPushButton(self.groupBox_4)
        self.button_Config.setObjectName(u"button_Config")
        self.button_Config.setMinimumSize(QSize(50, 20))

        self.verticalLayout.addWidget(self.button_Config)


        self.verticalLayout_4.addWidget(self.groupBox_4)


        self.horizontalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"GPS", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Dialog", u"Giroscopio", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Dialog", u"Giro", None))
        self.groupBox_17.setTitle(QCoreApplication.translate("Dialog", u"Aceleraci\u00f3n", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Altura", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Dialog", u"Presi\u00f3n", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Dialog", u"Interna", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Dialog", u"Temperatura ", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Dialog", u"Interna", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Dialog", u"Externa", None))
        self.groupBox_4.setTitle("")
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Serial Ports", None))
        self.buttonPorts.setText(QCoreApplication.translate("Dialog", u"\uf002", None))
        self.Record_button.setText("")
        self.save_button.setText(QCoreApplication.translate("Dialog", u"Save \uf0c7", None))
        self.abort_button.setText(QCoreApplication.translate("Dialog", u"Abortar \uf46e", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Hora de Inicio", None))
        self.time_label.setText(QCoreApplication.translate("Dialog", u"00:00:00", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Config", None))
        self.button_Config.setText(QCoreApplication.translate("Dialog", u"\ue615", None))
        pass
    # retranslateUi

