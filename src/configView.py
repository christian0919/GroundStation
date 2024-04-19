from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt
from config import config
class configView(QDialog):
    def __init__(self):
        super().__init__()

        # Cargar el archivo UI
        loader = QUiLoader()
        ui_file = QFile("Views/Config_View.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()
        
        layout = QVBoxLayout()
        layout.addWidget(self.ui)

        self.setLayout(layout)
        # Conectar señales y slots
        self.ui.ok_button.clicked.connect(self.ok)
        self.ui.cancel_button.clicked.connect(self.cancel)
        self.configuration = config()
        self.ui.spinAddr.setValue(self.configuration.get_LoRa_ADDRESS())
        self.ui.spinNetwork.setValue(self.configuration.get_LoRa_NETWORKID())
        self.ui.spinSpread.setValue(self.configuration.get_LoRa_SPREADING_FACTOR())
        self.ui.spinBandwidth.setValue(self.configuration.get_LoRa_BANDWIDTH())
        self.ui.spinCoding.setValue(self.configuration.get_LoRa_CODING_RATE())
        self.ui.spinPreamble.setValue(self.configuration.get_LoRa_PROGRAMMED_PREAMBLE())



    def ok(self): 
        self.configuration.Set_Values(self.ui.spinAddr.value(),
                                      self.ui.spinNetwork.value(),
                                      self.ui.comboBand.currentText(),
                                      self.ui.spinSpread.value(),
                                      self.ui.spinBandwidth.value(),
                                      self.ui.spinCoding.value(),
                                      self.ui.spinPreamble.value())
        self.accept()
    def cancel(self):
        self.accept()

