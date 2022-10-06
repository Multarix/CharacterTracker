# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/worldBuilding.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets

def resource_path(relative_path):
	""" Get absolute path to resource, works for dev and for PyInstaller """
	base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)));
	return os.path.join(base_path, relative_path);


class Ui_worldBuildingWindow(object):
    def setupUi(self, worldBuildingWindow):
        worldBuildingWindow.setObjectName("worldBuildingWindow")
        worldBuildingWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        worldBuildingWindow.resize(511, 281)
        worldBuildingWindow.setMinimumSize(QtCore.QSize(511, 281))
        worldBuildingWindow.setMaximumSize(QtCore.QSize(511, 281))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        worldBuildingWindow.setWindowIcon(icon)
        self.worldBuildingLabel = QtWidgets.QLabel(worldBuildingWindow)
        self.worldBuildingLabel.setGeometry(QtCore.QRect(10, 5, 151, 31))
        self.worldBuildingLabel.setObjectName("worldBuildingLabel")
        self.accept = QtWidgets.QPushButton(worldBuildingWindow)
        self.accept.setEnabled(False)
        self.accept.setGeometry(QtCore.QRect(350, 10, 71, 23))
        self.accept.setObjectName("accept")
        self.cancel = QtWidgets.QPushButton(worldBuildingWindow)
        self.cancel.setGeometry(QtCore.QRect(430, 10, 71, 23))
        self.cancel.setObjectName("cancel")
        self.textEditor = QtWidgets.QTextEdit(worldBuildingWindow)
        self.textEditor.setGeometry(QtCore.QRect(10, 40, 491, 231))
        self.textEditor.setAcceptDrops(False)
        self.textEditor.setObjectName("textEditor")
        self.addToTimeline = QtWidgets.QCheckBox(worldBuildingWindow)
        self.addToTimeline.setGeometry(QtCore.QRect(160, 10, 91, 23))
        self.addToTimeline.setObjectName("addToTimeline")
        self.yearOfEvent = QtWidgets.QSpinBox(worldBuildingWindow)
        self.yearOfEvent.setEnabled(False)
        self.yearOfEvent.setGeometry(QtCore.QRect(260, 10, 81, 23))
        self.yearOfEvent.setObjectName("yearOfEvent")
        self.worldBuildingLabel.setBuddy(self.textEditor)

        self.retranslateUi(worldBuildingWindow)
        self.cancel.clicked.connect(worldBuildingWindow.close) # type: ignore
        self.addToTimeline.toggled['bool'].connect(self.yearOfEvent.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(worldBuildingWindow)

    def retranslateUi(self, worldBuildingWindow):
        _translate = QtCore.QCoreApplication.translate
        worldBuildingWindow.setWindowTitle(_translate("worldBuildingWindow", "Add Detail"))
        self.worldBuildingLabel.setText(_translate("worldBuildingWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Add Detail</span></p></body></html>"))
        self.accept.setText(_translate("worldBuildingWindow", "Accept"))
        self.cancel.setText(_translate("worldBuildingWindow", "Cancel"))
        self.textEditor.setHtml(_translate("worldBuildingWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textEditor.setPlaceholderText(_translate("worldBuildingWindow", "Type here..."))
        self.addToTimeline.setText(_translate("worldBuildingWindow", "Add to Timeline"))
        self.yearOfEvent.setPrefix(_translate("worldBuildingWindow", "Year "))
