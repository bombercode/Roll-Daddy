'''
Roll Daddy
Created by Austin Poe | John Hornak | 2020
Released under GNU General Public License Version 3

'''

import sys
import random
import qdarkstyle
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_root(object):
    def setupUi(self, root):
#This is the main window and settings for it
        root.setObjectName("root")
        #Sets the dark style sheet
        root.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
#sets the window size and min/max
        root.resize(500, 375)
        root.setMinimumSize(QtCore.QSize(500, 375))
        root.setMaximumSize(QtCore.QSize(500, 375))
#these next couple of lines are setting the icon shown on the window
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/d20.ico"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        root.setWindowIcon(icon)
#alot of this is setting up the layout of the grid layout all of the widgets are in
        root.setToolTipDuration(3)
        root.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 0, 500, 315))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.layoutWidget.setFont(font)
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(10, 0, 10, 0)
        self.gridLayout.setObjectName("gridLayout")
#this huge chunk is setting up all the different widgets and their attributes 
#each row of widgets is seperated by an indent for clarity
        self.dice_number_1 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_number_1.setMinimum(1)
        self.dice_number_1.setFont(font)
        self.dice_number_1.setObjectName("dice_number_1")
        self.gridLayout.addWidget(self.dice_number_1, 0, 0, 1, 1)        
        self.dice_select_1 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_select_1.setFont(font)
        self.dice_select_1.setToolTip("")
        self.dice_select_1.setToolTipDuration(6)
        self.dice_select_1.setObjectName("dice_select_1")
        self.dice_select_1.addItem("")
        self.dice_select_1.addItem("")
        self.dice_select_1.addItem("")
        self.dice_select_1.addItem("")
        self.dice_select_1.addItem("")
        self.dice_select_1.addItem("")
        self.dice_select_1.addItem("")
        self.dice_select_1.addItem("")
        self.gridLayout.addWidget(self.dice_select_1, 0, 1, 1, 1)        
        self.modbox_1 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.modbox_1.setFont(font)
        self.modbox_1.setObjectName("modbox_1")
        self.modbox_1.addItem("")
        self.modbox_1.addItem("")
        self.gridLayout.addWidget(self.modbox_1, 0, 2, 1, 1)        
        self.mod_number_1 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mod_number_1.setFont(font)
        self.mod_number_1.setToolTip("")
        self.mod_number_1.setObjectName("mod_number_1")
        self.gridLayout.addWidget(self.mod_number_1, 0, 3, 1, 1)        
        self.roll_button_1 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.roll_button_1.setFont(font)
        self.roll_button_1.setObjectName("roll_button_1")
        self.gridLayout.addWidget(self.roll_button_1, 0, 4, 1, 1)
