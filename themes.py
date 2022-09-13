from typehinting import startProgram
from miscFunctions import miscFunctions

from PyQt5 import QtGui

true = True;
false = False;

themes = {
	0: "Dark",
	1: "Light"
}

class themeManager():
	def __init__(this, self: startProgram) -> None:
		this.self = self;
		this.functions = miscFunctions();
		
		this.swapTheme(self.settings["theme"]);
	# End of function
	

	def swapTheme(this, theme: int):
		themeType = themes[theme];
		
		this._swapIcons(themeType);
		# this._swapColors(themeType);
	# End of function


	def _swapIcons(this, theme):
		self = this.self;

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
