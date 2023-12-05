
PySide2 on windows for python 2.7 is not available



## Custom Widgets
- when defining a class of custom widgets , only QtWidgets.QtWidget is accepted as object for the class
    ```
    class CustomWidget(QtWidgets.QWidget):
        def __init__ (self, parent = None):
            super(CustomWidget, self).__init__(parent)
    ```

## QPixmap
- this still uses QtGui module in Qt.py
    ```QtGui.QPixmap(imagePath)```







