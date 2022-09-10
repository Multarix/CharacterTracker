#	 ██╗░░░██╗██╗    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
#	 ██║░░░██║██║    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
#	 ██║░░░██║██║    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
#	 ██║░░░██║██║    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
#	 ╚██████╔╝██║    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
#	 ░╚═════╝░╚═╝    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

from __future__ import annotations	# Type hinting

from typehinting import startProgram, miscDataLayout

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import *

from ui_editPersonWindow import Ui_editPersonWindow as editPersonWindow
from ui_addRelationWindow import Ui_addRelationWindow as addRelationWindow
from ui_worldBuildingWindow import Ui_worldBuildingWindow as worldBuildingWindow
from ui_optionsWindow import Ui_optionsWindow as optionsWindow
from ui_infoWindow import Ui_creditsWindow as creditsWindow


# Fixing python to not be shit
true = True;
false = False;


class windows():
	def __init__(this, ui):
		pass;

	def openCreditsWindow(this, self: startProgram):
		self.creditsWindow = QtWidgets.QDialog();
		self.creditsUI = creditsWindow();
		self.creditsUI.setupUi(self.creditsWindow);
		self.creditsWindow.show();
	# End of function
	
	
	def openOptionsWindow(this, self: startProgram):
		self.optionsWindow = QtWidgets.QDialog();
		self.optionsUI = optionsWindow();
		self.optionsUI.setupUi(self.optionsWindow);
		self.optionsWindow.show();
	# End of function
	
	
	def openEditCharacterWindow(this, self: startProgram, miscData: miscDataLayout, newChar: bool):
		"""
		Function to open the editCharacterUI when pressing the add or edit button on the mainWindowUI

		Args:
			newChar (bool): Whether a character is new or not
		"""

		self.editCharacterWindow = QtWidgets.QWidget();
		self.characterUI = editPersonWindow();
		self.characterUI.setupUi(self.editCharacterWindow);
		self.characterUI.characterID.hide(); # People don't need to see this, it's only for data tracking purposes
		
		# Fixing Palettes
		self.characterUI.textEdit.setPalette(miscData["palette"]);
		self.characterUI.name.setPalette(miscData["palette"]);
		self.characterUI.species.setPalette(miscData["palette"]);
		
		self._characterRelations.clear();
		
		# Buttons
		# Add
		self.characterUI.addRelation.clicked.connect(lambda: this.openAddRelationWindow(self, miscData, false));
		
		# Edit
		self.characterUI.editRelation.clicked.connect(lambda: this.openAddRelationWindow(self, miscData, true));
		self.characterUI.relationTable.currentRowChanged.connect(self.unlockEditRemoveRelationBtn)
		
		# Remove
		self.characterUI.removeRelation.clicked.connect(self.removeRelationBtn);
				
		# Accept
		self.characterUI.acceptForm.setDisabled(newChar);
		self.characterUI.name.textEdited.connect(self.unlockSubmitCharacterBtn);
		self.characterUI.acceptForm.clicked.connect(lambda: self.acceptCharacterBtn(newChar));
		
		# Font
		self.characterUI.name.setFont(miscData["font"]);
		self.characterUI.species.setFont(miscData["font"]);
		self.characterUI.textEdit.setFont(miscData["font"]);
		self.characterUI.relationTable.setFont(miscData["font"]);

		if(not newChar):
			currSelected = self.ui.characterList.currentRow();
			charData = self.data["characters"][currSelected];
			# id, name, title, age, gender (0=None, 1=Male, 2=Female), species, isdead (0=Alive), information, relations
			# 0   1     2      3    4                                  5        6                 7            8
			
			# ID
			self.characterUI.characterID.setValue(charData[0]);
			
			# Full Name
			self.characterUI.name.setText(charData[1]);
			
			# Title
			self.characterUI.titleSelector.setCurrentIndex(int(charData[2]));
			
			# Age
			self.characterUI.age.setValue(charData[3]);
			
			# Species
			self.characterUI.species.setText(charData[5]);
			
			# Character information
			self.characterUI.textEdit.setText(charData[7]);
			
			# Is Dead
			if(charData[6] == 1):
				self.characterUI.dead.setChecked(true);
			
			# Gender
			self.characterUI.genderSelector.setCurrentIndex(charData[4]);
			
			# Relations
			relations: str;
			relations = charData[8];
			if(relations):
				relationsArray = relations.split(", "); # Each relationship is seperated by ", "
				
				for relation in relationsArray:
					rel = relation.split("|"); # Each side of the relation is seperated by a "|"
					# rel[0] is the person, rel[1] is the type of relationship
					self._characterRelations.append((int(rel[0]), int(rel[1]))); # Add the item to the internal list, for later
				
				self.populateList(self.characterUI.relationTable, "relation");
		
		self.editCharacterWindow.show();
	# End of function
	

	def openAddRelationWindow(this, self: startProgram, miscData: miscDataLayout, existing: bool):
		"""
		Function to open the addRelationUI when pressing the add button on the editCharacterUI
		"""
		self.addRelationWindow = QtWidgets.QWidget();
		self.addRelationUI = addRelationWindow();
		self.addRelationUI.setupUi(self.addRelationWindow);
		
		# Fixing Palettes
		self.addRelationUI.search.setPalette(miscData["palette"]);
		self.addRelationUI.searchRelation.setPalette(miscData["palette"]);
		
		self.populateList(self.addRelationUI.characterList, "characters");
	
		self.addRelationUI.accept.clicked.connect(lambda: self.addRelationToListBtn(existing));
		self.addRelationUI.characterList.itemSelectionChanged.connect(self.unlockAcceptRelationBtn);
		self.addRelationUI.relationType.itemSelectionChanged.connect(self.unlockAcceptRelationBtn);
		
		# Search bars
		self.addRelationUI.search.textEdited.connect(lambda: self.searchBar(self.addRelationUI.search, self.addRelationUI.characterList));
		self.addRelationUI.searchRelation.textEdited.connect(lambda: self.searchBar(self.addRelationUI.searchRelation, self.addRelationUI.relationType));
		
		# Font
		self.addRelationUI.characterList.setFont(miscData["font"]);
		self.addRelationUI.relationType.setFont(miscData["font"]);
		self.addRelationUI.search.setFont(miscData["font"]);
		self.addRelationUI.searchRelation.setFont(miscData["font"]);
		
		if(existing): # Existing relationship
			relationIndex = self.characterUI.relationTable.currentRow();
			relationship = self._characterRelations[relationIndex];
			personID = relationship[0];
			relationTypeIndex = relationship[1];
			
			for i in range(len(self.data["characters"])):
				person = self.data["characters"][i];
				if(personID == person[0]):
					self.addRelationUI.characterList.setCurrentRow(i);
					self.addRelationUI.relationType.setCurrentRow(relationTypeIndex);
					break;

		self.addRelationWindow.show();
	# End of function
	
	
	def openWorldBuildingWindow(this, self: startProgram, miscData: miscDataLayout, newDetail: bool):
		self.worldBuildingWindow = QtWidgets.QDialog();
		self.worldBuildingUI = worldBuildingWindow();
		self.worldBuildingUI.setupUi(self.worldBuildingWindow);
		
		# Fixing Palettes
		self.worldBuildingUI.textEditor.setPalette(miscData["palette"]);
		
		# Accept button
		self.worldBuildingUI.accept.setDisabled(newDetail);
		self.worldBuildingUI.textEditor.textChanged.connect(self.unlockWorldBuildingAcceptBtn);
		self.worldBuildingUI.accept.clicked.connect(lambda: self.addWorldBuildingToListBtn(newDetail));
		
		if(not newDetail):
			currRow = self.ui.worldBuildingList.currentRow();
			self.worldBuildingUI.textEditor.setText(self.data["world"][currRow][0]);
		
		# Font
		self.worldBuildingUI.textEditor.setFont(miscData["font"]);
		
		self.worldBuildingWindow.show();
	# End of function