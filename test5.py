from PySide2.QtWidgets import QApplication, QLineEdit, QWidget, QVBoxLayout, QHBoxLayout, QLabel
from PySide2.QtCore import Qt

# Create the application
app = QApplication([])

# Create the main window
window = QWidget()
window.setWindowTitle("Styled LineEdit Example")

# Create QLineEdit widgets
first_name_edit = QLineEdit()
first_name_edit.setPlaceholderText("First Name")

last_name_edit = QLineEdit()
last_name_edit.setPlaceholderText("Last Name")

email_address_edit = QLineEdit()
email_address_edit.setPlaceholderText("Email Address")

email_confirm_edit = QLineEdit()
email_confirm_edit.setPlaceholderText("Email Confirm")

# Set the QLineEdit's stylesheet
line_edit_style = """
    QLineEdit {
        border: 2px solid #FF5252;
        border-radius: 15px;
        padding: 10px;
        font-size: 14px;
        color: #FF5252;
    }
    QLineEdit:focus {
        background-color: #FF5252;
        color: white;
    }
"""

first_name_edit.setStyleSheet(line_edit_style)
last_name_edit.setStyleSheet(line_edit_style)
email_address_edit.setStyleSheet(line_edit_style)
email_confirm_edit.setStyleSheet(line_edit_style)

# Create labels
first_name_label = QLabel("First Name")
last_name_label = QLabel("Last Name")
email_address_label = QLabel("Email Address")
email_confirm_label = QLabel("Email Confirm")

# Set the QLabel's stylesheet
label_style = """
    QLabel {
        font-size: 14px;
        color: #FF5252;
    }
"""

first_name_label.setStyleSheet(label_style)
last_name_label.setStyleSheet(label_style)
email_address_label.setStyleSheet(label_style)
email_confirm_label.setStyleSheet(label_style)

# Create layouts for each row
first_name_layout = QHBoxLayout()
first_name_layout.addWidget(first_name_label)
first_name_layout.addWidget(first_name_edit)

last_name_layout = QHBoxLayout()
last_name_layout.addWidget(last_name_label)
last_name_layout.addWidget(last_name_edit)

email_address_layout = QHBoxLayout()
email_address_layout.addWidget(email_address_label)
email_address_layout.addWidget(email_address_edit)

email_confirm_layout = QHBoxLayout()
email_confirm_layout.addWidget(email_confirm_label)
email_confirm_layout.addWidget(email_confirm_edit)

# Create the main layout and add the row layouts to it
main_layout = QVBoxLayout()
main_layout.addLayout(first_name_layout)
main_layout.addLayout(last_name_layout)
main_layout.addLayout(email_address_layout)
main_layout.addLayout(email_confirm_layout)
main_layout.setAlignment(Qt.AlignTop)
main_layout.setSpacing(20)

# Set the layout to the main window
window.setLayout(main_layout)

# Show the window
window.resize(500, 300)
window.show()

# Execute the application
app.exec_()
