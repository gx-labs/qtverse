import sys
from PySide2.QtWidgets import * 
from PySide2.QtCore import *
from PySide2.QtGui import *

class stackedWidget(QWidget):

   def __init__(self):
      super().__init__()
     
      # self.setFixedSize(500,400)
      #stacked widget
      self.stacked_widget = QStackedWidget(self)

      cpuPage = QWidget(self)
      cpuPageLayout = QVBoxLayout(cpuPage)
      cpuPageLayout.addWidget(QLabel("CPU INFO"))
      batteryPage = QWidget(self)
      batteryPageLayout=QVBoxLayout(batteryPage)
      batteryPageLayout.addWidget(QLabel("BATTERY INFO"))
        
      self.stacked_widget.addWidget(cpuPage)
      self.stacked_widget.addWidget(batteryPage)

      #button menu 
      self.button_menu=QWidget(self)
      self.button_menuLayout = QVBoxLayout(self.button_menu)
      self.button_menuLayout.addWidget(QPushButton("CPU", self, clicked=self.cpu_page))
      self.button_menuLayout.addWidget(QPushButton("BATTERY", self, clicked=self.battery_page))

      main_layout = QHBoxLayout()
      self.setLayout(main_layout)
      main_layout.addWidget(self.button_menu)
      main_layout.addWidget(self.stacked_widget)
      self.setGeometry(300, 300, 400, 200)

   def cpu_page(self):
      self.stacked_widget.setCurrentIndex(0)

   def battery_page(self):
      self.stacked_widget.setCurrentIndex(1)  
        
    
def main():
   app = QApplication(sys.argv)
   example = stackedWidget()
   example.show()
   sys.exit(app.exec_())

if __name__ == '__main__':
    main()



