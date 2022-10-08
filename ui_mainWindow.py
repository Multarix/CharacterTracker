# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/mainWindow.ui'
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


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(571, 506)
        mainWindow.setMinimumSize(QtCore.QSize(1, 1))
        mainWindow.setMaximumSize(QtCore.QSize(1071, 533))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icons/icon.ico")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindow.setWindowIcon(icon)
        mainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.timeline = QtWidgets.QLabel(self.centralwidget)
        self.timeline.setGeometry(QtCore.QRect(526, 453, 31, 21))
        self.timeline.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"    font: 75 12pt \"Fira Code\";\n"
"    qproperty-alignment: AlignCenter;\n"
"}")
        self.timeline.setObjectName("timeline")
        self.timelineLabel = QtWidgets.QLabel(self.centralwidget)
        self.timelineLabel.setGeometry(QtCore.QRect(10, 448, 221, 31))
        self.timelineLabel.setMinimumSize(QtCore.QSize(221, 31))
        self.timelineLabel.setMaximumSize(QtCore.QSize(221, 31))
        self.timelineLabel.setObjectName("timelineLabel")
        self.timelineSlider = QtWidgets.QSlider(self.centralwidget)
        self.timelineSlider.setGeometry(QtCore.QRect(120, 452, 401, 22))
        self.timelineSlider.setMinimumSize(QtCore.QSize(0, 0))
        self.timelineSlider.setMinimum(0)
        self.timelineSlider.setMaximum(10)
        self.timelineSlider.setProperty("value", 0)
        self.timelineSlider.setSliderPosition(0)
        self.timelineSlider.setOrientation(QtCore.Qt.Horizontal)
        self.timelineSlider.setTickPosition(QtWidgets.QSlider.TicksBothSides)
        self.timelineSlider.setTickInterval(0)
        self.timelineSlider.setObjectName("timelineSlider")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-2, -22, 577, 498))
        self.tabWidget.setMinimumSize(QtCore.QSize(1, 1))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.charactersTab = QtWidgets.QWidget()
        self.charactersTab.setObjectName("charactersTab")
        self.addPerson = QtWidgets.QPushButton(self.charactersTab)
        self.addPerson.setGeometry(QtCore.QRect(10, 420, 61, 23))
        self.addPerson.setObjectName("addPerson")
        self.charactersLabel = QtWidgets.QLabel(self.charactersTab)
        self.charactersLabel.setGeometry(QtCore.QRect(10, 2, 221, 31))
        self.charactersLabel.setMinimumSize(QtCore.QSize(221, 31))
        self.charactersLabel.setMaximumSize(QtCore.QSize(221, 31))
        self.charactersLabel.setObjectName("charactersLabel")
        self.moveUp = QtWidgets.QPushButton(self.charactersTab)
        self.moveUp.setEnabled(False)
        self.moveUp.setGeometry(QtCore.QRect(229, 420, 30, 23))
        self.moveUp.setObjectName("moveUp")
        self.selectionDetails = QtWidgets.QListWidget(self.charactersTab)
        self.selectionDetails.setEnabled(True)
        self.selectionDetails.setGeometry(QtCore.QRect(300, 55, 261, 361))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectionDetails.sizePolicy().hasHeightForWidth())
        self.selectionDetails.setSizePolicy(sizePolicy)
        self.selectionDetails.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.selectionDetails.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.selectionDetails.setAutoScroll(False)
        self.selectionDetails.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.selectionDetails.setProperty("showDropIndicator", False)
        self.selectionDetails.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.selectionDetails.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.selectionDetails.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.selectionDetails.setProperty("isWrapping", False)
        self.selectionDetails.setWordWrap(True)
        self.selectionDetails.setObjectName("selectionDetails")
        self.characterList = QtWidgets.QListWidget(self.charactersTab)
        self.characterList.setGeometry(QtCore.QRect(10, 55, 281, 361))
        self.characterList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.characterList.setAutoScroll(True)
        self.characterList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.characterList.setProperty("showDropIndicator", True)
        self.characterList.setDragEnabled(False)
        self.characterList.setDragDropOverwriteMode(False)
        self.characterList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.characterList.setAlternatingRowColors(False)
        self.characterList.setIconSize(QtCore.QSize(11, 11))
        self.characterList.setUniformItemSizes(False)
        self.characterList.setObjectName("characterList")
        self.moveDown = QtWidgets.QPushButton(self.charactersTab)
        self.moveDown.setEnabled(False)
        self.moveDown.setGeometry(QtCore.QRect(261, 420, 30, 23))
        self.moveDown.setObjectName("moveDown")
        self.characterSearch = QtWidgets.QLineEdit(self.charactersTab)
        self.characterSearch.setGeometry(QtCore.QRect(10, 31, 281, 21))
        self.characterSearch.setAcceptDrops(False)
        self.characterSearch.setToolTip("")
        self.characterSearch.setObjectName("characterSearch")
        self.removePerson = QtWidgets.QPushButton(self.charactersTab)
        self.removePerson.setEnabled(False)
        self.removePerson.setGeometry(QtCore.QRect(150, 420, 61, 23))
        self.removePerson.setObjectName("removePerson")
        self.editPerson = QtWidgets.QPushButton(self.charactersTab)
        self.editPerson.setEnabled(False)
        self.editPerson.setGeometry(QtCore.QRect(80, 420, 61, 23))
        self.editPerson.setObjectName("editPerson")
        self.tabWidget.addTab(self.charactersTab, "")
        self.eventsTab = QtWidgets.QWidget()
        self.eventsTab.setObjectName("eventsTab")
        self.eventsLabel = QtWidgets.QLabel(self.eventsTab)
        self.eventsLabel.setGeometry(QtCore.QRect(10, 2, 300, 31))
        self.eventsLabel.setMinimumSize(QtCore.QSize(221, 31))
        self.eventsLabel.setMaximumSize(QtCore.QSize(300, 31))
        self.eventsLabel.setObjectName("eventsLabel")
        self.eventsList = QtWidgets.QListWidget(self.eventsTab)
        self.eventsList.setGeometry(QtCore.QRect(10, 55, 551, 361))
        self.eventsList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.eventsList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.eventsList.setAutoScroll(True)
        self.eventsList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.eventsList.setProperty("showDropIndicator", False)
        self.eventsList.setDragEnabled(False)
        self.eventsList.setDragDropOverwriteMode(False)
        self.eventsList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.eventsList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.eventsList.setAlternatingRowColors(False)
        self.eventsList.setIconSize(QtCore.QSize(11, 11))
        self.eventsList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.eventsList.setUniformItemSizes(False)
        self.eventsList.setWordWrap(True)
        self.eventsList.setObjectName("eventsList")
        self.eventsSearch = QtWidgets.QLineEdit(self.eventsTab)
        self.eventsSearch.setGeometry(QtCore.QRect(10, 31, 281, 21))
        self.eventsSearch.setAcceptDrops(False)
        self.eventsSearch.setToolTip("")
        self.eventsSearch.setObjectName("eventsSearch")
        self.eventsRemove = QtWidgets.QPushButton(self.eventsTab)
        self.eventsRemove.setEnabled(False)
        self.eventsRemove.setGeometry(QtCore.QRect(150, 420, 61, 23))
        self.eventsRemove.setObjectName("eventsRemove")
        self.eventsEdit = QtWidgets.QPushButton(self.eventsTab)
        self.eventsEdit.setEnabled(False)
        self.eventsEdit.setGeometry(QtCore.QRect(80, 420, 61, 23))
        self.eventsEdit.setObjectName("eventsEdit")
        self.eventsAdd = QtWidgets.QPushButton(self.eventsTab)
        self.eventsAdd.setGeometry(QtCore.QRect(10, 420, 61, 23))
        self.eventsAdd.setObjectName("eventsAdd")
        self.tabWidget.addTab(self.eventsTab, "")
        self.detailsTab = QtWidgets.QWidget()
        self.detailsTab.setObjectName("detailsTab")
        self.worldBuildingList = QtWidgets.QListWidget(self.detailsTab)
        self.worldBuildingList.setGeometry(QtCore.QRect(10, 55, 551, 361))
        self.worldBuildingList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.worldBuildingList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.worldBuildingList.setAutoScroll(True)
        self.worldBuildingList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.worldBuildingList.setProperty("showDropIndicator", False)
        self.worldBuildingList.setDragEnabled(False)
        self.worldBuildingList.setDragDropOverwriteMode(False)
        self.worldBuildingList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.worldBuildingList.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.worldBuildingList.setAlternatingRowColors(False)
        self.worldBuildingList.setIconSize(QtCore.QSize(11, 11))
        self.worldBuildingList.setVerticalScrollMode(QtWidgets.QAbstractItemView.ScrollPerPixel)
        self.worldBuildingList.setUniformItemSizes(False)
        self.worldBuildingList.setWordWrap(True)
        self.worldBuildingList.setObjectName("worldBuildingList")
        self.worldBuildingSearch = QtWidgets.QLineEdit(self.detailsTab)
        self.worldBuildingSearch.setGeometry(QtCore.QRect(10, 31, 281, 21))
        self.worldBuildingSearch.setAcceptDrops(False)
        self.worldBuildingSearch.setToolTip("")
        self.worldBuildingSearch.setObjectName("worldBuildingSearch")
        self.worldBuildingRemove = QtWidgets.QPushButton(self.detailsTab)
        self.worldBuildingRemove.setEnabled(False)
        self.worldBuildingRemove.setGeometry(QtCore.QRect(150, 420, 61, 23))
        self.worldBuildingRemove.setObjectName("worldBuildingRemove")
        self.worldBuildingLabel = QtWidgets.QLabel(self.detailsTab)
        self.worldBuildingLabel.setGeometry(QtCore.QRect(10, 2, 300, 31))
        self.worldBuildingLabel.setMinimumSize(QtCore.QSize(221, 31))
        self.worldBuildingLabel.setMaximumSize(QtCore.QSize(300, 31))
        self.worldBuildingLabel.setObjectName("worldBuildingLabel")
        self.worldBuildingEdit = QtWidgets.QPushButton(self.detailsTab)
        self.worldBuildingEdit.setEnabled(False)
        self.worldBuildingEdit.setGeometry(QtCore.QRect(80, 420, 61, 23))
        self.worldBuildingEdit.setObjectName("worldBuildingEdit")
        self.worldBuildingAdd = QtWidgets.QPushButton(self.detailsTab)
        self.worldBuildingAdd.setGeometry(QtCore.QRect(10, 420, 61, 23))
        self.worldBuildingAdd.setObjectName("worldBuildingAdd")
        self.tabWidget.addTab(self.detailsTab, "")
        self.tabWidget.raise_()
        self.timeline.raise_()
        self.timelineLabel.raise_()
        self.timelineSlider.raise_()
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 571, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuOptions")
        mainWindow.setMenuBar(self.menubar)
        self.action_New = QtWidgets.QAction(mainWindow)
        self.action_New.setObjectName("action_New")
        self.action_Open = QtWidgets.QAction(mainWindow)
        self.action_Open.setObjectName("action_Open")
        self.action_Save = QtWidgets.QAction(mainWindow)
        self.action_Save.setObjectName("action_Save")
        self.action_Save_As = QtWidgets.QAction(mainWindow)
        self.action_Save_As.setObjectName("action_Save_As")
        self.action_Exit = QtWidgets.QAction(mainWindow)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Add_Character = QtWidgets.QAction(mainWindow)
        self.action_Add_Character.setObjectName("action_Add_Character")
        self.action_Edit_Character = QtWidgets.QAction(mainWindow)
        self.action_Edit_Character.setEnabled(False)
        self.action_Edit_Character.setObjectName("action_Edit_Character")
        self.action_Remove_Character = QtWidgets.QAction(mainWindow)
        self.action_Remove_Character.setEnabled(False)
        self.action_Remove_Character.setObjectName("action_Remove_Character")
        self.action_Refresh = QtWidgets.QAction(mainWindow)
        self.action_Refresh.setObjectName("action_Refresh")
        self.action_Credits = QtWidgets.QAction(mainWindow)
        self.action_Credits.setObjectName("action_Credits")
        self.action_Settings = QtWidgets.QAction(mainWindow)
        self.action_Settings.setObjectName("action_Settings")
        self.menuFile.addAction(self.action_New)
        self.menuFile.addAction(self.action_Open)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Save)
        self.menuFile.addAction(self.action_Save_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.action_Exit)
        self.menuEdit.addAction(self.action_Add_Character)
        self.menuEdit.addAction(self.action_Edit_Character)
        self.menuEdit.addAction(self.action_Remove_Character)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_Refresh)
        self.menuOptions.addAction(self.action_Credits)
        self.menuOptions.addSeparator()
        self.menuOptions.addAction(self.action_Settings)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.charactersLabel.setBuddy(self.characterList)
        self.eventsLabel.setBuddy(self.eventsList)
        self.worldBuildingLabel.setBuddy(self.worldBuildingList)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.timelineSlider.valueChanged['int'].connect(self.timeline.setNum) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "MainWindow"))
        self.timeline.setText(_translate("mainWindow", "<html><head/><body><p>0</p></body></html>"))
        self.timelineLabel.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Timeline</span></p></body></html>"))
        self.addPerson.setText(_translate("mainWindow", "Add..."))
        self.charactersLabel.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Characters</span></p></body></html>"))
        self.moveUp.setText(_translate("mainWindow", "▲"))
        self.characterList.setSortingEnabled(False)
        self.moveDown.setText(_translate("mainWindow", "▼"))
        self.characterSearch.setPlaceholderText(_translate("mainWindow", "Search Characters"))
        self.removePerson.setText(_translate("mainWindow", "Remove"))
        self.editPerson.setText(_translate("mainWindow", "Edit..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.charactersTab), _translate("mainWindow", "Characters"))
        self.eventsLabel.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Lore/ Events</span></p></body></html>"))
        self.eventsList.setSortingEnabled(False)
        self.eventsSearch.setPlaceholderText(_translate("mainWindow", "Search Events"))
        self.eventsRemove.setText(_translate("mainWindow", "Remove"))
        self.eventsEdit.setText(_translate("mainWindow", "Edit..."))
        self.eventsAdd.setText(_translate("mainWindow", "Add..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.eventsTab), _translate("mainWindow", "Events"))
        self.worldBuildingList.setSortingEnabled(False)
        self.worldBuildingSearch.setPlaceholderText(_translate("mainWindow", "Search Notes"))
        self.worldBuildingRemove.setText(_translate("mainWindow", "Remove"))
        self.worldBuildingLabel.setText(_translate("mainWindow", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">World Details</span></p></body></html>"))
        self.worldBuildingEdit.setText(_translate("mainWindow", "Edit..."))
        self.worldBuildingAdd.setText(_translate("mainWindow", "Add..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.detailsTab), _translate("mainWindow", "World Building"))
        self.menuFile.setTitle(_translate("mainWindow", "File"))
        self.menuEdit.setTitle(_translate("mainWindow", "Edit"))
        self.menuOptions.setTitle(_translate("mainWindow", "&Options"))
        self.action_New.setText(_translate("mainWindow", "New..."))
        self.action_New.setShortcut(_translate("mainWindow", "Ctrl+N"))
        self.action_Open.setText(_translate("mainWindow", "Open..."))
        self.action_Open.setShortcut(_translate("mainWindow", "Ctrl+O"))
        self.action_Save.setText(_translate("mainWindow", "Save"))
        self.action_Save.setShortcut(_translate("mainWindow", "Ctrl+S"))
        self.action_Save_As.setText(_translate("mainWindow", "Save As..."))
        self.action_Save_As.setShortcut(_translate("mainWindow", "Ctrl+Shift+S"))
        self.action_Exit.setText(_translate("mainWindow", "Exit"))
        self.action_Add_Character.setText(_translate("mainWindow", "&Add Character..."))
        self.action_Add_Character.setShortcut(_translate("mainWindow", "Alt+A"))
        self.action_Edit_Character.setText(_translate("mainWindow", "&Edit Character"))
        self.action_Edit_Character.setShortcut(_translate("mainWindow", "Alt+E"))
        self.action_Remove_Character.setText(_translate("mainWindow", "&Remove Character"))
        self.action_Refresh.setText(_translate("mainWindow", "Refresh"))
        self.action_Refresh.setShortcut(_translate("mainWindow", "F5"))
        self.action_Credits.setText(_translate("mainWindow", "&Credits"))
        self.action_Settings.setText(_translate("mainWindow", "&Settings..."))
