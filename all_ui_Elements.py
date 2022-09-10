#	 ██╗░░░██╗██╗    ███████╗██╗░░░██╗███╗░░██╗░█████╗░████████╗██╗░█████╗░███╗░░██╗░██████╗
#	 ██║░░░██║██║    ██╔════╝██║░░░██║████╗░██║██╔══██╗╚══██╔══╝██║██╔══██╗████╗░██║██╔════╝
#	 ██║░░░██║██║    █████╗░░██║░░░██║██╔██╗██║██║░░╚═╝░░░██║░░░██║██║░░██║██╔██╗██║╚█████╗░
#	 ██║░░░██║██║    ██╔══╝░░██║░░░██║██║╚████║██║░░██╗░░░██║░░░██║██║░░██║██║╚████║░╚═══██╗
#	 ╚██████╔╝██║    ██║░░░░░╚██████╔╝██║░╚███║╚█████╔╝░░░██║░░░██║╚█████╔╝██║░╚███║██████╔╝
#	 ░╚═════╝░╚═╝    ╚═╝░░░░░░╚═════╝░╚═╝░░╚══╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░╚═╝░░╚══╝╚═════╝░

from __future__ import annotations	# Type hinting

from typehinting import startProgram

from PyQt5 import QtWidgets
from PyQt5.QtGui import *

from ui_editPersonWindow import Ui_editPersonWindow as editPersonWindow
from ui_addRelationWindow import Ui_addRelationWindow as addRelationWindow
from ui_worldBuildingWindow import Ui_worldBuildingWindow as worldBuildingWindow
from ui_optionsWindow import Ui_optionsWindow as optionsWindow
from ui_infoWindow import Ui_creditsWindow as creditsWindow

from miscFunctions import miscFunctions
from buttonFunctions import buttonFunctions

# Fixing python to not be shit
true = True;
false = False;


