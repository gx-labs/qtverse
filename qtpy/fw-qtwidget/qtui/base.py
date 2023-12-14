#!/usr/bin/env python
# coding=utf-8
# -*- coding: utf-8 -*-

from Qt import QtCompat, QtWidgets, QtCore

def directory_view(path):
    pass

def add_custom_widget_to_list_widget(custom_widget, list_widget):
    """
    Adds the given widget to the list widget

    :param custom_widget:
    :param list_widget:
    :return:
    """

    # Create QListWidgetItem
    list_widget_item = QtWidgets.QListWidgetItem(list_widget)

    # Set size hint
    list_widget_item.setSizeHint(custom_widget.sizeHint())

    # Add QListWidgetItem into QListWidget
    list_widget.addItem(list_widget_item)
    list_widget.setItemWidget(list_widget_item, custom_widget)