#this longboi calls the roll method (implemented for each button)  
        self.roll_button_1.clicked.connect(lambda: self.roll(str(self.dice_select_1.currentText()), 1, int(self.dice_number_1.value()), str(self.modbox_1.currentText()), int(self.mod_number_1.value()))) 
        self.output_1 = QtWidgets.QLabel(self.layoutWidget)
        self.output_1.setEnabled(True)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(65)
        self.output_1.setFont(font)
        self.output_1.setObjectName("output_1")
        self.gridLayout.addWidget(self.output_1, 0, 5, 1, 1)
        
        self.dice_number_2 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_number_2.setMinimum(1)
        self.dice_number_2.setFont(font)
        self.dice_number_2.setObjectName("dice_number_2")
        self.gridLayout.addWidget(self.dice_number_2, 1, 0, 1, 1)        
        self.dice_select_2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_select_2.setFont(font)
        self.dice_select_2.setObjectName("dice_select_2")
        self.dice_select_2.addItem("")
        self.dice_select_2.addItem("")
        self.dice_select_2.addItem("")
        self.dice_select_2.addItem("")
        self.dice_select_2.addItem("")
        self.dice_select_2.addItem("")
        self.dice_select_2.addItem("")
        self.dice_select_2.addItem("")
        self.gridLayout.addWidget(self.dice_select_2, 1, 1, 1, 1)        
        self.modbox_2 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.modbox_2.setFont(font)
        self.modbox_2.setObjectName("modbox_2")
        self.modbox_2.addItem("")
        self.modbox_2.addItem("")
        self.gridLayout.addWidget(self.modbox_2, 1, 2, 1, 1)        
        self.mod_number_2 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mod_number_2.setFont(font)
        self.mod_number_2.setObjectName("mod_number_2")
        self.gridLayout.addWidget(self.mod_number_2, 1, 3, 1, 1)        
        self.roll_button_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.roll_button_2.setFont(font)
        self.roll_button_2.setObjectName("roll_button_2")
        self.gridLayout.addWidget(self.roll_button_2, 1, 4, 1, 1) 
        self.roll_button_2.clicked.connect(lambda: self.roll(str(self.dice_select_2.currentText()), 2, int(self.dice_number_2.value()), str(self.modbox_2.currentText()), int(self.mod_number_2.value())))
        self.output_2 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(65)
        self.output_2.setFont(font)
        self.output_2.setObjectName("output_2")
        self.gridLayout.addWidget(self.output_2, 1, 5, 1, 1)
        
        self.dice_number_3 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_number_3.setMinimum(1)
        self.dice_number_3.setFont(font)
        self.dice_number_3.setObjectName("dice_number_3")
        self.gridLayout.addWidget(self.dice_number_3, 2, 0, 1, 1)        
        self.dice_select_3 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_select_3.setFont(font)
        self.dice_select_3.setObjectName("dice_select_3")
        self.dice_select_3.addItem("")
        self.dice_select_3.addItem("")
        self.dice_select_3.addItem("")
        self.dice_select_3.addItem("")
        self.dice_select_3.addItem("")
        self.dice_select_3.addItem("")
        self.dice_select_3.addItem("")
        self.dice_select_3.addItem("")
        self.gridLayout.addWidget(self.dice_select_3, 2, 1, 1, 1)               
        self.modbox_3 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.modbox_3.setFont(font)
        self.modbox_3.setObjectName("modbox_3")
        self.modbox_3.addItem("")
        self.modbox_3.addItem("")
        self.gridLayout.addWidget(self.modbox_3, 2, 2, 1, 1)        
        self.mod_number_3 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mod_number_3.setFont(font)
        self.mod_number_3.setObjectName("mod_number_3")
        self.gridLayout.addWidget(self.mod_number_3, 2, 3, 1, 1)                
        self.roll_button_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.roll_button_3.setFont(font)
        self.roll_button_3.setObjectName("roll_button_3")
        self.gridLayout.addWidget(self.roll_button_3, 2, 4, 1, 1)
        self.roll_button_3.clicked.connect(lambda: self.roll(str(self.dice_select_3.currentText()), 3, int(self.dice_number_3.value()), str(self.modbox_3.currentText()), int(self.mod_number_3.value())))
        self.output_3 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(65)
        self.output_3.setFont(font)
        self.output_3.setObjectName("output_3")
        self.gridLayout.addWidget(self.output_3, 2, 5, 1, 1)
        
        self.dice_number_4 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_number_4.setMinimum(1)
        self.dice_number_4.setFont(font)
        self.dice_number_4.setObjectName("dice_number_4")
        self.gridLayout.addWidget(self.dice_number_4, 3, 0, 1, 1)        
        self.dice_select_4 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_select_4.setFont(font)
        self.dice_select_4.setObjectName("dice_select_4")
        self.dice_select_4.addItem("")
        self.dice_select_4.addItem("")
        self.dice_select_4.addItem("")
        self.dice_select_4.addItem("")
        self.dice_select_4.addItem("")
        self.dice_select_4.addItem("")
        self.dice_select_4.addItem("")
        self.dice_select_4.addItem("")
        self.gridLayout.addWidget(self.dice_select_4, 3, 1, 1, 1)              
        self.modbox_4 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.modbox_4.setFont(font)
        self.modbox_4.setObjectName("modbox_4")
        self.modbox_4.addItem("")
        self.modbox_4.addItem("")
        self.gridLayout.addWidget(self.modbox_4, 3, 2, 1, 1)        
        self.mod_number_4 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mod_number_4.setFont(font)
        self.mod_number_4.setObjectName("mod_number_4")
        self.gridLayout.addWidget(self.mod_number_4, 3, 3, 1, 1)
        self.roll_button_4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.roll_button_4.setFont(font)
        self.roll_button_4.setObjectName("roll_button_4")
        self.gridLayout.addWidget(self.roll_button_4, 3, 4, 1, 1)
        self.roll_button_4.clicked.connect(lambda: self.roll(str(self.dice_select_4.currentText()), 4, int(self.dice_number_4.value()), str(self.modbox_4.currentText()), int(self.mod_number_4.value())))
        self.output_4 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(65)
        self.output_4.setFont(font)
        self.output_4.setObjectName("output_4")
        self.gridLayout.addWidget(self.output_4, 3, 5, 1, 1)       
        
        self.dice_number_5 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_number_5.setMinimum(1)
        self.dice_number_5.setFont(font)
        self.dice_number_5.setObjectName("dice_number_5")
        self.gridLayout.addWidget(self.dice_number_5, 4, 0, 1, 1)                
        self.dice_select_5 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.dice_select_5.setFont(font)
        self.dice_select_5.setObjectName("dice_select_5")
        self.dice_select_5.addItem("")
        self.dice_select_5.addItem("")
        self.dice_select_5.addItem("")
        self.dice_select_5.addItem("")
        self.dice_select_5.addItem("")
        self.dice_select_5.addItem("")
        self.dice_select_5.addItem("")
        self.dice_select_5.addItem("")
        self.gridLayout.addWidget(self.dice_select_5, 4, 1, 1, 1)        
        self.modbox_5 = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.modbox_5.setFont(font)
        self.modbox_5.setObjectName("modbox_5")
        self.modbox_5.addItem("")
        self.modbox_5.addItem("")
        self.gridLayout.addWidget(self.modbox_5, 4, 2, 1, 1)        
        self.mod_number_5 = QtWidgets.QSpinBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.mod_number_5.setFont(font)
        self.mod_number_5.setObjectName("mod_number_5")
        self.gridLayout.addWidget(self.mod_number_5, 4, 3, 1, 1)        
        self.roll_button_5 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.roll_button_5.setFont(font)
        self.roll_button_5.setObjectName("roll_button_5")
        self.gridLayout.addWidget(self.roll_button_5, 4, 4, 1, 1)
        self.roll_button_5.clicked.connect(lambda: self.roll(str(self.dice_select_5.currentText()), 5, int(self.dice_number_5.value()), str(self.modbox_5.currentText()), int(self.mod_number_5.value())))
        self.output_5 = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(65)
        self.output_5.setFont(font)
        self.output_5.setObjectName("output_5")
        self.gridLayout.addWidget(self.output_5, 4, 5, 1, 1)     
        root.setCentralWidget(self.centralwidget)
