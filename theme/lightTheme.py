# type: ignore
from typehinting import startProgram
import theme.light as theme

# from PyQt5 import QtGui

class lightTheme():
	def __init__(this) -> None:
		pass
	
	
	
	def creditWindowTheme(this, self: startProgram):
		self.creditsWindow.setStyleSheet(theme.window);
		self.creditsUI.programName.setStyleSheet(theme.labelOverride);
		self.creditsUI.link.setStyleSheet(theme.labelOverride);
		self.creditsUI.copyright.setStyleSheet(theme.labelOverride);



	def mainWindowTheme(this, self: startProgram):
		self.mainWindow.setStyleSheet(theme.window);
		
		self.ui.selectionDetails.setStyleSheet(theme.selectionDetails);
		self.ui.eventList.setStyleSheet(theme.worldBuildingList);
		self.ui.worldBuildingList.setStyleSheet(theme.worldBuildingList);
		
		# # Palette fix
		# palette = self.ui.characterSearch.palette();
		# palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor("#a0a2a5"));
		# self.ui.characterSearch.setPalette(palette);
		# self.ui.worldBuildingSearch.setPalette(palette);
		# Font
		self.ui.characterSearch.setFont(self.fontType);
		self.ui.eventSearch.setFont(self.fontType);
		self.ui.worldBuildingSearch.setFont(self.fontType);
		
		self.ui.charactersLabel.setFont(self.fontType);
		self.ui.eventLabel.setFont(self.fontType);
		self.ui.worldBuildingLabel.setFont(self.fontType);
		
		self.ui.characterList.setFont(self.fontType);
		self.ui.eventList.setFont(self.fontType)
		self.ui.worldBuildingList.setFont(self.fontType);
		self.ui.selectionDetails.setFont(self.fontType);
		


	def optionsWindowTheme(this, self: startProgram):
		self.optionsWindow.setStyleSheet(theme.window);



	def personWindowTheme(this, self: startProgram):
		self.editCharacterWindow.setStyleSheet(theme.window);

		# # Palette Fix
		# palette = self.characterUI.name.palette();
		# palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor("#a0a2a5"));
		# self.characterUI.name.setPalette(palette);
		# self.characterUI.species.setPalette(palette);
		# self.characterUI.textEdit.setPalette(palette);
		# Font
		self.characterUI.firstName.setFont(self.fontType);
		self.characterUI.lastName.setFont(self.fontType);
		self.characterUI.species.setFont(self.fontType);
		self.characterUI.textEdit.setFont(self.fontType);
		self.characterUI.relationTable.setFont(self.fontType);



	def relationWindowTheme(this, self: startProgram):
		self.addRelationWindow.setStyleSheet(theme.window);
		
		# # Palette Fix
		# palette = self.addRelationUI.search.palette();
		# palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor("#a0a2a5"));
		# self.addRelationUI.search.setPalette(palette);
		# self.addRelationUI.searchRelation.setPalette(palette);
		# Font
		self.addRelationUI.characterList.setFont(self.fontType);
		self.addRelationUI.relationType.setFont(self.fontType);
		self.addRelationUI.search.setFont(self.fontType);
		self.addRelationUI.searchRelation.setFont(self.fontType);



	def worldWindowTheme(this, self: startProgram):
		self.worldBuildingWindow.setStyleSheet(theme.window);
		
		# # Palette Fix
		# palette = self.worldBuildingUI.textEditor.palette();
		# palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor("#a0a2a5"));
		# self.worldBuildingUI.textEditor.setPalette(palette);
		# Font
		self.worldBuildingUI.textEditor.setFont(self.fontType);
		
	
	
	def eventWindowTheme(this, self: startProgram):
		self.eventWindow.setStyleSheet(theme.window);
		
		# # Palette Fix
		# palette = self.eventUI.textEditor.palette();
		# palette.setColor(QtGui.QPalette.PlaceholderText, QtGui.QColor("#a0a2a5"));
		# self.eventUI.textEditor.setPalette(palette);
		# Font
		self.eventUI.textEditor.setFont(self.fontType);