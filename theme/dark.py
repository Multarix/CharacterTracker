# General Background
window ="""QMainWindow {
	background: rgb(54, 57, 63);
	color: rgb(255, 255, 255);
}
QWidget {
	background: rgb(54, 57, 63);
	color: rgb(255, 255, 255);
}


/* QLineEdit */
QLineEdit {
	background: rgb(64, 68, 75);
	color: rgb(255, 255, 255);
	border: 1px solid rgb(50, 50, 50);
	border-radius:5px;
	padding-left: 3px;
	padding-right: 3px;
}


/* QPushButton */
QPushButton {
    background: rgb(64, 68, 75);
    color: rgb(255, 255, 255);
}
QPushButton:hover {
	background: rgb(79, 83, 89);
	color: rgb(255, 255, 255);
}
QPushButton:disabled {
	background: rgb(54, 57, 63);
	color: rgb(126, 126, 126);
}


/* QLabel */
QLabel {
	background: transparent;
	font: font "Fira Code";
}


/* QListWidget */
QListWidget{
	color: rgb(255, 255, 255);
	background: rgb(64, 68, 75);
	border: 1px solid rgb(50, 50, 50);
	border-radius:5px;
	outline: 0;
}
QListWidget:item{
	color: rgb(255, 255, 255);
	padding: 3px;
	border: 1px solid transparent;
	border-radius: 5px;
}
QListWidget:item:hover{
	padding-left: 3px;
	padding-right: 3px;
	background: rgb(74, 76, 79);
	border: 1px solid rgb(64, 66, 75);
}
QListWidget:item:selected{
	padding-left: 3px;
	padding-right: 3px;
	background: rgb(93, 94, 97);
	border: 1px solid rgb(74, 76, 79);
}


/* QComboBox */
QComboBox {
	background: rgb(64, 68, 75);
	border: 1px solid rgb(50, 50, 50);
	border-radius:5px;
	padding-left: 3px;
}


/* QSpinBox */
QSpinBox {
    background: rgb(64, 68, 75);
    color: rgb(255, 255, 255);
	border: 1px solid rgb(50, 50, 50);
	border-radius:5px;
	padding-left: 3px;
}
QSpinBox:disabled {
	background: rgb(54, 57, 63);
	color: rgb(126, 126, 126);
}


/* QTextEdit */
QTextEdit {
	background: rgb(64, 68, 75);
	color:rgb(255, 255, 255);
	border: 1px solid rgb(50, 50, 50);
	border-radius:5px;
	padding: 3px;
}


/* QTabWidget */
QTabWidget {
	background: rgb(54, 57, 63);
	color: rgb(255, 255, 255);
}
QTabWidget::tab-bar {
	left: 335px;
	top: 51px;
}
QTabWidget::pane {
	border: 0px;
}
QTabBar::tab {
	background: rgb(64, 68, 75);
}
QTabBar::tab:hover {
	background: rgb(79, 83, 89);
	color: rgb(255, 255, 255);
}
QTabBar::tab:selected {
	background: rgb(89, 93, 99);
	color: rgb(255, 255, 255);
}


/* QCheckBox */
QCheckBox {
	color: rgb(255, 255, 255);
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
	background: rgb(41, 43, 47);
	color: rgb(255, 255, 255);
}
QMenuBar::item {
	background: rgb(41, 43, 47);
	color: rgb(255, 255, 255);
}
QMenuBar::item:selected {
	background: rgb(64, 68, 74);
	color: rgb(255, 255, 255);
}
QMenu {
	background: rgb(41, 43, 47);
	color: rgb(255, 255, 255);
}
QMenu::item {
	background: rgb(41, 43, 47);
	color: rgb(255, 255, 255);
}
QMenu::item:selected {
	background: rgb(64, 68, 74);
	color: rgb(255, 255, 255);
}
QMenu::item:disabled {
	background: rgb(41, 43, 47);
	color: rgb(126, 126, 126);
}
QMenu::separator {
	color: rgb(0, 0, 0);
	padding-top: 4px;
}"""


# NOT DEFAULT ITEMS
## SELECTION DETAILS
selectionDetails = """QListWidget{
	color: rgb(255, 255, 255);
	background: rgb(64, 68, 75);
	border: 1px solid rgb(50, 50, 50);
	border-radius:5px;
	outline: 0;
}

QListWidget:item{
	padding: 3px;
	background: rgb(64, 68, 75);
}"
"""

## WORLD BUILDING LIST
worldBuildingList = """QListWidget{
	color: rgb(255, 255, 255);
	background: rgb(64, 68, 75);
	border: 1px solid rgb(50, 50, 50);
	border-radius:5px;
	outline: 0;
}

QListWidget:item{
	color: rgb(255, 255, 255);
	padding-left: 3px;
	padding-right: 3px;
	border: 1px solid transparent;
	padding-top: 5px;
	padding-bottom: 5px;
	border-radius: 5px;
}

QListWidget:item:hover{
	background: rgb(74, 76, 79);
	border: 1px solid rgb(64, 66, 75);
}

QListWidget:item:selected{
	background: rgb(93, 94, 97);
	border: 1px solid rgb(74, 76, 79);
}"
"""

## LABEL OVERRIDE
labelOverride = """QLabel {
	background: transparent;
}"""