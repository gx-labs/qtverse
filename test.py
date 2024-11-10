from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout
from PySide2.QtCore import Qt

# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Styled Button Example")

# Create a button
button = QPushButton("BUTTON 1")

# Set the button's stylesheet
button.setStyleSheet("""
    QPushButton {
        color: #E94E3C;
        border: 2px solid #E94E3C;
        border-radius: 10px;
        font-size: 14px;
        padding: 5px 10px;
    }
    QPushButton:hover {
        background-color: #E94E3C;
        color: white;
    }
    QPushButton:pressed {
        background-color: #162C42;
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
