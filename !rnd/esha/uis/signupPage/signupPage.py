import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QCheckBox, QSpacerItem, QSizePolicy
from PySide2.QtCore import QSize, Qt

class signupPage(QWidget):
    def __init__(self):
        super().__init__()

        # Window properties
        self.setWindowTitle("Sign Up")
        self.setFixedSize(QSize(400, 700))  
               
#_____________Window layout____________

        window_layout = QHBoxLayout()

        # Set layout for the main window
        self.setLayout(window_layout)

        # ----- Horizontal Spacer -----
        self.left_spacer = QSpacerItem(60,20)
        window_layout.addItem(self.left_spacer)

#_____________Signup layout____________
  
        signup_layout = QVBoxLayout()

        # vertical spacer at Top
        self.top_spacer = QSpacerItem(20,245)
        signup_layout.addItem(self.top_spacer)

        # ----- Sign Up Label -----
        self.signup = QLabel("Sign Up")
        self.signup.setAlignment(Qt.AlignCenter)

        self.signup_font = self.signup.font()
        self.signup_font.setPointSize(12)
        self.signup_font.setBold(True) 
        self.signup.setFont(self.signup_font)
        
        signup_layout.addWidget(self.signup)

#______________Name layout_______________

        nameInput_layout = QHBoxLayout()

        # ----- Name Input ----
        self.name_label = QLabel("Name")
        self.name_input = QLineEdit()

        # Adding widgets to nameInput_layout
        nameInput_layout.addWidget(self.name_label)
        nameInput_layout.addWidget(self.name_input)

        # Adding nameInput_layout to signup_layout
        signup_layout.addLayout(nameInput_layout)

#_____________Password layout________________

        passwordInput_layout = QHBoxLayout()

        # ----- Password Input -----
        self.password_label = QLabel("Password")
        self.password_input = QLineEdit()   

        # Adding widgets to passwordInput_layout
        passwordInput_layout.addWidget(self.password_label)
        passwordInput_layout.addWidget(self.password_input)
 
        # Adding passwordInput_layout to signup_layout
        signup_layout.addLayout(passwordInput_layout)
        
        # ----- Check box ----
        self.check_box = QCheckBox("Agree with our conditions")
        signup_layout.addWidget(self.check_box)

#___________register button layout______________

        registerBtn_layout = QVBoxLayout()
        #registerBtn_layout.setAlignment(Qt.AlignCenter)  
       
        # ----- register button -----
        self.register_btn = QPushButton("Register")
        self.register_btn.setMaximumWidth(100)
        registerBtn_layout.addWidget(self.register_btn,alignment=Qt.AlignCenter)
        
        signup_layout.addLayout(registerBtn_layout)

#____________login button layout_________________

        loginBtn_layout = QVBoxLayout()

        # ----- Login button -----
        self.login_btn = QPushButton("Already Registered? Login")
        self.login_btn.setMaximumWidth(200)
        self.login_btn.setFlat(True)
        loginBtn_layout.addWidget(self.login_btn,alignment=Qt.AlignCenter)

        signup_layout.addLayout(loginBtn_layout)

        # Vertical Spacer at bottom      
        self.botton_spacer = QSpacerItem(20,265)
        signup_layout.addItem(self.botton_spacer)

        window_layout.addLayout(signup_layout)

        # Horizontal Spacer at Right      
        self.right_spacer = QSpacerItem(60,20)
        window_layout.addItem(self.right_spacer)

def main():
        app = QApplication(sys.argv)
        window = signupPage()
        window.show()
        sys.exit(app.exec_())

if __name__ == '__main__':
    main()

