import os
import sys

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

css_file = os.path.join(os.path.dirname(__file__), "style.css")
if os.path.exists(css_file):
    with open(css_file, 'r') as f:
        css_data = f.read()
else:
    print("CSS File does not exist")
class CheckableComboBox(QComboBox): 
      
    def __init__(self, parent = None): 
        super(CheckableComboBox, self).__init__(parent) 
        self.view().pressed.connect(self.handleItemPressed) 
        self.setModel(QStandardItemModel(self)) 
  
    def handleItemPressed(self, index): 
          
        item = self.model().itemFromIndex(index) 
          
        if item.checkState() == Qt.Checked: 
              
            item.setCheckState(Qt.Unchecked) 
              
        else: 
            item.setCheckState(Qt.Checked)

class CustomWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        self.combo_box = CheckableComboBox(self) 
        self.combo_box.setFixedSize(250, 40)
        self.combo_box.addItem("Bootstrap")
        self.combo_box.addItem("Angular")
        self.combo_box.addItem("JavaScript")

        self.combo_box.setStyleSheet(css_data)

        self.setLayout(layout)
        layout.addWidget(self.combo_box, alignment=Qt.AlignCenter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = CustomWidget()
    widget.show()
    sys.exit(app.exec_())