# type: ignore
from __future__ import annotations
from typing import TypedDict
from typing import Tuple

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *

from ui_mainWindow import Ui_mainWindow as mainWindow
from ui_editPersonWindow import Ui_editPersonWindow as editPersonWindow
from ui_addRelationWindow import Ui_addRelationWindow as addRelationWindow
from ui_worldBuildingWindow import Ui_worldBuildingWindow as worldBuildingWindow
from ui_optionsWindow import Ui_optionsWindow as optionsWindow
from ui_infoWindow import Ui_creditsWindow as creditsWindow

characterRelations = Tuple[int, int]
character = Tuple[int, str, str, int, int, int, str, int, str, str]
worldItem = Tuple[str, int]
eventItem = Tuple[int, int, int, str, str]

class settingsLayout(TypedDict):
	timelineLength: int;
	monthsPerYear: int;
	startYear: int;

class dataLayout(TypedDict):
	"""Character, world, events and settings layout"""
	characters: list[character];
	world: list[worldItem];
	events: list[eventItem];
	settings: settingsLayout;


class fixesLayout(TypedDict):
	font: QtGui.QFont;
	palette: QtGui.QPalette


class configLayout(TypedDict):
	"""Config settings layout"""
	theme: int;
	lang: int;
	longestRelation: int;
	
	
class miscFunctions():
	def __init__(self) -> None:
		pass
	
	def resource_path(self, relative_path: str) -> str:
		pass
	
	def showDetails(this) -> None:
		pass
	
	def searchBar(this, searchBar: QLineEdit, listToSearch: QListWidget) -> None:
		pass
	
	def unlockWorldBuildingEditRemoveBtns(this) -> None:
		pass
	
	def unlockWorldBuildingAcceptBtn(this):
		pass
	
	def unlockEditRemoveCharacterBtns(this) -> None:
		pass
	
	def unlockSubmitCharacterBtn(this) -> None:
		pass
	
	def unlockEditRemoveRelationBtn(this) -> None:
		pass
	
	def unlockAcceptRelationBtn(this) -> None:
		pass
	
	def populateList(this, table: QListWidget, type: str) -> None:
		pass
	
	def relationConversion(this, item: int | str) -> str | int:
		pass
	
	def maxRelationLength(this) -> int:
		pass
	
	def titleConversion(this, item: int | str | None) -> str | int:
		pass
	
	def relationTupleConversion(this, relationship: tuple) -> tuple | None:
		pass


class themeManager():
	def __init__(self) -> None:
		self.functions = miscFunctions();
	
	def setTheme(this, self: startProgram, window: str, ) -> None:
		pass


class startProgram():
	def __init__(self) -> None:
		# Main Window
		self.mainWindow = QtWidgets.QMainWindow();
		self.ui = mainWindow();
		self.ui.setupUi();

		# Credits Window
		self.creditsWindow = QtWidgets.QWidget();
		self.creditsUI = creditsWindow();
		self.creditsUI.setupUi();
		
		# Options Window (Disabled)
		self.optionsWindow = QtWidgets.QWidget();
		self.optionsUI = optionsWindow();
		self.optionsUI.setupUi();
		
		# Edit Character Window
		self.editCharacterWindow = QtWidgets.QWidget();
		self.characterUI = editPersonWindow();
		self.characterUI.setupUi();
		
		# Add Relation Window
		self.addRelationWindow = QtWidgets.QWidget();
		self.addRelationUI = addRelationWindow();
		self.addRelationUI.setupUi();
		
		# World Building Window
		self.worldBuildingWindow = QtWidgets.QWidget();
		self.worldBuildingUI = worldBuildingWindow();
		self.worldBuildingUI.setupUi();
		
		self.settings: configLayout
		self.settings = {
			"theme": "Dark",
			"lang": 0,
		}
		self.data: dataLayout;
		self.data = {
			"characters": [],
			"world": []
		};
		self.fontType = QtGui.QFont,
		
		self.themeManager = themeManager()
		
		self.deathIcon = QtGui.QIcon;
		
		self.longestRelation: int;
		self.longestRelation = 10;
		
		self._characterRelations: list[characterRelations];
		self._characterRelations = [];