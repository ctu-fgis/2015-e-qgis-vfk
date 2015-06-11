# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'vfkPlugin_dialog.ui'
#
# Created: Thu May 14 18:30:38 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_vfkDialogBase(object):
    def setupUi(self, vfkDialogBase):
        vfkDialogBase.setObjectName(_fromUtf8("vfkDialogBase"))
        vfkDialogBase.resize(414, 306)

        self.retranslateUi(vfkDialogBase)
        QtCore.QMetaObject.connectSlotsByName(vfkDialogBase)

    def retranslateUi(self, vfkDialogBase):
        vfkDialogBase.setWindowTitle(_translate("vfkDialogBase", "Vfk Plugin", None))

