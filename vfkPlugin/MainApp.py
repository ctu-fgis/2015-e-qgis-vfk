# -*- coding: utf-8 -*-
"""
/***************************************************************************
 vfkPluginDialog
                                 A QGIS plugin
 Plugin umoznujici praci s daty katastru nemovitosti
                             -------------------
        begin                : 2015-06-11
        git sha              : $Format:%H$
        copyright            : (C) 2015 by Stepan Bambula, Adam Dlesk, Jaroslav Urik
        email                : stepan.bambula@fsv.cvut.cz, adam.dlesk@fsv.cvut.cz, jaroslav.urik@fsv.cvut.cz
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

# Import the PyQt, QGIS libraries and classes
import os
#import subprocess
from PyQt4 import QtCore, QtGui
from ui_MainApp import Ui_MainApp


class MainApp (QtGui.QMainWindow):
    def __init__(self, iface, parent=None):
        QtGui.QMainWindow.__init__(self)
        self.iface = iface

        # Set up the user interface from Designer.
        self.ui = Ui_MainApp()
        self.ui.setupUi(self)