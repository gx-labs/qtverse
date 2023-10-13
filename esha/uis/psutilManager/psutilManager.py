import sys
from PySide2.QtWidgets import (QApplication,QWidget,QLabel,QGridLayout,QPushButton,QStackedWidget,QAction,QHBoxLayout,QVBoxLayout,QSizePolicy,QTextEdit)
from PySide2.QtGui import QFont,  QIcon, QPixmap
from PySide2.QtCore import Qt, QSize, Signal

class psutilManager(QWidget):
    def __init__(self):                                          
        super().__init__()

        self.setWindowTitle("PSUTIL MANAGER")
        self.setFixedSize(QSize(1000, 700))     
        self.windowLayout=QHBoxLayout()
        self.windowLayout.setContentsMargins(0,0,0,0)
        self.windowLayout.setSpacing(0)
        self.setLayout(self.windowLayout)

        self.appLayout=QVBoxLayout()

#_____________________________________
#              HEADER
#_____________________________________

        self.header=QWidget()
        self.headerLayout=QHBoxLayout()
        #__________________________________
        #________LEFT_MENU_BUTTON__________

        self.left_header_widget=QWidget()
        self.leftHeaderLayout=QHBoxLayout(self.left_header_widget)
        self.leftHeaderLayout.setContentsMargins(0,9,9,9)
        self.leftHeaderLayout.setSpacing(0)
        self.menu_btn=QPushButton(QIcon('icons/menu.png'),"MENU")
        self.menu_btn.setFlat(True)
        font_menuBtn=self.menu_btn.font()
        font_menuBtn.setBold(True)
        font_menuBtn.setPointSize(10)
        self.menu_btn.setFont(font_menuBtn)
        self.leftHeaderLayout.addWidget(self.menu_btn)
        self.headerLayout.addWidget(self.left_header_widget,0, Qt.AlignLeft|Qt.AlignTop)

        #___________________________________
        #________CENTER_PSUTIL_LABEL________  
          
        self.center_header_widget=QWidget()
        self.centerHeaderLayout=QHBoxLayout(self.center_header_widget)
        self.icon_label=QLabel()
        psutil_icon=QPixmap('icons/airplay.png')
        psutil_icon=psutil_icon.scaled(20,20)
        self.icon_label.setPixmap(psutil_icon)
        self.centerHeaderLayout.addWidget(self.icon_label)
        self.psutilManager_label=QLabel("PSUTIL MANAGER")
        font_psutilLabel=self.psutilManager_label.font()
        font_psutilLabel.setBold(True)
        font_psutilLabel.setPointSize(12)
        self.psutilManager_label.setFont( font_psutilLabel)
        self.centerHeaderLayout.addWidget(self.psutilManager_label)
        self.headerLayout.addWidget(self.center_header_widget,0, Qt.AlignLeft|Qt.AlignTop)
       
        #_______________________________________
        #__________RIGHT_MINMAX_BUTTONS_________        
       
        self.right_header_widget=QWidget()
        self.rightHeaderLayout=QHBoxLayout(self.right_header_widget)
        self.rightHeaderLayout.setContentsMargins(9,9,9,9)
        self.rightHeaderLayout.setSpacing(0)
        self.minimize_btn=QPushButton()
        self.maximize_btn=QPushButton()
        self.close_btn=QPushButton()
        self.rightHeaderLayout.addWidget(self.minimize_btn)
        self.rightHeaderLayout.addWidget(self.maximize_btn)
        self.rightHeaderLayout.addWidget(self.close_btn)
        self.headerLayout.addWidget(self.right_header_widget,0, Qt.AlignRight|Qt.AlignTop)
      
        self.appLayout.addLayout(self.headerLayout)

