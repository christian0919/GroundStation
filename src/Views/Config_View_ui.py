# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Config_View.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QGridLayout,
    QGroupBox, QHBoxLayout, QPushButton, QSizePolicy,
    QSpinBox, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(389, 446)
        font = QFont()
        font.setFamilies([u"Hack Nerd Font"])
        font.setPointSize(10)
        Dialog.setFont(font)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_3 = QGroupBox(self.groupBox)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.spinNetwork = QSpinBox(self.groupBox_3)
        self.spinNetwork.setObjectName(u"spinNetwork")

        self.horizontalLayout_2.addWidget(self.spinNetwork)


        self.gridLayout.addWidget(self.groupBox_3, 0, 1, 1, 1)

        self.groupBox_9 = QGroupBox(self.groupBox)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.groupBox_9.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.spinBandwidth = QSpinBox(self.groupBox_9)
        self.spinBandwidth.setObjectName(u"spinBandwidth")

        self.horizontalLayout_7.addWidget(self.spinBandwidth)


        self.gridLayout.addWidget(self.groupBox_9, 4, 0, 1, 1)

        self.groupBox_7 = QGroupBox(self.groupBox)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(16777215, 70))
        self.groupBox_7.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.spinAddr = QSpinBox(self.groupBox_7)
        self.spinAddr.setObjectName(u"spinAddr")

        self.horizontalLayout_3.addWidget(self.spinAddr)


        self.gridLayout.addWidget(self.groupBox_7, 0, 0, 1, 1)

        self.groupBox_8 = QGroupBox(self.groupBox)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.groupBox_8.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.comboBand = QComboBox(self.groupBox_8)
        self.comboBand.addItem("")
        self.comboBand.addItem("")
        self.comboBand.setObjectName(u"comboBand")

        self.horizontalLayout_5.addWidget(self.comboBand)


        self.gridLayout.addWidget(self.groupBox_8, 2, 0, 1, 1)

        self.groupBox_4 = QGroupBox(self.groupBox)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.spinSpread = QSpinBox(self.groupBox_4)
        self.spinSpread.setObjectName(u"spinSpread")

        self.horizontalLayout_4.addWidget(self.spinSpread)


        self.gridLayout.addWidget(self.groupBox_4, 2, 1, 1, 1)

        self.groupBox_5 = QGroupBox(self.groupBox)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.spinCoding = QSpinBox(self.groupBox_5)
        self.spinCoding.setObjectName(u"spinCoding")

        self.horizontalLayout_6.addWidget(self.spinCoding)


        self.gridLayout.addWidget(self.groupBox_5, 4, 1, 1, 1)

        self.groupBox_10 = QGroupBox(self.groupBox)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.groupBox_10.setMaximumSize(QSize(16777215, 70))
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.spinPreamble = QSpinBox(self.groupBox_10)
        self.spinPreamble.setObjectName(u"spinPreamble")

        self.horizontalLayout_9.addWidget(self.spinPreamble)


        self.gridLayout.addWidget(self.groupBox_10, 7, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 80))
        self.groupBox_2.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.ok_button = QPushButton(self.groupBox_2)
        self.ok_button.setObjectName(u"ok_button")
        self.ok_button.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.ok_button, 0, Qt.AlignTop)

        self.cancel_button = QPushButton(self.groupBox_2)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setMinimumSize(QSize(0, 20))

        self.horizontalLayout.addWidget(self.cancel_button, 0, Qt.AlignTop)


        self.verticalLayout.addWidget(self.groupBox_2, 0, Qt.AlignTop)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Config", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"LoRa ", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"NETWORKID", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Dialog", u"BANDWIDTH", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Dialog", u"ADDRESS", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Dialog", u"BAND", None))
        self.comboBand.setItemText(0, QCoreApplication.translate("Dialog", u"915000000", None))
        self.comboBand.setItemText(1, QCoreApplication.translate("Dialog", u"863000000", None))

        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"SPREADING FACTOR", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"CODING RATE", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Dialog", u"PROGRAMMED PREAMBLE", None))
        self.groupBox_2.setTitle("")
        self.ok_button.setText(QCoreApplication.translate("Dialog", u" OK \u2705", None))
        self.cancel_button.setText(QCoreApplication.translate("Dialog", u"Cancel \u2718", None))
    # retranslateUi

