from __future__ import annotations
from typehinting import startProgram

from miscFunctions import miscFunctions

from PyQt5 import QtGui

from theme.darkTheme import darkTheme
from theme.lightTheme import lightTheme

# Fixing python to not be shit
true = True;
false = False;

themeConversion = {
	0: "Dark",
	1: "Light"
}

themes = {
	"Dark": darkTheme(),
	"Light": lightTheme()
};

class themeManager():
	def __init__(this, self: startProgram) -> None:
		this.functions = miscFunctions(self);
		
		this.setTheme(self, "main");
	# End of function


	def setTheme(this, self: startProgram, window: str, ) -> None:
		themeString = this._themeConvert(self.settings["theme"]);
		
		themeClass: darkTheme | lightTheme;
		themeClass = themes[themeString];
		
		if(window == "main"):
			this._setIcons(self, themeString)
			return themeClass.mainWindowTheme(self);
			
		if(window == "world"):
			return themeClass.worldWindowTheme(self);
			
		if(window == "credits"):
			return themeClass.creditWindowTheme(self);
			
		if(window == "options"):
			return themeClass.optionsWindowTheme(self);
			
		if(window == "person"):
			return themeClass.personWindowTheme(self);
			
		if(window == "relation"):
			return themeClass.relationWindowTheme(self);
	# End of function
	
	
	def _themeConvert(this, theme: int) -> str:
		themeType = themeConversion[theme];
		return themeType;
	# End of function


	def _setIcons(this, self: startProgram, theme: str) -> None:
	
		self.deathIcon = this._QIcon(f"icons\\dead_{theme}.png");
		
		# Character related
		self.ui.actionAdd_Character.setIcon(this._QIcon(f"icons\\addPerson_{theme}.png"));
		self.ui.actionEdit_Character.setIcon(this._QIcon(f"icons\\editCharacter_{theme}.png"));
		self.ui.actionRemove_Character.setIcon(this._QIcon(f"icons\\removeCharacter_{theme}.png"));

		# File related
		self.ui.action_New.setIcon(this._QIcon(f"icons\\new_{theme}.png"));
		self.ui.action_Open.setIcon(this._QIcon(f"icons\\open_{theme}.png"));
		self.ui.action_Save.setIcon(this._QIcon(f"icons\\save_{theme}.png"));
		self.ui.actionSave_As.setIcon(this._QIcon(f"icons\\saveAs_{theme}.png"));
		
		# Misc
		self.ui.actionRefresh.setIcon(this._QIcon(f"icons\\refresh_{theme}.png"));
		self.ui.action_Credits.setIcon(this._QIcon(f"icons\\about_{theme}.png"));
		self.ui.action_config.setIcon(this._QIcon(f"icons\\settings_{theme}.png"));
		self.ui.action_Exit.setIcon(this._QIcon(f"icons\\cancel_{theme}.png"));
	# End of function


	def _QIcon(this, file: str) -> QtGui.QIcon:
		path = this.functions.resource_path(file)
		icon = QtGui.QIcon();
		icon.addPixmap(QtGui.QPixmap(path));
		return icon;
	# End of function