#this chunk sets up the menu and the options inside of it
        self.menubar = QtWidgets.QMenuBar(root)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 475, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        root.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(root)
        self.statusbar.setObjectName("statusbar")
        root.setStatusBar(self.statusbar)
        self.actionReset = QtWidgets.QAction(root)
        self.actionReset.setObjectName("actionReset")
        self.actionReset.triggered.connect(self.reset)
        self.menuFile.addAction(self.actionReset)
        self.menubar.addAction(self.menuFile.menuAction())

#not sure what this is doing
        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
#sets the window title (just realized you can put a comment on the same line as code)
        root.setWindowTitle(_translate("root", "Roll Daddy"))
#this sets the text for all the widgets 
        self.dice_select_1.setItemText(0, _translate("root", "d20"))
        self.dice_select_1.setItemText(1, _translate("root", "d12"))
        self.dice_select_1.setItemText(2, _translate("root", "d10"))
        self.dice_select_1.setItemText(3, _translate("root", "d8"))
        self.dice_select_1.setItemText(4, _translate("root", "d6"))
        self.dice_select_1.setItemText(5, _translate("root", "d4"))
        self.dice_select_1.setItemText(6, _translate("root", "d3"))
        self.dice_select_1.setItemText(7, _translate("root", "d2"))
        self.dice_select_2.setItemText(0, _translate("root", "d20"))
        self.dice_select_2.setItemText(1, _translate("root", "d12"))
        self.dice_select_2.setItemText(2, _translate("root", "d10"))
        self.dice_select_2.setItemText(3, _translate("root", "d8"))
        self.dice_select_2.setItemText(4, _translate("root", "d6"))
        self.dice_select_2.setItemText(5, _translate("root", "d4"))
        self.dice_select_2.setItemText(6, _translate("root", "d3"))
        self.dice_select_2.setItemText(7, _translate("root", "d2"))
        self.dice_select_3.setItemText(0, _translate("root", "d20"))
        self.dice_select_3.setItemText(1, _translate("root", "d12"))
        self.dice_select_3.setItemText(2, _translate("root", "d10"))
        self.dice_select_3.setItemText(3, _translate("root", "d8"))
        self.dice_select_3.setItemText(4, _translate("root", "d6"))
        self.dice_select_3.setItemText(5, _translate("root", "d4"))
        self.dice_select_3.setItemText(6, _translate("root", "d3"))
        self.dice_select_3.setItemText(7, _translate("root", "d2"))
        self.dice_select_4.setItemText(0, _translate("root", "d20"))
        self.dice_select_4.setItemText(1, _translate("root", "d12"))
        self.dice_select_4.setItemText(2, _translate("root", "d10"))
        self.dice_select_4.setItemText(3, _translate("root", "d8"))
        self.dice_select_4.setItemText(4, _translate("root", "d6"))
        self.dice_select_4.setItemText(5, _translate("root", "d4"))
        self.dice_select_4.setItemText(6, _translate("root", "d3"))
        self.dice_select_4.setItemText(7, _translate("root", "d2"))
        self.dice_select_5.setItemText(0, _translate("root", "d20"))
        self.dice_select_5.setItemText(1, _translate("root", "d12"))
        self.dice_select_5.setItemText(2, _translate("root", "d10"))
        self.dice_select_5.setItemText(3, _translate("root", "d8"))
        self.dice_select_5.setItemText(4, _translate("root", "d6"))
        self.dice_select_5.setItemText(5, _translate("root", "d4"))
        self.dice_select_5.setItemText(6, _translate("root", "d3"))
        self.dice_select_5.setItemText(7, _translate("root", "d2"))

        self.modbox_1.setItemText(0, _translate("root", "+"))
        self.modbox_1.setItemText(1, _translate("root", "-"))
        self.modbox_2.setItemText(0, _translate("root", "+"))
        self.modbox_2.setItemText(1, _translate("root", "-"))
        self.modbox_3.setItemText(0, _translate("root", "+"))
        self.modbox_3.setItemText(1, _translate("root", "-"))
        self.modbox_4.setItemText(0, _translate("root", "+"))
        self.modbox_4.setItemText(1, _translate("root", "-"))
        self.modbox_5.setItemText(0, _translate("root", "+"))
        self.modbox_5.setItemText(1, _translate("root", "-"))    

        self.roll_button_1.setText(_translate("root", "Roll"))
        self.roll_button_2.setText(_translate("root", "Roll"))
        self.roll_button_3.setText(_translate("root", "Roll"))
        self.roll_button_4.setText(_translate("root", "Roll"))
        self.roll_button_5.setText(_translate("root", "Roll"))
        
        self.output_1.setText(_translate("root", ""))
        self.output_2.setText(_translate("root", ""))
        self.output_3.setText(_translate("root", ""))
        self.output_4.setText(_translate("root", ""))
        self.output_5.setText(_translate("root", ""))

        self.menuFile.setTitle(_translate("root", "File"))
        self.actionReset.setText(_translate("root", "Reset"))
        

