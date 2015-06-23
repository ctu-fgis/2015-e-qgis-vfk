# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import QFile, QIODevice, QUrl
from PyQt4.QtSql import QSqlDatabase


class vfkTextBrowser ():

    def __init__(self):
        pass

    def exportDocument(self, task, fileName, format):
        fileOut = QFile(fileName)

        if fileOut.open(QIODevice.WriteOnly | QIODevice.Text) is False:
            return False

        taskMap = {}


    def parseTask(self, task):
        task = QUrl(task)
        taskList = []
        taskList.append(task.encodedQueryItems())

        taskMap = {}
        taskMap['action'] = task.path()

        for i in taskList:
            taskMap['']