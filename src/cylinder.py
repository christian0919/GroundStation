import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame, QWidget
from PySide6.Qt3DCore import Qt3DCore
from PySide6.Qt3DExtras import Qt3DExtras
from PySide6.QtGui import QVector3D, QColor
from PySide6.QtCore import QTimer


class CylinderWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        # Crear la vista 3D
        self.view = Qt3DExtras.Qt3DWindow()
        container = QWidget.createWindowContainer(self.view)
        layout.addWidget(container)

        # Crear escena
        self.scene = Qt3DCore.QEntity()
        self.view.setRootEntity(self.scene)

        # Crear cámara
        self.camera = self.view.camera()
        self.camera.setPosition(QVector3D(0, 0, 10))
        self.camera.setViewCenter(QVector3D(0, 0, 0))

        # Crear objeto 3D (cilindro)
        self.mesh = Qt3DExtras.QCylinderMesh()
        self.mesh.setLength(3.0)  # Cambiar el largo del cilindro a 3 unidades
        self.transform = Qt3DCore.QTransform()
        self.material = Qt3DExtras.QPhongMaterial()

        self.entity = Qt3DCore.QEntity(self.scene)
        self.entity.addComponent(self.mesh)
        self.entity.addComponent(self.transform)
        self.entity.addComponent(self.material)

        # Configurar color del material (rojo)
        self.material.setDiffuse(QColor(255, 0, 0))

        # Obtener datos de orientación del MPU9250 (solo simulados en este ejemplo)
        self.orientation_data = QTimer(self)
        self.orientation_data.timeout.connect(self.update_orientation)
        self.orientation_data.start(50)  # Actualizar cada 50 ms (20 veces por segundo)

    def update_orientation(self):
        # Simulación de datos de orientación (reemplaza esto con tus datos reales del MPU9250)
        # Suponemos que recibimos datos de ángulos de Euler (roll, pitch, yaw)
        roll = 0  # Obtén el ángulo de balanceo desde el MPU9250
        pitch = 0  # Obtén el ángulo de inclinación desde el MPU9250
        yaw = 0  # Obtén el ángulo de dirección desde el MPU9250

        # Aplicar la orientación al objeto 3D
        self.transform.setRotationX(roll)
        self.transform.setRotationY(pitch)
        self.transform.setRotationZ(yaw)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Visualización de cilindro con orientación desde MPU9250")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        layout = QVBoxLayout(self.central_widget)

        # Crear un QFrame
        self.frame = QFrame()
        layout.addWidget(self.frame)

        # Insertar visualización del cilindro en el QFrame
        self.cylinder_widget = CylinderWidget(self.frame)
        frame_layout = QVBoxLayout(self.frame)
        frame_layout.addWidget(self.cylinder_widget)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
