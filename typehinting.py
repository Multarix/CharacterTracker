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
character = Tuple[int, str, int, int, int, str, int, str, str]
worldItem = Tuple[str, int]
class dataLayout(TypedDict):
	"""Character and World data layout"""
	characters: list[character];
	world: list[worldItem];


class fixesLayout(TypedDict):
	font: QtGui.QFont;
	palette: QtGui.QPalette


class configLayout(TypedDict):
	"""Config settings layout"""
	theme: str;
	lang: int;
	longestRelation: int;


class startProgram():
	def __init__(self) -> None:
		# Main Window
		self.mainWindow = QtWidgets.QMainWindow();
		self.ui = mainWindow();
		self.ui.setupUi();

		# Credits Window
		self.creditsWindow = QtWidgets.QDialog();
		self.creditsUI = creditsWindow();
		self.creditsUI.setupUi();
		
		# Options Window (Disabled)
		self.optionsWindow = QtWidgets.QDialog();
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
		self.worldBuildingWindow = QtWidgets.QDialog();
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
		self.fixes: fixesLayout;
		self.fixes = {
			"font": QtGui.QFont,
			"palette": QtGui.QPalette
		}
		
		self.deathIcon = QtGui.QIcon;
		
		self.longestRelation: int;
		self.longestRelation = 10;
		
		self._characterRelations: list[characterRelations];
		self._characterRelations = [];