from typehinting import startProgram
import theme.darkFolder.creditWindow as creditWindow
import theme.darkFolder.mainWindow as mainWindow
import theme.darkFolder.optionsWindow as optionsWindow
import theme.darkFolder.personWindow as personWindow
import theme.darkFolder.relationWindow as relationWindow
import theme.darkFolder.worldWindow as worldWindow

class darkTheme():
	def __init__(this) -> None:
		pass
	
	def creditWindowTheme(this, self: startProgram):
		self.creditsWindow.setStyleSheet(creditWindow.creditsWindow);
		self.creditsUI.label.setStyleSheet(creditWindow.label_1);
		self.creditsUI.label_2.setStyleSheet(creditWindow.label_2);
		self.creditsUI.label_3.setStyleSheet(creditWindow.label_3);
		self.creditsUI.pushButton.setStyleSheet(creditWindow.pushButton);


	def mainWindowTheme(this, self: startProgram):
		self.mainWindow.setStyleSheet(mainWindow.mainWindow);
		self.ui.tabWidget.setStyleSheet(mainWindow.tabWidget);
		self.ui.addPerson.setStyleSheet(mainWindow.addPerson);
		self.ui.ageSlider.setStyleSheet(mainWindow.ageSlider);
		self.ui.ageSliderCount.setStyleSheet(mainWindow.ageSliderCount);
		self.ui.characterList.setStyleSheet(mainWindow.characterList);
		self.ui.characterSearch.setStyleSheet(mainWindow.characterSearch);
		self.ui.characterList.setStyleSheet(mainWindow.characterList);
		self.ui.editPerson.setStyleSheet(mainWindow.editPerson);
		self.ui.moveDown.setStyleSheet(mainWindow.moveDown);
		self.ui.moveUp.setStyleSheet(mainWindow.moveUp);
		self.ui.removePerson.setStyleSheet(mainWindow.removePerson);
		self.ui.selectionDetails.setStyleSheet(mainWindow.selectionDetails);
		self.ui.worldBuildingAdd.setStyleSheet(mainWindow.worldBuildingAdd);
		self.ui.worldBuildingEdit.setStyleSheet(mainWindow.worldBuildingEdit);
		self.ui.worldBuildingLabel.setStyleSheet(mainWindow.worldBuildingLabel);
		self.ui.worldBuildingList.setStyleSheet(mainWindow.worldBuildingList);
		self.ui.worldBuildingRemove.setStyleSheet(mainWindow.worldBuildingRemove);
		self.ui.worldBuildingSearch.setStyleSheet(mainWindow.worldBuildingSearch);
		self.ui.menubar.setStyleSheet(mainWindow.menubar);
		self.ui.menu_File.setStyleSheet(mainWindow.menubarTab);
		self.ui.menu_Options.setStyleSheet(mainWindow.menubarTab);
		self.ui.menuHelp.setStyleSheet(mainWindow.menubarTab);

	def optionsWindowTheme(this, self: startProgram):
		self.optionsWindow.setStyleSheet(optionsWindow.optionsWindow);
		self.optionsUI.accept.setStyleSheet(optionsWindow.acceptCancel);
		self.optionsUI.cancel.setStyleSheet(optionsWindow.acceptCancel);
		self.optionsUI.themeBox.setStyleSheet(optionsWindow.themeBox);
		self.optionsUI.themeLabel.setStyleSheet(optionsWindow.themeLabel);
		self.optionsUI.langBox.setStyleSheet(optionsWindow.langBox);
		self.optionsUI.langLabel.setStyleSheet(optionsWindow.langLabel);


	def personWindowTheme(this, self: startProgram):
		self.editCharacterWindow.setStyleSheet(personWindow.personWindow);
		self.characterUI.acceptForm.setStyleSheet(personWindow.acceptForm);
		self.characterUI.addRelation.setStyleSheet(personWindow.addRelation);
		self.characterUI.age.setStyleSheet(personWindow.age);
		self.characterUI.ageLabel.setStyleSheet(personWindow.ageLabel);
		self.characterUI.charInfoLabel.setStyleSheet(personWindow.charInfoLabel);
		self.characterUI.characterID.setStyleSheet(personWindow.characterID);
		self.characterUI.dead.setStyleSheet(personWindow.dead);
		self.characterUI.editRelation.setStyleSheet(personWindow.editRelation);
		self.characterUI.fullNameLabel.setStyleSheet(personWindow.fullNameLabel);
		self.characterUI.genderLabel.setStyleSheet(personWindow.genderLabel);
		self.characterUI.genderSelector.setStyleSheet(personWindow.genderSelector);
		self.characterUI.name.setStyleSheet(personWindow.name);
		self.characterUI.relationLabel.setStyleSheet(personWindow.relationLabel);
		self.characterUI.relationTable.setStyleSheet(personWindow.relationTable);
		self.characterUI.removeRelation.setStyleSheet(personWindow.removeRelation);
		self.characterUI.species.setStyleSheet(personWindow.species);
		self.characterUI.speciesLabel.setStyleSheet(personWindow.speciesLabel);
		self.characterUI.textEdit.setStyleSheet(personWindow.textEdit);
		self.characterUI.titleLabel.setStyleSheet(personWindow.titleLabel);
		self.characterUI.titleSelector.setStyleSheet(personWindow.titleSelector);


	def relationWindowTheme(this, self: startProgram):
		self.addRelationWindow.setStyleSheet(relationWindow.relationWindow);
		self.addRelationUI.accept.setStyleSheet(relationWindow.accept);
		self.addRelationUI.cancel.setStyleSheet(relationWindow.cancel);
		self.addRelationUI.characterList.setStyleSheet(relationWindow.characterList);
		self.addRelationUI.label.setStyleSheet(relationWindow.label1);
		self.addRelationUI.relationType.setStyleSheet(relationWindow.relationType);
		self.addRelationUI.search.setStyleSheet(relationWindow.search);
		self.addRelationUI.searchRelation.setStyleSheet(relationWindow.searchRelation);


	def worldWindowTheme(this, self: startProgram):
		self.worldBuildingWindow.setStyleSheet(worldWindow.worldBuildingWindow);
		self.worldBuildingUI.worldBuildingLabel.setStyleSheet(worldWindow.worldBuildingLabel);
		self.worldBuildingUI.accept.setStyleSheet(worldWindow.accept);
		self.worldBuildingUI.cancel.setStyleSheet(worldWindow.cancel);
		self.worldBuildingUI.textEditor.setStyleSheet(worldWindow.textEditor);