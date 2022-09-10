from __future__ import annotations	# Type hinting
from typehinting import dataLayout, configLayout, fixesLayout

# Misc Imports
import sys, os, platform

# QT
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *

from ui_mainWindow import Ui_mainWindow as mainWindow

from fileManagement import fileManager
from all_ui_Elements import windows
from buttonFunctions import buttonFunctions
from miscFunctions import miscFunctions

##########################
## To Do:				##
## Options Menu			##
## - Theme				##
## - Language?			##
##						##
## New File				##
##########################

fontStyle = QtGui.QFont.StyleHint;
styleHint = fontStyle.TypeWriter;

osType = platform.system();
if(osType == "Linux"):
	styleHint = fontStyle.Monospace;
	
if(osType == "Windows"):
	styleHint = fontStyle.TypeWriter;


true = True;
false = False;

defaultConfig: configLayout;
defaultConfig = {
	"theme":"Dark",
	"lang": 0,
	"longestRelation": 0
}

monospace = QtGui.QFont("Fira Code", 8);
monospace.setStyleHint(styleHint);

class startProgram(QMainWindow):
	def __init__(self):
		super().__init__();
		self.setWindowTitle("Character Tracker");
		self.mainWindow = QtWidgets.QMainWindow();
		self.ui = mainWindow();
		self.ui.setupUi(self.mainWindow);

		# Palette fix cause modal window breaks it for some reason?
		palette = self.ui.characterSearch.palette();
		palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor("#a0a2a5"));
		self.ui.characterSearch.setPalette(palette);
		self.ui.worldBuildingSearch.setPalette(palette);
		
		self.fixes: fixesLayout
		self.fixes = {
			"font": monospace,
			"palette": palette
		}
		
		self.data: dataLayout;
		self.data = {
			"characters": [],
			"world": []
		};
		
		self._characterRelations = [];
		
		self.windows = windows(self);
		self.file = fileManager(self);
		self.buttons = buttonFunctions(self);
		self.functions = miscFunctions(self);
		
		self.settings = defaultConfig;
		self.settings["longestRelation"] = self.functions.maxRelationLength();
		
		deathIconPath = self.functions.resource_path(f"icons\\dead_{self.settings['theme']}.png");
		self.deathIcon = QtGui.QIcon();
		self.deathIcon.addPixmap(QtGui.QPixmap(deathIconPath));

		# ageSlider stuff is not programatically functional yet, so hide and disable it
		self.ui.ageSlider.setHidden(true);
		self.ui.ageSlider.setDisabled(true);
		self.ui.ageSliderCount.setHidden(true);
		self.ui.ageSliderCount.setDisabled(true);
		
		self._connections();
		self._setFonts();
	# End of function
	
		
	def _connections(self):
		ui = self.ui;
		file = self.file;
		windows = self.windows;
		buttons = self.buttons;
		functions = self.functions;
		
		# --Buttons to open other windows--
		ui.addPerson.clicked.connect(lambda: windows.openEditCharacterWindow(true));											# Add character
		ui.editPerson.clicked.connect(lambda: windows.openEditCharacterWindow(false));											# Edit character
		ui.characterList.itemDoubleClicked.connect(lambda: windows.openEditCharacterWindow(false));								# Edit character
		ui.worldBuildingAdd.clicked.connect(lambda: windows.openWorldBuildingWindow(true));										# Add world building
		ui.worldBuildingEdit.clicked.connect(lambda: windows.openWorldBuildingWindow(false)); 									# Edit world building
		ui.worldBuildingList.itemDoubleClicked.connect(lambda: windows.openWorldBuildingWindow(false));							# Edit world building
		
		# --Functional Buttons--
		ui.removePerson.clicked.connect(buttons.removeCharacterBtn);															# Remove Character
		ui.worldBuildingRemove.clicked.connect(buttons.removeWorldBuilding);													# Remove world building
		ui.moveUp.clicked.connect(lambda: buttons.moveRow(-1)); 																# Move a row up
		ui.moveDown.clicked.connect(lambda: buttons.moveRow(1));																# Move a row down
		
		# --Menu Options--
		ui.action_New.triggered.connect(lambda: file.new);																		# New file
		ui.action_Save.triggered.connect(lambda: file.save(false, self.data));													# Save
		ui.actionSave_As.triggered.connect(lambda: file.save(true, self.data));													# Save as
		ui.action_Open.triggered.connect(self.file.open);																		# Open a file
		ui.actionAdd_Character.triggered.connect(lambda: windows.openEditCharacterWindow(true));								# Add character
		ui.actionEdit_Character.triggered.connect(lambda: windows.openEditCharacterWindow(false));								# Edit character
		ui.actionRemove_Character.triggered.connect(buttons.removeCharacterBtn);												# Remove character
		ui.actionRefresh.triggered.connect(lambda: functions.populateList(ui.characterList, "characters"));						# Refresh
		ui.action_config.triggered.connect(lambda: windows.openOptionsWindow(self));											# Settings menu
		ui.action_Credits.triggered.connect(lambda: windows.openCreditsWindow(self));											# Credits menu
		
		# --Misc Functions--
		ui.characterSearch.textEdited.connect(lambda: functions.searchBar(ui.characterSearch, ui.characterList));				# Character search
		ui.worldBuildingSearch.textEdited.connect(lambda: functions.searchBar(ui.worldBuildingSearch, ui.worldBuildingList));	# World search
		ui.characterList.itemSelectionChanged.connect(functions.showDetails);													# Show details
		ui.characterList.itemSelectionChanged.connect(functions.unlockEditRemoveCharacterBtns);									# Lock/ unlock character Buttons
		ui.worldBuildingList.itemSelectionChanged.connect(functions.unlockWorldBuildingEditRemoveBtns);							# Lock/ unlock world buttons
	# End of function
	

	def _setFonts(self):
		self.ui.characterSearch.setFont(monospace);
		self.ui.characterList.setFont(monospace);
		self.ui.selectionDetails.setFont(monospace);
		self.ui.worldBuildingList.setFont(monospace);
		self.ui.worldBuildingSearch.setFont(monospace);
	# End of function
	

if(__name__ == "__main__"):
	app = QApplication(sys.argv);
	app.setApplicationDisplayName("Character Tracker");
	win = startProgram();
	win.mainWindow.show();
	sys.exit(app.exec());