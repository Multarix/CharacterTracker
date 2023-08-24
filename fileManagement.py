#	 ███████╗██╗██╗░░░░░███████╗  ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗███╗░░░███╗███████╗███╗░░██╗████████╗
#	 ██╔════╝██║██║░░░░░██╔════╝  ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝████╗░████║██╔════╝████╗░██║╚══██╔══╝
#	 █████╗░░██║██║░░░░░█████╗░░  ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██╔████╔██║█████╗░░██╔██╗██║░░░██║░░░
#	 ██╔══╝░░██║██║░░░░░██╔══╝░░  ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██║╚██╔╝██║██╔══╝░░██║╚████║░░░██║░░░
#	 ██║░░░░░██║███████╗███████╗  ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░╚═╝░██║███████╗██║░╚███║░░░██║░░░
#	 ╚═╝░░░░░╚═╝╚══════╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░░░╚═╝░░░


from __future__ import annotations					# Type Hinting
from typehinting import startProgram, dataLayout	# Type Hinting

import sqlite3
import os

from PyQt5 import QtCore
from PyQt5.QtWidgets import *

from miscFunctions import miscFunctions

# Fixing python to not be shit
true = True;
false = False;


class fileManager():
	def __init__(this, self: startProgram) -> None:
		this.self = self
		this.functions = miscFunctions(self);
		
		this._version = "1.1";
		this._fileName = None;
		this._database = None;
		
		this.data: dataLayout;
		this.data = {
			"characters": [],
			"world": []
		};

	
	def new(this) -> None:
		# Gonna just wipe everything, close window and re-open?
		# Also ask to confirm
		pass
	# End of function
	
	
	def _saveAs(this) -> bool | str:
		"""
		Extra function to save a file with a specific filename

		Returns:
			bool | str: Returns false if there were no errors, otherwise returns the error code
		"""
		# Get the new save location
		fileLocation = QFileDialog.getSaveFileUrl(this.self, "Save File", QtCore.QUrl(""), "Character Tracker (*.chtr)", "Character Tracker (*.chtr)");
		
		if(fileLocation[0].toString() != ''): # If the user clicked cancel/ closed the dialog
			fileLocation = fileLocation[0].toString();
		else:
			return 1;
		
		fileLocation = fileLocation.replace("file:///", ""); # Remove the file related weirdness from QT
		fileArray = fileLocation.split("/");
		fileName = fileArray.pop(); # Get the filename from the last item in the array
		pathToFile = "/".join(fileArray); # Rejoin the path to file
		filePath = os.path.join(pathToFile, fileName); # Get the OS's version of the path to the file
		
		errorCode = "SAV000"; # Error code for making directory
		try:
			if(not os.path.exists(pathToFile)): # If the path to the given directory doesn't exist
				os.makedirs(pathToFile); # We make the path a thing
			
			errorCode = "SAV001"; # Error code for creating/ opening/ saving file
			file = open(filePath, "w"); # Create or open a file
			file.write(""); # Overwrite everything in the file to be empty
			file.close(); # And then save it
			
			errorCode = "SQL000"; # Error code for connecting to the SQL
			this._database = sqlite3.connect(filePath); # Now we turn it into a database
			
			errorCode = "SQL001"; # Error code for creating the SQL Schema
			this._createSchema(); # And create the SQL Schema
			
			this._fileName = filePath; # Assuming nothing went wrong, we can now set our fileName variable
			return false; # Return false, cause there were no errors
		except:
			return errorCode; # Something went wrong, so we return the code
	# End of function
	
				
	def save(this, saveAs: bool, data: dataLayout) -> None:
		"""
		Function to save a file

		Args:
			saveAs (bool): Whether or not to call _saveAs()
			data (dataLayout): The data to save
		"""
		if(not this._fileName or saveAs): # If the fileName has not been set, or saveAs is true
			errorCode = this._saveAs(); # We go through 'Save As'
			
			if(errorCode): # If there was an error
				if(errorCode == 1):
					return;
				else:
					print(f"An error occured: {errorCode})");
					return this._errorMessage(f"An error occured while saving the file (Error code: {errorCode})");
		
		print("Saving Changes...");
		errorCode = "SAV102"; # Error code for record deletion
		this._deleteRecords(); # Delete everything from our database
		
		errorCode = "SAV103"; # Error code for post deletion, pre character data - if you get this your data is fucked
		try:
			for person in data["characters"]:
				sql = this._database.cursor();
				sql.execute("INSERT INTO characters (id, name, title, age, gender, species, isdead, information, relationships) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", person);
				this._database.commit();
			
			errorCode = "SAV104"; # Error code for post character data, pre world data
			for worldItem in data["world"]:
				sql = this._database.cursor();
				sql.execute("INSERT INTO worldBuilding (text, notUsed) VALUES (?, ?)", worldItem);
				this._database.commit();
			
			return print("Save Complete!"); # Console message for saving success
		except:
			print(f"An error occured: {errorCode})");
			return this._errorMessage(f"An error occured while saving the file (Error code: {errorCode})");
	# End of function


	def _deleteRecords(this) -> None:
		try:
			sql = this._database.cursor();
			sql.execute("DELETE FROM characters");
			this._database.commit();
			
			sql.execute("DELETE FROM worldBuilding");
			this._database.commit();
		except:
			this._errorMessage("An error occured while saving the file (Error code: SAV000)"); # Error Code for during deleting data
	# End of function
	

	def open(this) -> None:
		"""
		Opens an sqlite database

		Args:
			file (str): The URL to the file
		"""
		self = this.self;
		fileName = QFileDialog.getOpenFileName(self, "Choose File", "", "Character Tracker (*.chtr);;All Files (*)")[0];
		
		if(not fileName): # If the user clicked cancel/ closed the dialog
			return;
		
		code = "OPN000"; # Not valid SQL
		try:
			this._database = sqlite3.connect(fileName);
			sql = this._database.cursor();
			
			code = "OPN001"; # No version table
			sql.execute("SELECT * from version");
			versionData = sql.fetchall();
			if(versionData[0][0] < this._version):
				this._updateSchema();
			
			code = "OPN002"; # No characters table
			sql.execute("SELECT * FROM characters");
			this.data["characters"] = sql.fetchall();
			this.functions.populateList(self.ui.characterList, "characters");
			
			code = "OPN003"; # No worldbuilding table
			sql.execute("SELECT * FROM worldBuilding");
			this.data["world"] =  sql.fetchall();
			this.functions.populateList(self.ui.worldBuildingList, "world");
			
			this._fileName = fileName;
		except:
			this._errorMessage(f"An error occured while opening the file (Error code: {code}");
		
		self.data = this.data;
		this.functions.populateList(self.ui.characterList, "characters");
		this.functions.populateList(self.ui.worldBuildingList, "world");
	# End of function
		

	def _createSchema(this) -> None:
		"""
		Creates the tables required in the sql spreadsheet
		"""
		if(not this._database):
			return;
		
		# Data storage
		sql = this._database.cursor();
		sql.execute('CREATE TABLE "characters" ("id" INTEGER, "name" TEXT, "title" INTEGER, "age" INTEGER, "gender" INTEGER, "species" TEXT, "isdead" INTEGER, "information" TEXT, "relationships" TEXT)');
		this._database.commit();
		
		sql.execute('CREATE TABLE "worldBuilding" ("text" TEXT, "notUsed" INTEGER);');
		this._database.commit();
		
		# Versioning control system
		sql.execute('CREATE TABLE "version" ("currentVersion" TEXT, "notUsed", INTEGER)');
		this._database.commit();
		sql.execute('INSERT INTO version (currentVersion, notUsed) VALUES (?, ?)', (this._version, 0));
		this._database.commit();
	# End of function
	

	def _updateSchema(this) -> None:
		pass;
	# End of function


	def _errorMessage(this, message: str) -> None:
		QMessageBox.critical(this.self, "Error", message);
	# End of function
