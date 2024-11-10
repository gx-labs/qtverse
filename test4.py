from PySide2.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout
from PySide2.QtCore import Qt
# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Styled LineEdit Example")

# Create a QLineEdit
line_edit = QLineEdit()
line_edit.setPlaceholderText("Your name")
line_edit.setStyleSheet("""
    QLineEdit {
        border: 2px solid #1E90FF;
        border-radius: 10px;
        padding: 8px;
        font-size: 16px;
        color: gray;
    }
    QLineEdit:focus {
        border: 2px solid #1E90FF;
        background-color: white;
        color: black;
        box-shadow: 0 0 10px #1E90FF;
    }
""")

# Create a layout and add the QLineEdit to it
layout = QVBoxLayout()
layout.addWidget(line_edit)
layout.setAlignment(Qt.AlignCenter)

# Set the layout to the main window
window.setLayout(layout)

# Show the window
window.resize(400, 100)
window.show()

# Execute the application
app.exec_()
