# Libraire necessaire
import sys
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap

# Instance de l'aplication
app = QApplication(sys.argv)

# Créer une fenêtre
root = QWidget()
root.resize(1080, 720)
root.setWindowTitle("Siv - Conexion")

# Créer un label
label = QLabel(root)

# Image ( Logo )
pixmap = QPixmap('./src/logo.png')
label.setPixmap(pixmap)

x = 500
y = 400
label.setGeometry(x, y, pixmap.width(), pixmap.height())



# Créer un layout vertical
layout = QVBoxLayout()
layout.addWidget(label)


# Définir le layout pour la fenêtre
root.setLayout(layout)

# definir la couleur de fond
root.setStyleSheet("background-color: rgb(255, 255, 255)")

# Afficher la fenêtre
root.show()

sys.exit(app.exec_())
