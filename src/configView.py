from PySide6.QtWidgets import QDialog, QVBoxLayout
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile, Qt

class configView(QDialog):
    def __init__(self):
        super().__init__()

        # Cargar el archivo UI
        loader = QUiLoader()
        ui_file = QFile("Config_View.ui")
        ui_file.open(QFile.ReadOnly)
        self.ui = loader.load(ui_file)
        ui_file.close()
        
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        self.setLayout(layout)
        # Conectar señales y slots
        self.ui.ok_button.clicked.connect(self.ok)
        self.ui.cancel_button.clicked.connect(self.cancel)
    
    def ok(self): 
        self.accept()
    def cancel(self):
        self.accept()

