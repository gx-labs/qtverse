import sys
from PySide2.QtWidgets import QApplication, QMainWindow, QScrollBar
from PySide2.QtCore import Qt

app = QApplication(sys.argv)

# Create a QMainWindow
main_window = QMainWindow()

# Create a horizontal scrollbar
horizontal_scrollbar = QScrollBar(Qt.Horizontal)
main_window.setCentralWidget(horizontal_scrollbar)

# Define the stylesheet with animation
style = """
/* HORIZONTAL SCROLLBAR */
QScrollBar:horizontal {
    border: none;
    background: rgb(45, 45, 68);
    height: 14px;
    margin: 0 15px 0 15px;
    border-radius: 0px;
}

/* HANDLE BAR HORIZONTAL */
QScrollBar::handle:horizontal {
    background-color: rgb(80, 80, 122);
    min-width: 30px;
    border-radius: 7px;
    animation: pulsate 2s infinite alternate; /* Pulsating animation */
}

@keyframes pulsate {
    0% {
        background-color: rgb(80, 80, 122);
    }
    100% {
        background-color: rgb(255, 0, 127);
    }
}

/* BTN LEFT - SCROLLBAR */
QScrollBar::sub-line:horizontal {
    border: none;
    background-color: rgb(59, 59, 90);
    width: 15px;
    border-top-left-radius: 7px;
    border-bottom-left-radius: 7px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}
QScrollBar::sub-line:horizontal:hover {
    background-color: rgb(255, 0, 127);
}
QScrollBar::sub-line:horizontal:pressed {
    background-color: rgb(185, 0, 92);
}

/* BTN RIGHT - SCROLLBAR */
QScrollBar::add-line:horizontal {
    border: none;
    background-color: rgb(59, 59, 90);
    width: 15px;
    border-top-right-radius: 7px;
    border-bottom-right-radius: 7px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}
QScrollBar::add-line:horizontal:hover {
    background-color: rgb(255, 0, 127);
}
QScrollBar::add-line:horizontal:pressed {
    background-color: rgb(185, 0, 92);
}

/* RESET ARROW */
QScrollBar::left-arrow:horizontal, QScrollBar::right-arrow:horizontal {
    background: none;
}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: none;
}
"""

horizontal_scrollbar.setStyleSheet(style)

# Show the main window
main_window.show()

# Start the application event loop
sys.exit(app.exec_())
