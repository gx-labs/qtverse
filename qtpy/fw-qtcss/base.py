
import os

fileDir = os.path.dirname(os.path.abspath(__file__))

class StyleSheetFramework(object):
    def __init__(self, theme="default"):
        self._theme = theme

    def load(self, sheet_name):
        print ("load") , self._theme, sheet_name
        get_sheet_file = fileDir + os.sep + "presets" + os.sep  + self._theme + os.sep + sheet_name.split('.')[0] + os.sep + sheet_name.split('.')[1] + ".stylesheet"
        # get_sheet_file_path = os.path.join(fileDir , "themes" , self._theme , sheet_name)
        print(get_sheet_file)
        print(os.path.isfile(get_sheet_file))
        with open(get_sheet_file , 'r') as f:
            data = f.read()
        return data

if __name__ == '__main__':
    default_sheet = StyleSheetFramework()
    
    custom_stylesheet = StyleSheetFramework().load('QSlider.purple_horizonal')
    print(custom_stylesheet)

    # mars_sheet = StyleSheetFramework(theme="mars")







