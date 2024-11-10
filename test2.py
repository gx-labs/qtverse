from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide2.QtCore import Qt

# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Styled Button Example")

# Create a button
button = QPushButton("HOVER ME")

# Set the button's stylesheet
button.setStyleSheet("""
    QPushButton {
        background-color: #000000;
        color: #DAA520;
        border: 2px solid #DAA520;
        border-radius: 15px;
        font-size: 14px;
        padding: 5px 15px;
    }
    QPushButton:hover {
        background-color: #333333;
    }
    QPushButton:pressed {
        background-color: #555555;
    }
""")

# Create a layout and add the button to it
layout = QVBoxLayout()
layout.addWidget(button)
layout.setAlignment(Qt.AlignCenter)

# Set the layout to the main window
window.setLayout(layout)

# Show the window
window.resize(300, 200)
window.show()

# Execute the application
app.exec_()
