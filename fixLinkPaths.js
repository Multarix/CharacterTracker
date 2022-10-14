const fs = require("fs");

// const mainWindow = require("mainWindow.py");
// const infoWindow = require("info.py");
// const optionsWindow = require("options.py");
// const editWindow = rquire("editPerson.py");

fileArray = ["ui_mainWindow.py", "ui_optionsWindow.py", "ui_infoWindow.py", "ui_editPersonWindow.py", "ui_worldBuildingWindow.py", "ui_addRelationWindow.py", "ui_events.py"];
const reg = /QPixmap\("ui\\\\\.\.\/(.*?)"/

const line0 = "# type: ignore\n";
const line1 = 'import sys\n';
const line2 = 'import os\n';
const line3 = 'from PyQt5 import QtCore, QtGui, QtWidgets'
const line4 = '\n\ndef resource_path(relative_path):\n';
const line5 = '	""" Get absolute path to resource, works for dev and for PyInstaller """\n';
const line6 = '	base_path = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)));\n';
const line7 = '	return os.path.join(base_path, relative_path);';

const fullText = line0 + line1 + line2 + line3 + line4 + line5 + line6 + line7;

for(file of fileArray){
	f = fs.readFileSync(file, { encoding: 'utf8' });
	
	let item = reg.exec(f);
	while(item){
		f = f.replace(item[0], `QPixmap(resource_path("${item[1]}")`);
		item = reg.exec(f);
	}
	
	f = f.replace(line3, fullText);
	fs.writeFileSync(file, f, { encoding: 'utf8' });
	console.log(`- Successfully edited ${file}`);
}

