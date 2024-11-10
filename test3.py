from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QLabel
from PySide2.QtGui import QFont, QPixmap
from PySide2.QtCore import Qt

app = QApplication([])

window = QWidget()
window.setWindowTitle("Styled Button Example")

button = QPushButton()
button_layout = QHBoxLayout(button)

# Create a label for the checkmark icon
checkmark_label = QLabel()
checkmark_pixmap = QPixmap("checkmark.png")
checkmark_label.setPixmap(checkmark_pixmap)
button_layout.addWidget(checkmark_label)

# Create a label for the button text
text_label = QLabel("LOOK I'M A BUTTON")
text_label.setFont(QFont("Arial", 12, QFont.Bold))
text_label.setStyleSheet("color: white;")
button_layout.addWidget(text_label)

button_layout.setSpacing(10)
button_layout.setAlignment(Qt.AlignCenter)

# Set the button's stylesheet
button.setFixedSize(220, 55)
button.setStyleSheet("""
    QPushButton {
        background-color: #1E75B8;
        border: none;
        border-radius: 10px;
        padding: 10px 20px;
    }
    QPushButton:hover {
        background-color: #166499;
    }
    QPushButton:pressed {
        background-color: #12527A;
    }
""")

# Create a layout and add the button to it
main_layout = QHBoxLayout()
main_layout.addWidget(button)
main_layout.setAlignment(Qt.AlignCenter)

# Set the layout to the main window
window.setLayout(main_layout)

# Show the window
window.show()

# Execute the application
app.exec_()
