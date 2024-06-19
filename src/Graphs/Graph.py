import pyqtgraph as pg
from PySide6.QtWidgets import QGroupBox, QVBoxLayout, QWidget

class GraphBox_Number(QGroupBox):
    def __init__(self, parent=None):
        super().__init__("Name", parent)
        self.layout = QVBoxLayout(self)
        self.plot_widget = pg.PlotWidget()
        self.layout.addWidget(self.plot_widget)
        self.plot_widget.setBackground(None)
        self.plot_widget.setLabel('left', 'Valores Y')
        self.plot_widget.setLabel('bottom', 'Valores X')
        self.plot_widget.addLegend()

        # Ejemplo de datos
        self.plot_widget.plot([1, 2, 3, 4, 5], [10, 20, 30, 40, 50], pen='r', name='Línea 1')

