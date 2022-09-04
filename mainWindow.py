# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/main.ui'
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


class Ui_mainWindowUI(object):
    def setupUi(self, mainWindowUI):
        mainWindowUI.setObjectName("mainWindowUI")
        mainWindowUI.resize(479, 361)
        mainWindowUI.setMinimumSize(QtCore.QSize(479, 361))
        mainWindowUI.setMaximumSize(QtCore.QSize(479, 361))
        mainWindowUI.setWindowTitle("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(resource_path("icons/icon.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mainWindowUI.setWindowIcon(icon)
        mainWindowUI.setStyleSheet("background: rgb(54, 57, 63);\n"
"color: rgb(255, 255, 255);")
        mainWindowUI.setIconSize(QtCore.QSize(48, 48))
        self.centralwidget = QtWidgets.QWidget(mainWindowUI)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(-3, -22, 491, 391))
        self.tabWidget.setMinimumSize(QtCore.QSize(491, 0))
        self.tabWidget.setStyleSheet("QTabWidget {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabWidget::tab-bar {\n"
"    left: 305px;\n"
"    top: 62px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    background: rgb(64, 68, 75);\n"
"}\n"
"\n"
"QTabBar::tab:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QTabBar::tab:selected {\n"
"    background: rgb(89, 93, 99);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.tabWidget.setObjectName("tabWidget")
        self.Characters = QtWidgets.QWidget()
        self.Characters.setStyleSheet("")
        self.Characters.setObjectName("Characters")
        self.removePerson = QtWidgets.QPushButton(self.Characters)
        self.removePerson.setEnabled(False)
        self.removePerson.setGeometry(QtCore.QRect(150, 310, 61, 23))
        self.removePerson.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.removePerson.setObjectName("removePerson")
        self.editPerson = QtWidgets.QPushButton(self.Characters)
        self.editPerson.setEnabled(False)
        self.editPerson.setGeometry(QtCore.QRect(80, 310, 61, 23))
        self.editPerson.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.editPerson.setObjectName("editPerson")
        self.charactersLabel = QtWidgets.QLabel(self.Characters)
        self.charactersLabel.setGeometry(QtCore.QRect(10, 5, 161, 31))
        self.charactersLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"    font: font \"Fira Code\";\n"
"}")
        self.charactersLabel.setObjectName("charactersLabel")
        self.characterList = QtWidgets.QListWidget(self.Characters)
        self.characterList.setGeometry(QtCore.QRect(10, 70, 221, 231))
        self.characterList.setStyleSheet("QListWidget{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListWidget:item{\n"
"    color: rgb(255, 255, 255);\n"
"    padding: 3px;\n"
"    border: 1px solid transparent;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget:item:hover{\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    background: rgb(74, 76, 79);\n"
"    border: 1px solid rgb(64, 66, 75);\n"
"}\n"
"\n"
"QListWidget:item:selected{\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    background: rgb(93, 94, 97);\n"
"    border: 1px solid rgb(74, 76, 79);\n"
"}")
        self.characterList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.characterList.setAutoScroll(True)
        self.characterList.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.characterList.setProperty("showDropIndicator", True)
        self.characterList.setDragEnabled(False)
        self.characterList.setDragDropOverwriteMode(False)
        self.characterList.setDragDropMode(QtWidgets.QAbstractItemView.NoDragDrop)
        self.characterList.setAlternatingRowColors(False)
        self.characterList.setIconSize(QtCore.QSize(11, 11))
        self.characterList.setUniformItemSizes(True)
        self.characterList.setObjectName("characterList")
        self.characterSearch = QtWidgets.QLineEdit(self.Characters)
        self.characterSearch.setGeometry(QtCore.QRect(10, 40, 221, 21))
        self.characterSearch.setAcceptDrops(False)
        self.characterSearch.setToolTip("")
        self.characterSearch.setStyleSheet("QLineEdit{\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"}")
        self.characterSearch.setObjectName("characterSearch")
        self.selectionDetails = QtWidgets.QListWidget(self.Characters)
        self.selectionDetails.setEnabled(True)
        self.selectionDetails.setGeometry(QtCore.QRect(240, 70, 231, 231))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectionDetails.sizePolicy().hasHeightForWidth())
        self.selectionDetails.setSizePolicy(sizePolicy)
        self.selectionDetails.setStyleSheet("QListWidget{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListWidget:item{\n"
"    padding: 3px;\n"
"    background: rgb(64, 68, 75);\n"
"}")
        self.selectionDetails.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.selectionDetails.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.selectionDetails.setAutoScroll(False)
        self.selectionDetails.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.selectionDetails.setProperty("showDropIndicator", False)
        self.selectionDetails.setDefaultDropAction(QtCore.Qt.IgnoreAction)
        self.selectionDetails.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.selectionDetails.setProperty("isWrapping", False)
        self.selectionDetails.setWordWrap(True)
        self.selectionDetails.setObjectName("selectionDetails")
        self.addPerson = QtWidgets.QPushButton(self.Characters)
        self.addPerson.setGeometry(QtCore.QRect(10, 310, 61, 23))
        self.addPerson.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.addPerson.setObjectName("addPerson")
        self.moveUp = QtWidgets.QPushButton(self.Characters)
        self.moveUp.setEnabled(False)
        self.moveUp.setGeometry(QtCore.QRect(240, 310, 31, 23))
        self.moveUp.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.moveUp.setObjectName("moveUp")
        self.moveDown = QtWidgets.QPushButton(self.Characters)
        self.moveDown.setEnabled(False)
        self.moveDown.setGeometry(QtCore.QRect(270, 310, 31, 23))
        self.moveDown.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.moveDown.setObjectName("moveDown")
        self.tabWidget.addTab(self.Characters, "")
        self.WorldBuilding = QtWidgets.QWidget()
        self.WorldBuilding.setObjectName("WorldBuilding")
        self.worldBuildingAdd = QtWidgets.QPushButton(self.WorldBuilding)
        self.worldBuildingAdd.setGeometry(QtCore.QRect(10, 310, 61, 23))
        self.worldBuildingAdd.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.worldBuildingAdd.setObjectName("worldBuildingAdd")
        self.worldBuildingEdit = QtWidgets.QPushButton(self.WorldBuilding)
        self.worldBuildingEdit.setEnabled(False)
        self.worldBuildingEdit.setGeometry(QtCore.QRect(90, 310, 61, 23))
        self.worldBuildingEdit.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.worldBuildingEdit.setObjectName("worldBuildingEdit")
        self.worldBuildingRemove = QtWidgets.QPushButton(self.WorldBuilding)
        self.worldBuildingRemove.setEnabled(False)
        self.worldBuildingRemove.setGeometry(QtCore.QRect(170, 310, 61, 23))
        self.worldBuildingRemove.setStyleSheet("QPushButton {\n"
"    background: rgb(64, 68, 75);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: rgb(79, 83, 89);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background: rgb(54, 57, 63);\n"
"    color: rgb(126, 126, 126);\n"
"}")
        self.worldBuildingRemove.setObjectName("worldBuildingRemove")
        self.worldBuildingSearch = QtWidgets.QLineEdit(self.WorldBuilding)
        self.worldBuildingSearch.setGeometry(QtCore.QRect(10, 40, 221, 21))
        self.worldBuildingSearch.setAcceptDrops(False)
        self.worldBuildingSearch.setToolTip("")
        self.worldBuildingSearch.setStyleSheet("QLineEdit{\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"}")
        self.worldBuildingSearch.setObjectName("worldBuildingSearch")
        self.worldBuildingLabel = QtWidgets.QLabel(self.WorldBuilding)
        self.worldBuildingLabel.setGeometry(QtCore.QRect(10, 5, 221, 31))
        self.worldBuildingLabel.setStyleSheet("QLabel {\n"
"    background: transparent;\n"
"    font: font \"Fira Code\";\n"
"}")
        self.worldBuildingLabel.setObjectName("worldBuildingLabel")
        self.worldBuildingList = QtWidgets.QListWidget(self.WorldBuilding)
        self.worldBuildingList.setGeometry(QtCore.QRect(10, 70, 461, 231))
        self.worldBuildingList.setStyleSheet("QListWidget{\n"
"    color: rgb(255, 255, 255);\n"
"    background: rgb(64, 68, 75);\n"
"    border: 1px solid rgb(50, 50, 50);\n"
"    border-radius:5px;\n"
"    outline: 0;\n"
"}\n"
"\n"
"QListWidget:item{\n"
"    color: rgb(255, 255, 255);\n"
"    padding-left: 3px;\n"
"    padding-right: 3px;\n"
"    border: 1px solid transparent;\n"
"    padding-top: 5px;\n"
"    padding-bottom: 5px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QListWidget:item:hover{\n"
"    background: rgb(74, 76, 79);\n"
"    border: 1px solid rgb(64, 66, 75);\n"
"}\n"
"\n"
"QListWidget:item:selected{\n"
"    background: rgb(93, 94, 97);\n"
"    border: 1px solid rgb(74, 76, 79);\n"
"}")
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
        self.worldBuildingList.setUniformItemSizes(False)
        self.worldBuildingList.setWordWrap(True)
        self.worldBuildingList.setObjectName("worldBuildingList")
        self.tabWidget.addTab(self.WorldBuilding, "")
        mainWindowUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindowUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 479, 21))
        self.menubar.setStyleSheet("QMenuBar {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenuBar::item {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenuBar::item:selected {\n"
"    background: rgb(64, 68, 74);\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.menubar.setNativeMenuBar(True)
        self.menubar.setObjectName("menubar")
        self.menu_File = QtWidgets.QMenu(self.menubar)
        self.menu_File.setStyleSheet("QMenu {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background: rgb(64, 68, 74);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item:disabled {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(126, 126, 126);\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    color: rgb(0, 0, 0);\n"
"    padding-top: 4px;\n"
"}")
        self.menu_File.setObjectName("menu_File")
        self.menu_Options = QtWidgets.QMenu(self.menubar)
        self.menu_Options.setStyleSheet("QMenu {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background: rgb(64, 68, 74);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item:disabled {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(126, 126, 126);\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    color: rgb(0, 0, 0);\n"
"    padding-top: 4px;\n"
"}")
        self.menu_Options.setObjectName("menu_Options")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("QMenu {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item:selected {\n"
"    background: rgb(64, 68, 74);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QMenu::item:disabled {\n"
"    background: rgb(41, 43, 47);\n"
"    color: rgb(126, 126, 126);\n"
"}\n"
"\n"
"QMenu::separator {\n"
"    color: rgb(0, 0, 0);\n"
"    padding-top: 4px;\n"
"}")
        self.menuHelp.setObjectName("menuHelp")
        mainWindowUI.setMenuBar(self.menubar)
        self.action_Open = QtWidgets.QAction(mainWindowUI)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(resource_path("icons/open_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Open.setIcon(icon1)
        self.action_Open.setObjectName("action_Open")
        self.action_Exit = QtWidgets.QAction(mainWindowUI)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(resource_path("icons/cancel_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Exit.setIcon(icon2)
        self.action_Exit.setObjectName("action_Exit")
        self.action_Save = QtWidgets.QAction(mainWindowUI)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(resource_path("icons/save_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Save.setIcon(icon3)
        self.action_Save.setObjectName("action_Save")
        self.action_config = QtWidgets.QAction(mainWindowUI)
        self.action_config.setEnabled(False)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(resource_path("icons/settings_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_config.setIcon(icon4)
        self.action_config.setObjectName("action_config")
        self.actionSave_As = QtWidgets.QAction(mainWindowUI)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(resource_path("icons/saveAs_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSave_As.setIcon(icon5)
        self.actionSave_As.setObjectName("actionSave_As")
        self.action_New = QtWidgets.QAction(mainWindowUI)
        self.action_New.setEnabled(False)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(resource_path("icons/new_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_New.setIcon(icon6)
        self.action_New.setObjectName("action_New")
        self.action_Credits = QtWidgets.QAction(mainWindowUI)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(resource_path("icons/about_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.action_Credits.setIcon(icon7)
        self.action_Credits.setObjectName("action_Credits")
        self.actionAdd_Character = QtWidgets.QAction(mainWindowUI)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(resource_path("icons/addPerson_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd_Character.setIcon(icon8)
        self.actionAdd_Character.setObjectName("actionAdd_Character")
        self.actionRefresh = QtWidgets.QAction(mainWindowUI)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(resource_path("icons/refresh_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRefresh.setIcon(icon9)
        self.actionRefresh.setObjectName("actionRefresh")
        self.actionEdit_Character = QtWidgets.QAction(mainWindowUI)
        self.actionEdit_Character.setEnabled(False)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(resource_path("icons/editCharacter_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit_Character.setIcon(icon10)
        self.actionEdit_Character.setObjectName("actionEdit_Character")
        self.actionRemove_Character = QtWidgets.QAction(mainWindowUI)
        self.actionRemove_Character.setEnabled(False)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(resource_path("icons/removeCharacter_Dark.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRemove_Character.setIcon(icon11)
        self.actionRemove_Character.setObjectName("actionRemove_Character")
        self.menu_File.addAction(self.action_New)
        self.menu_File.addAction(self.action_Open)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Save)
        self.menu_File.addAction(self.actionSave_As)
        self.menu_File.addSeparator()
        self.menu_File.addAction(self.action_Exit)
        self.menu_Options.addAction(self.actionAdd_Character)
        self.menu_Options.addAction(self.actionEdit_Character)
        self.menu_Options.addAction(self.actionRemove_Character)
        self.menu_Options.addSeparator()
        self.menu_Options.addAction(self.actionRefresh)
        self.menu_Options.addSeparator()
        self.menu_Options.addAction(self.action_config)
        self.menuHelp.addAction(self.action_Credits)
        self.menubar.addAction(self.menu_File.menuAction())
        self.menubar.addAction(self.menu_Options.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.charactersLabel.setBuddy(self.characterList)
        self.worldBuildingLabel.setBuddy(self.characterList)

        self.retranslateUi(mainWindowUI)
        self.tabWidget.setCurrentIndex(0)
        self.selectionDetails.currentRowChanged['int'].connect(self.selectionDetails.clearSelection) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(mainWindowUI)
        mainWindowUI.setTabOrder(self.characterSearch, self.addPerson)
        mainWindowUI.setTabOrder(self.addPerson, self.editPerson)
        mainWindowUI.setTabOrder(self.editPerson, self.removePerson)
        mainWindowUI.setTabOrder(self.removePerson, self.characterList)
        mainWindowUI.setTabOrder(self.characterList, self.selectionDetails)

    def retranslateUi(self, mainWindowUI):
        _translate = QtCore.QCoreApplication.translate
        self.removePerson.setText(_translate("mainWindowUI", "Remove"))
        self.editPerson.setText(_translate("mainWindowUI", "Edit..."))
        self.charactersLabel.setText(_translate("mainWindowUI", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">Characters</span></p></body></html>"))
        self.characterList.setSortingEnabled(False)
        self.characterSearch.setPlaceholderText(_translate("mainWindowUI", "Search Characters"))
        self.addPerson.setText(_translate("mainWindowUI", "Add..."))
        self.moveUp.setText(_translate("mainWindowUI", "▲"))
        self.moveDown.setText(_translate("mainWindowUI", "▼"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Characters), _translate("mainWindowUI", "Characters"))
        self.worldBuildingAdd.setText(_translate("mainWindowUI", "Add..."))
        self.worldBuildingEdit.setText(_translate("mainWindowUI", "Edit..."))
        self.worldBuildingRemove.setText(_translate("mainWindowUI", "Remove"))
        self.worldBuildingSearch.setPlaceholderText(_translate("mainWindowUI", "Search Notes"))
        self.worldBuildingLabel.setText(_translate("mainWindowUI", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:600;\">World Building</span></p></body></html>"))
        self.worldBuildingList.setSortingEnabled(False)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.WorldBuilding), _translate("mainWindowUI", "World Building"))
        self.menu_File.setTitle(_translate("mainWindowUI", "&File"))
        self.menu_Options.setTitle(_translate("mainWindowUI", "&Edit"))
        self.menuHelp.setTitle(_translate("mainWindowUI", "&Help"))
        self.action_Open.setText(_translate("mainWindowUI", "&Open..."))
        self.action_Open.setShortcut(_translate("mainWindowUI", "Ctrl+O"))
        self.action_Exit.setText(_translate("mainWindowUI", "&Exit"))
        self.action_Save.setText(_translate("mainWindowUI", "&Save"))
        self.action_Save.setShortcut(_translate("mainWindowUI", "Ctrl+S"))
        self.action_config.setText(_translate("mainWindowUI", "&Settings"))
        self.actionSave_As.setText(_translate("mainWindowUI", "Save &As"))
        self.actionSave_As.setShortcut(_translate("mainWindowUI", "Ctrl+Shift+S"))
        self.action_New.setText(_translate("mainWindowUI", "&New..."))
        self.action_New.setShortcut(_translate("mainWindowUI", "Ctrl+N"))
        self.action_Credits.setText(_translate("mainWindowUI", "&Information"))
        self.actionAdd_Character.setText(_translate("mainWindowUI", "&Add Character..."))
        self.actionRefresh.setText(_translate("mainWindowUI", "&Refresh"))
        self.actionRefresh.setShortcut(_translate("mainWindowUI", "Ctrl+R"))
        self.actionEdit_Character.setText(_translate("mainWindowUI", "&Edit Character..."))
        self.actionRemove_Character.setText(_translate("mainWindowUI", "Remove Character"))