class windows():
	def __init__(this, self: startProgram):
		this.self = self;
		this.functions = miscFunctions(self);
		this.buttons = buttonFunctions(self);


	def openCreditsWindow(this):
		self = this.self;
		self.creditsWindow = QtWidgets.QDialog();
		self.creditsUI = creditsWindow();
		self.creditsUI.setupUi(self.creditsWindow);
		self.creditsWindow.show();
	# End of function
	
	
	def openOptionsWindow(this):
		self = this.self;
		self.optionsWindow = QtWidgets.QDialog();
		self.optionsUI = optionsWindow();
		self.optionsUI.setupUi(self.optionsWindow);
		self.optionsWindow.show();
	# End of function
	
	
	def openEditCharacterWindow(this, newChar: bool):
		"""
		Function to open the editCharacterUI when pressing the add or edit button on the mainWindowUI

		Args:
			newChar (bool): Whether a character is new or not
		"""
		self = this.self;
		self.editCharacterWindow = QtWidgets.QWidget();
		self.characterUI = editPersonWindow();
		self.characterUI.setupUi(self.editCharacterWindow);
		self.characterUI.characterID.hide(); # People don't need to see this, it's only for data tracking purposes
		
		# Palette Fix
		self.characterUI.textEdit.setPalette(self.fixes["palette"]);
		self.characterUI.name.setPalette(self.fixes["palette"]);
		self.characterUI.species.setPalette(self.fixes["palette"]);
		# Font
		self.characterUI.name.setFont(self.fixes["font"]);
		self.characterUI.species.setFont(self.fixes["font"]);
		self.characterUI.textEdit.setFont(self.fixes["font"]);
		self.characterUI.relationTable.setFont(self.fixes["font"]);
		
		self._characterRelations.clear();
		
		# Buttons
		# Add
		self.characterUI.addRelation.clicked.connect(lambda: this.openAddRelationWindow(false));
		
		# Edit
		self.characterUI.editRelation.clicked.connect(lambda: this.openAddRelationWindow(true));
		self.characterUI.relationTable.currentRowChanged.connect(this.functions.unlockEditRemoveRelationBtn)
		
		# Remove
		self.characterUI.removeRelation.clicked.connect(this.buttons.removeRelationBtn);
				
		# Accept
		self.characterUI.acceptForm.setDisabled(newChar);
		self.characterUI.name.textEdited.connect(this.functions.unlockSubmitCharacterBtn);
		self.characterUI.acceptForm.clicked.connect(lambda: this.buttons.acceptCharacterBtn(newChar));
		


		if(not newChar):
			currSelected = self.ui.characterList.currentRow();
			charData = self.data["characters"][currSelected];
			# id, name, title, age, gender (0=None, 1=Male, 2=Female), species, isdead (0=Alive), information, relations
			# 0   1     2      3    4                                  5        6                 7            8
			
			self.characterUI.characterID.setValue(charData[0]);								# ID
			self.characterUI.name.setText(charData[1]);										# Full Name
			self.characterUI.titleSelector.setCurrentIndex(int(charData[2]));				# Title
			self.characterUI.age.setValue(charData[3]);										# Age
			self.characterUI.species.setText(charData[5]);									# Species
			self.characterUI.textEdit.setText(charData[7]);									# Character Info
			self.characterUI.genderSelector.setCurrentIndex(charData[4]);					# Gender
			
			if(charData[6] == 1):
				self.characterUI.dead.setChecked(true);										# Is Dead

			relations = charData[8];
			if(relations):
				relationsArray = relations.split(", "); # Each relationship is seperated by ", "
				
				for relation in relationsArray:
					rel = relation.split("|"); # Each side of the relation is seperated by a "|"
					# rel[0] is the person, rel[1] is the type of relationship
					self._characterRelations.append((int(rel[0]), int(rel[1]))); # Add the item to the internal list, for later
				
				this.functions.populateList(self.characterUI.relationTable, "relation");	# Relations
		
		self.editCharacterWindow.show();
	# End of function
	

	def openAddRelationWindow(this, existing: bool):
		"""
		Function to open the addRelationUI when pressing the add button on the editCharacterUI
		"""
		self = this.self;
		self.addRelationWindow = QtWidgets.QWidget();
		self.addRelationUI = addRelationWindow();
		self.addRelationUI.setupUi(self.addRelationWindow);
		
		# Palette Fix
		self.addRelationUI.search.setPalette(self.fixes["palette"]);
		self.addRelationUI.searchRelation.setPalette(self.fixes["palette"]);
		
		# Font
		self.addRelationUI.characterList.setFont(self.fixes["font"]);
		self.addRelationUI.relationType.setFont(self.fixes["font"]);
		self.addRelationUI.search.setFont(self.fixes["font"]);
		self.addRelationUI.searchRelation.setFont(self.fixes["font"]);
		
		this.functions.populateList(self.addRelationUI.characterList, "characters");
	
		# --Connections--
		self.addRelationUI.accept.clicked.connect(lambda: this.buttons.addRelationToListBtn(existing));
		self.addRelationUI.characterList.itemSelectionChanged.connect(this.functions.unlockAcceptRelationBtn);
		self.addRelationUI.relationType.itemSelectionChanged.connect(this.functions.unlockAcceptRelationBtn);
		
		# Search bars
		self.addRelationUI.search.textEdited.connect(lambda: this.functions.searchBar(self.addRelationUI.search, self.addRelationUI.characterList));
		self.addRelationUI.searchRelation.textEdited.connect(lambda: this.functions.searchBar(self.addRelationUI.searchRelation, self.addRelationUI.relationType));
		

		
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
	
	
	def openWorldBuildingWindow(this, newDetail: bool):
		self = this.self;
		self.worldBuildingWindow = QtWidgets.QDialog();
		self.worldBuildingUI = worldBuildingWindow();
		self.worldBuildingUI.setupUi(self.worldBuildingWindow);
		
		# Palette Fix
		self.worldBuildingUI.textEditor.setPalette(self.fixes["palette"]);
		# Font
		self.worldBuildingUI.textEditor.setFont(self.fixes["font"]);
		
		# Accept button
		self.worldBuildingUI.accept.setDisabled(newDetail);
		self.worldBuildingUI.textEditor.textChanged.connect(this.functions.unlockWorldBuildingAcceptBtn);
		self.worldBuildingUI.accept.clicked.connect(lambda: this.buttons.addWorldBuildingToListBtn(newDetail));
		
		if(not newDetail):
			currRow = self.ui.worldBuildingList.currentRow();
			self.worldBuildingUI.textEditor.setText(self.data["world"][currRow][0]);

		self.worldBuildingWindow.show();
	# End of function