#this outputs the result of the roll        
    def roll_out(self, result, buttonNumber):
        if buttonNumber == 1:
            self.output_1.setText(str(result))
        elif buttonNumber == 2:
            self.output_2.setText(str(result))
        elif buttonNumber == 3:
            self.output_3.setText(str(result))
        elif buttonNumber == 4:
            self.output_4.setText(str(result))
        elif buttonNumber == 5:
            self.output_5.setText(str(result))

    def roll(self, dice, buttonNumber, diceNumber, modSign, modNumber):  
# This is called when the roll button is clicked,
# If the drop down name selected matches the name in the conditional, a roll is executed
        result = 0
        if modSign == "-":
            modNumber = modNumber * -1
            
        if dice == "d20":
            while (diceNumber > 0):
                result = random.randint(1, 20) + result
                diceNumber -= 1
        elif dice == "d12":
            while (diceNumber > 0):
                result = random.randint(1, 12) + result
                diceNumber -= 1
        elif dice == "d10":
            while (diceNumber > 0):
                result = random.randint(1, 10) + result
                diceNumber -= 1
        elif dice == "d8":
            while (diceNumber > 0):
                result = random.randint(1, 8) + result
                diceNumber -= 1
        elif dice == "d6":
            while (diceNumber > 0):
                result = random.randint(1, 6) + result
                diceNumber -= 1
        elif dice == "d4":
            while (diceNumber > 0):
                result = random.randint(1, 4) + result
                diceNumber -= 1
        elif dice == "d3":
            while (diceNumber > 0):
                result = random.randint(1, 3) + result
                diceNumber -= 1
        elif dice == "d2":
            while (diceNumber > 0):
                result = random.randint(1, 2) + result
                diceNumber -= 1
        self.roll_out(result + modNumber, buttonNumber) 

#called when the reset button is pressed (resets the output windows)        
    def reset(self):
        self.output_1.setText("")
        self.output_2.setText("")
        self.output_3.setText("")
        self.output_4.setText("")
        self.output_5.setText("")



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    root = QtWidgets.QMainWindow()
    ui = Ui_root()
    ui.setupUi(root)
    root.show()
    sys.exit(app.exec_())