#_____________________________________
#              MIDDLE
#_____________________________________      

        self.middle=QWidget()
        self.middleLayout=QHBoxLayout()
        self.middleLayout.setContentsMargins(9,9,0,0)
        self.middleLayout.setSpacing(0)

        #_______________________________
        #___________LEFT_MENU___________
        
        self.left_middle_widget=QWidget()
        self.left_middle_widget.setMinimumWidth(175)      
        self.leftMenuLayout=QVBoxLayout(self.left_middle_widget)
        self.leftMenuLayout.setContentsMargins(0,0,0,0)
        self.leftMenuLayout.setSpacing(0)
        
        # CPU button       
        self.cpu_btn=QPushButton(QIcon('icons/cpu.png'),"CPU",clicked = self.cpu_page)
        self.cpu_btn.setStyleSheet("text-align: left;") 
        self.cpu_btn.setFlat(True)
        font_cpuBtn=self.cpu_btn.font()
        font_cpuBtn.setPointSize(10)
        self.cpu_btn.setFont(font_cpuBtn)
        self.leftMenuLayout.addWidget(self.cpu_btn)        
        # Battery button       
        self.battery_btn=QPushButton(QIcon('icons/battery.png'),"Battery", clicked=self.battery_page)
        self.battery_btn.setStyleSheet("text-align: left;") 
        self.battery_btn.setFlat(True)
        font_batteryBtn=self.battery_btn.font()
        font_batteryBtn.setPointSize(10)
        self.battery_btn.setFont(font_batteryBtn)        
        self.leftMenuLayout.addWidget(self.battery_btn)       
        # System info button
        self.systeminfo_btn=QPushButton(QIcon('icons/desktop.png'),"System Information",clicked=self.systeminfo_page)
        self.systeminfo_btn.setStyleSheet("text-align: left;") 
        self.systeminfo_btn.setFlat(True)
        font_systeminfoBtn=self.systeminfo_btn.font()
        font_systeminfoBtn.setPointSize(10)
        self.systeminfo_btn.setFont(font_systeminfoBtn)         
        self.leftMenuLayout.addWidget(self.systeminfo_btn)                                      
        # Activities button
        self.activities_btn=QPushButton(QIcon('icons/activities.png'),"Activities",clicked=self.activity_page)
        self.activities_btn.setStyleSheet("text-align: left;") 
        self.activities_btn.setFlat(True)
        font_activitiesBtn=self.activities_btn.font()
        font_activitiesBtn.setPointSize(10)
        self.activities_btn.setFont(font_activitiesBtn)
        self.leftMenuLayout.addWidget(self.activities_btn)  
        # Storage button 
        self.storage_btn=QPushButton(QIcon('icons/storage.png'),"Storage",clicked=self.storage_page)
        self.storage_btn.setStyleSheet("text-align: left;") 
        self.storage_btn.setFlat(True)
        font_storageBtn=self.storage_btn.font()
        font_storageBtn.setPointSize(10)
        self.storage_btn.setFont(font_storageBtn)       
        self.leftMenuLayout.addWidget(self.storage_btn)  
        # Sensor button
        self.sensors_btn=QPushButton(QIcon('icons/sensor.png'),"Sensors",clicked=self.sensor_page)
        self.sensors_btn.setStyleSheet("text-align: left;") 
        self.sensors_btn.setFlat(True)
        font_sensorBtn=self.sensors_btn.font()
        font_sensorBtn.setPointSize(10)
        self.sensors_btn.setFont(font_sensorBtn)
        self.leftMenuLayout.addWidget(self.sensors_btn)  
        # Wifi button
        self.networks_btn=QPushButton(QIcon('icons/wifi.png'),"Networks",clicked=self.network_page) 
        self.networks_btn.setStyleSheet("text-align: left;")   
        self.networks_btn.setFlat(True)
        font_networkBtn=self.networks_btn.font()
        font_networkBtn.setPointSize(10)
        self.networks_btn.setFont(font_networkBtn)
        self.leftMenuLayout.addWidget(self.networks_btn)   
        
        self.middleLayout.addWidget(self.left_middle_widget,0, Qt.AlignLeft|Qt.AlignTop)

        #____________________________________    
        #________CENTER_CONTENTS_BODY________

        self.center_middle_widget=QWidget()
        sizePolicy_centerMiddle = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy_centerMiddle.setHorizontalStretch(0)
        sizePolicy_centerMiddle.setVerticalStretch(0)
        sizePolicy_centerMiddle.setHeightForWidth(self.center_middle_widget.sizePolicy().hasHeightForWidth())
        self.center_middle_widget.setSizePolicy(sizePolicy_centerMiddle)
        self.centerInfoLayout=QVBoxLayout(self.center_middle_widget)
        self.centerInfoLayout.setContentsMargins(0,0,0,0)
        self.centerInfoLayout.setSpacing(0)

        #Stacked Widget        
        self.stacked_widget = QStackedWidget()
        self.centerInfoLayout.addWidget(self.stacked_widget)
        # cpu page
        self.cpuPage=QWidget()
        cpuPageLayout=QVBoxLayout(self.cpuPage)
        top_widget=QWidget()
        cpuPageLayout.addWidget(top_widget)
        top_widgetLayout=QGridLayout()
        top_widget.setLayout(top_widgetLayout)
        
        systemInfo_label=QLabel("System Information")
        systeminfo_font=systemInfo_label.font()
        systeminfo_font.setBold(True)
        systeminfo_font.setPointSize(12)
        systemInfo_label.setFont(systeminfo_font)

        top_widgetLayout.addWidget(systemInfo_label, 0,0,1,1)
        top_widgetLayout.addWidget(QLabel("CPU Count"), 1,0,1,1,Qt.AlignLeft|Qt.AlignTop)
        top_widgetLayout.addWidget(QLabel("4"), 1,1,1,1,Qt.AlignLeft|Qt.AlignTop)
        top_widgetLayout.addWidget(QLabel("CPU Per"), 2,0,1,1,Qt.AlignLeft|Qt.AlignTop)
        top_widgetLayout.addWidget(QLabel("45.5%"), 2,1,1,1,Qt.AlignLeft|Qt.AlignTop)
        top_widgetLayout.addWidget(QLabel("CPU Main Core"), 3,0,1,1,Qt.AlignLeft|Qt.AlignTop)
        top_widgetLayout.addWidget(QLabel("2"), 3,1,1,1,Qt.AlignLeft|Qt.AlignTop)
       
        bottom_widget=QWidget()
        cpuPageLayout.addWidget(bottom_widget)
        bottom_widgetLayout=QGridLayout()
        bottom_widget.setLayout(bottom_widgetLayout)

        bottom_widgetLayout.addWidget(QLabel("Total Ram"), 0,0,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("7.6888 GB"), 0,1,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("Available RAM"), 1,0,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("4.3384 GB"), 1,1,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("Used RAM"), 2,0,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("2.3344 GB"), 2,1,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("Free RAM"), 3,0,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("1.6028 GB"), 3,1,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("RAM Usage"), 4,0,1,1,Qt.AlignLeft|Qt.AlignTop)
        bottom_widgetLayout.addWidget(QLabel("7.6888 GB"), 4,1,1,1,Qt.AlignLeft|Qt.AlignTop)


        # battery page
        self.batteryPage=QWidget()
        batteryPageLayout=QVBoxLayout(self.batteryPage)
        batteryPageLayout.addWidget(QLabel("BATTERY INFO"))
        # system information page
        self.syteminfoPage=QWidget()
        systemInfoPageLayout=QVBoxLayout(self.syteminfoPage)
        systemInfoPageLayout.addWidget(QLabel("SYSTEM INFO"))
        # activity page 
        self.activityPage=QWidget()
        activityPageLayout=QVBoxLayout(self.activityPage)
        activityPageLayout.addWidget(QLabel("ACTIVITIES"))
        # storage page
        self.storagePage=QWidget()
        storagePageLayout=QVBoxLayout(self.storagePage)
        storagePageLayout.addWidget(QLabel("STORAGE"))
        # sensors page
        self.sensorPage=QWidget()
        sensorPageLayout=QVBoxLayout(self.sensorPage)
        sensorPageLayout.addWidget(QLabel("SENSORS"))
        # networks page
        self.networkPage=QWidget()
        networkPageLayout=QVBoxLayout(self.networkPage)
        networkPageLayout.addWidget(QLabel("NETWORKS"))
                      
        self.stacked_widget.addWidget(self.cpuPage)
        self.stacked_widget.addWidget(self.batteryPage)
        self.stacked_widget.addWidget(self.syteminfoPage)
        self.stacked_widget.addWidget(self.activityPage)
        self.stacked_widget.addWidget(self.storagePage)
        self.stacked_widget.addWidget(self.sensorPage)
        self.stacked_widget.addWidget(self.networkPage)
        
        self.middleLayout.addWidget(self.center_middle_widget)
 
        #______________________________________
        #______RIGHT_DEVELOPER_DETAILS_________

        self.right_middle_widget=QWidget()
        self.rightMiddleLayout=QVBoxLayout(self.right_middle_widget)         
        self.about_label=QLabel("About")
        font_aboutLabel=self.menu_btn.font()
        font_aboutLabel.setBold(True)
        font_aboutLabel.setPointSize(10)
        self.about_label.setFont( font_aboutLabel)
        self.rightMiddleLayout.addWidget(self.about_label)
        self.description=QTextEdit("App Designed And Developed By Khamisi Kibet.")
        self.description.setMaximumSize(QSize(175, 50))
        self.rightMiddleLayout.addWidget(self.description)
        self.youtube_label=QLabel("Youtube/")
        self.rightMiddleLayout.addWidget(self.youtube_label)
        self.site_label=QLabel("Patreon/")
        self.rightMiddleLayout.addWidget(self.site_label)
        self.paypal_label=QLabel("PayPal")
        self.rightMiddleLayout.addWidget(self.paypal_label)
        self.middleLayout.addWidget(self.right_middle_widget,0, Qt.AlignRight|Qt.AlignTop)
        

        self.appLayout.addLayout(self.middleLayout)

