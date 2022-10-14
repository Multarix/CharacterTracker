# General Background
window = """QMainWindow {
	background: rgb(240, 240, 240);
	color: rgb(0, 0, 0);
}
QWidget {
	background: rgb(240, 240, 240);
	color: rgb(0, 0, 0);
}


/* QLineEdit */
QLineEdit {
	background: rgb(255, 255, 255);
	color: rgb(0, 0, 0);
	border: 1px solid rgb(200, 200, 200);
	border-radius:5px;
	padding-left: 3px;
	padding-right: 3px;
}


/* QPushButton */
QPushButton {
    background: rgb(230, 230, 230);
    color: rgb(0, 0, 0);
}
QPushButton:hover {
	background: rgb(220, 220, 220);
	color: rgb(0, 0, 0);
}
QPushButton:disabled {
	background: rgb(240, 240, 240);
	color: rgb(126, 126, 126);
}


/* QLabel */
QLabel {
	background: transparent;
	font: font "Fira Code";
}


/* QListWidget */
QListWidget {
	color: rgb(0, 0, 0);
	background: rgb(255, 255, 255);
	border: 1px solid rgb(200, 200, 200);
	border-radius:5px;
	outline: 0;
}
QListWidget:item {
	color: rgb(0, 0, 0);
	padding: 3px;
	border: 1px solid transparent;
	border-radius: 5px;
}
QListWidget:item:hover {
	padding-left: 3px;
	padding-right: 3px;
	background: rgb(250, 250, 250);
	border: 1px solid rgb(210, 210, 210);
}
QListWidget:item:selected {
	padding-left: 3px;
	padding-right: 3px;
	background: rgb(240, 240, 240);
	border: 1px solid rgb(200, 200, 200);
}


/* QComboBox */
QComboBox {
	background: rgb(255, 255, 255);
	border: 1px solid rgb(200, 200, 200);
	border-radius:5px;
	padding-left: 3px;
}


/* QSpinBox */
QSpinBox {
	background: rgb(255, 255, 255);
	color: rgb(0, 0, 0);
	border: 1px solid rgb(200, 200, 200);
	border-radius:5px;
	padding-left: 3px;
}
QSpinBox:disabled {
	background: rgb(240, 240, 240);
	color: rgb(126, 126, 126);
}


/* QTextEdit */
QTextEdit {
	background: rgb(255, 255, 255);
	color:rgb(0, 0, 0);
	border: 1px solid rgb(200, 200, 200);
	border-radius:5px;
	padding: 3px;
}


/* QTabWidget */
QTabWidget {
	background: rgb(240, 240, 240);
	color: rgb(0, 0, 0);
}
QTabWidget::tab-bar {
	left: 335px;
	top: 51px;
}
QTabWidget::pane {
	border: 0px;
}
QTabBar::tab {
	background: rgb(230, 230, 230);
}
QTabBar::tab:hover {
	background: rgb(220, 220, 220);
	color: rgb(0, 0, 0);
}
QTabBar::tab:selected {
	background: rgb(210, 210, 210);
	color: rgb(0, 0, 0);
}


/* QCheckBox */
QCheckBox {
	color: rgb(0, 0, 0);
	background: transparent;
	font: font "Fira Code";
}
QCheckBox::disabled {
	color: rgb(126, 126, 126);
}


/* QSlider */
QSlider {
	background: transparent;
}


/* QMenuBar */
QMenuBar {
	background: rgb(255, 255, 255);
	color: rgb(0, 0, 0);
}
QMenuBar::item {
	background: rgb(255, 255, 255);
	color: rgb(0, 0, 0);
}
QMenuBar::item:selected {
	background: rgb(230, 230, 230);
	color: rgb(0, 0, 0);
}
QMenu {
	background: rgb(240, 240, 240);
	color: rgb(0, 0, 0);
}
QMenu::item {
	background: rgb(240, 240, 240);
	color: rgb(0, 0, 0);
}
QMenu::item:selected {
	background: rgb(220, 220, 220);
	color: rgb(0, 0, 0);
}
QMenu::item:disabled {
	background: rgb(240, 240, 240);
	color: rgb(126, 126, 126);
}
QMenu::separator {
	color: rgb(0, 0, 0);
	padding-top: 4px;
}"""




# NOT DEFAULT ITEMS
## SELECTION DETAILS
selectionDetails = """QListWidget {
	color: rgb(0, 0, 0);
	background: rgb(255, 255, 255);
	border: 1px solid rgb(200, 200, 200);
	border-radius:5px;
	outline: 0;
}

QListWidget:item {
	padding: 3px;
	background: rgb(255, 255, 255);
}"""

## WORLD BUILDING LIST
worldBuildingList = """QListWidget {
	color: rgb(0, 0, 0);
	background: rgb(255, 255, 255);
	border: 1px solid rgb(200, 200, 200);
	border-radius: 5px;
	outline: 0;
}

QListWidget:item {
	color: rgb(0, 0, 0);
	padding-left: 3px;
	padding-right: 3px;
	border: 1px solid transparent;
	padding-top: 5px;
	padding-bottom: 5px;
	border-radius: 5px;
}

QListWidget:item:hover {
	background: rgb(250, 250, 250);
	border: 1px solid rgb(210, 210, 210);
}

QListWidget:item:selected {
	background: rgb(240, 240, 240);
	border: 1px solid rgb(200, 200, 200);
}"""

## LABEL OVERRIDE
labelOverride = """QLabel {
	background: transparent;
}"""