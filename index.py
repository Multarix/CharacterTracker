from __future__ import annotations					# Type hinting
from typehinting import dataLayout, configLayout	# Type hinting

# Misc Imports
import sys, platform, os, json

# QT
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import *						# type: ignore

from ui_mainWindow import Ui_mainWindow as mainWindow

from fileManagement import fileManager
from all_ui_Elements import windows
from buttonFunctions import buttonFunctions
from miscFunctions import miscFunctions
from themes import themeManager


defaultConfig: configLayout;
defaultConfig = {
	"theme": 0,
	"lang": 0,
	"longestRelation": 0
}


def getConfigData() -> list:
	homePath = os.path.abspath(os.path.expanduser("~"));
	configDirectory = os.path.join(homePath, ".characterTracker");
	if(not os.path.exists(configDirectory)):
		os.mkdir(configDirectory);
	
	configPath = os.path.join(configDirectory, "config.json");
	if(not os.path.exists(configPath)):
		file = open(configPath, "w");
		content = json.dumps(defaultConfig, indent="\t");
		file.write(content);
		file.close();
	
	f = open(configPath);
	configData = f.read();
	f.close();
	
	return [json.loads(configData), configPath];

configData = getConfigData();

config: dict[str, int];
config = configData[0];
configFilePath = configData[1];

##########################
## To Do:				##
## Options Menu			##
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


monospace = QtGui.QFont("Fira Code", 8);
monospace.setStyleHint(styleHint);


class startProgram(QMainWindow):
	def __init__(self):
		super().__init__();
		self.setWindowTitle("Character Tracker");
		self.mainWindow = QtWidgets.QMainWindow();
		self.ui = mainWindow();
		self.ui.setupUi(self.mainWindow);
		self.settings = config;
		self.fontType = monospace
		self.themeManager = themeManager(self);								# type: ignore
		
		self.data: dataLayout;
		self.data = {
			"characters": [],
			"world": [],
			"events": [],
			"settings": {
				"timelineLength": 5,
				"timelineScale": 12, # (Months per year)
				"startYear": 2000
			}
		};
		
		self._characterRelations = [];
		
		self.windows = windows(self);										# type: ignore
		self.file = fileManager(self);										# type: ignore
		self.buttons = buttonFunctions(self);								# type: ignore
		self.functions = miscFunctions(self);								# type: ignore
		
		config["longestRelation"] = self.functions.maxRelationLength();
		
		# Timeline stuff is not programatically functional yet, so disable it
		self.ui.timelineSlider.setDisabled(true);
		
		self._connections();
	# End of function
	
		
	def _connections(self) -> None:
		ui = self.ui;
		file = self.file;
		windows = self.windows;
		buttons = self.buttons;
		functions = self.functions;
		
		# --Fix Scrollbars--
		ui.characterList.verticalScrollBar().setSingleStep(10);
		ui.selectionDetails.verticalScrollBar().setSingleStep(10);
		ui.eventList.verticalScrollBar().setSingleStep(10);
		ui.worldBuildingList.verticalScrollBar().setSingleStep(10);
		
		# --Buttons to open other windows--
		ui.addPerson.clicked.connect(lambda: windows.openEditCharacterWindow(true));											# Add character
		ui.editPerson.clicked.connect(lambda: windows.openEditCharacterWindow(false));											# Edit character
		ui.characterList.itemDoubleClicked.connect(lambda: windows.openEditCharacterWindow(false));								# Edit character
		ui.worldBuildingAdd.clicked.connect(lambda: windows.openWorldBuildingWindow(true));										# Add world building
		ui.worldBuildingEdit.clicked.connect(lambda: windows.openWorldBuildingWindow(false)); 									# Edit world building
		ui.worldBuildingList.itemDoubleClicked.connect(lambda: windows.openWorldBuildingWindow(false));							# Edit world building
		ui.eventAdd.clicked.connect(lambda: windows.openEventWindow(true));														# Add event
		ui.eventEdit.clicked.connect(lambda: windows.openEventWindow(false));													# Edit event
		ui.eventList.itemDoubleClicked.connect(lambda: windows.openEventWindow(false));											# Edit event
		
		# --Functional Buttons--
		ui.removePerson.clicked.connect(buttons.removeCharacterBtn);															# Remove Character
		ui.eventRemove.clicked.connect(buttons.removeEventBtn);																	# Remove Event
		ui.worldBuildingRemove.clicked.connect(buttons.removeWorldBuilding);													# Remove world building
		ui.moveUp.clicked.connect(lambda: buttons.moveRow(-1)); 																# Move a row up
		ui.moveDown.clicked.connect(lambda: buttons.moveRow(1));																# Move a row down
		
		# --Menu Options--
		ui.action_New.triggered.connect(lambda: file.new);																		# New file
		ui.action_Save.triggered.connect(lambda: file.saveOrSaveAs(false, self.data));													# Save
		ui.action_Save_As.triggered.connect(lambda: file.saveOrSaveAs(true, self.data));												# Save as
		ui.action_Open.triggered.connect(self.file.open);																		# Open a file
		ui.action_Add_Character.triggered.connect(lambda: windows.openEditCharacterWindow(true));								# Add character
		ui.action_Edit_Character.triggered.connect(lambda: windows.openEditCharacterWindow(false));								# Edit character
		ui.action_Remove_Character.triggered.connect(buttons.removeCharacterBtn);												# Remove character
		ui.action_Refresh.triggered.connect(lambda: functions.populateList(ui.characterList, "characters"));					# Refresh
		ui.action_Settings.triggered.connect(windows.openOptionsWindow);														# Settings menu
		ui.action_Credits.triggered.connect(windows.openCreditsWindow);															# Credits menu
		
		# --Misc Functions--
		ui.characterSearch.textEdited.connect(lambda: functions.searchBar(ui.characterSearch, ui.characterList));				# Character search
		ui.eventSearch.textEdited.connect(lambda: functions.searchBar(ui.eventSearch, ui.eventList));							# Event search
		ui.worldBuildingSearch.textEdited.connect(lambda: functions.searchBar(ui.worldBuildingSearch, ui.worldBuildingList));	# World search
		ui.characterList.itemSelectionChanged.connect(functions.charListSelectionChange);										# Show details & Lock/ unlock character Buttons
		ui.eventList.itemSelectionChanged.connect(functions.unlockEditRemoveEventBtns);											# Lock/ unlock event Buttons
		ui.worldBuildingList.itemSelectionChanged.connect(functions.unlockWorldBuildingEditRemoveBtns);							# Lock/ unlock world buttons
	# End of function
	

def saveConfig(win: startProgram):
	settings = json.dumps(win.settings, indent="\t");
	
	configFile = open(configFilePath, "w");
	configFile.write(settings);
	configFile.close();


if(__name__ == "__main__"):
	app = QApplication(sys.argv);
	app.setApplicationDisplayName("Character Tracker");
	
	win = startProgram();
	
	app.aboutToQuit.connect(lambda: saveConfig(win));
	win.mainWindow.show();

	sys.exit(app.exec());