#_____________________________________
#              FOOTER
#_____________________________________


        self.footer=QWidget()
        self.footerLayout=QHBoxLayout()
        self.footerLayout.setContentsMargins(5,9,0,9)
        self.footerLayout.setSpacing(0)
       
        #______________________________________
        #_________LEFT_VERSION_LABEL___________

        self.left_footer_widget=QWidget()
        self.leftFooterLayout=QVBoxLayout(self.left_footer_widget)
        self.version_label=QLabel("Version 1.0 | Copyright Spinn Co.")
        self.leftFooterLayout.addWidget(self.version_label)    
        self.footerLayout.addWidget(self.left_footer_widget,0, Qt.AlignLeft|Qt.AlignBottom)
        
        #_____________________________________
        #__________RIGHT_HELP_BUTTON__________

        self.right_footer_widget=QWidget()
        self.rightFooterLayout=QVBoxLayout(self.right_footer_widget)       
        self.help_btn=QPushButton("?")
        self.help_btn.setFlat(True)
        self.help_btn.setMaximumWidth(30)
        self.help_btn.setMaximumHeight(20)
        font_helpBtn = self.help_btn.font()
        font_helpBtn.setBold(True)
        self.help_btn.setFont(font_helpBtn)
        self.rightFooterLayout.addWidget(self.help_btn)
        self.footerLayout.addWidget(self.right_footer_widget,0,Qt.AlignRight|Qt.AlignBottom)
        
        self.appLayout.addLayout(self.footerLayout)

        self.windowLayout.addLayout(self.appLayout)


#SIGNALS

    def cpu_page(self):       
        self.stacked_widget.setCurrentIndex(0)

    def battery_page(self):       
        self.stacked_widget.setCurrentIndex(1)

    def systeminfo_page(self):       
        self.stacked_widget.setCurrentIndex(2)

    def activity_page(self):       
        self.stacked_widget.setCurrentIndex(3)  

    def storage_page(self):       
        self.stacked_widget.setCurrentIndex(4)      

    def sensor_page(self):       
        self.stacked_widget.setCurrentIndex(5)

    def network_page(self):       
        self.stacked_widget.setCurrentIndex(6)

def main():
    app = QApplication(sys.argv)
    w = psutilManager()
    w.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


