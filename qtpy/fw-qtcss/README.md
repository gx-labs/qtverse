# Stylesheet Framework

A library of css stylesheets for ready to use in Qt applications.

## Project Goals
This project was created with a goal to have a custom lib of
stylesheets which can be used intuitively in a Qt application.

## Quick Start | Getting Started

Intended use of the framework

``` python
StyleSheetFramework().load('widgetPreset')
StyleSheetFramework().load('theme')
```


example: To Load a custom widget preset
``` python
from sytlesheet_framework import StyleSheetFramework

widget_stylesheet = StyleSheetFramework().load('QSlider.purple_horizonal')
self.setStyleSheet(widget_stylesheet)

```

example: To Load a custom Theme
``` python
mars_stylesheet = StyleSheetFramework(theme="mars")
self.setStyleSheet(mars_stylesheet)
```



