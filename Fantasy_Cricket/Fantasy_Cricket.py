#
# Fantasy Cricket.py
#
# Created by: Sugitha S Babu
#
# Created on: 27 ‎November ‎2019
#
# Last Updated on: 18 ‎December ‎2019


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QPushButton, QLineEdit, QMessageBox, QInputDialog, QApplication, QLabel, QToolTip)
from functools import partial
from CustomDialog_NewTeam import Ui_Dialog_1
from CustomDialog_OpenTeam import Ui_Dialog_2
from CustomDialog_EvaluateTeam import Ui_Dialog_3
from Team_Preview_Dialog import Ui_Dialog_4
from picture_background import qt_resource_data
import sys
import sqlite3
import base64
        
class Ui_MainWindow(object):
    def __init__(self): 
        self.batsman_record = []
        self.bowlers_record = []
        self.allrounders_record = []
        self.wicketkeepers_record = []
        self.selectedplayers = []
        self.connection = None
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setStatusTip("")
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(12)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setAcceptDrops(False)
        self.frame.setAutoFillBackground(False)
        self.frame.setStyleSheet("border-color: rgb(136, 136, 136);\n"
"background-color: rgb(5, 189, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.label.setWordWrap(False)
        self.label.setIndent(-6)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_10.setSpacing(69)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_6.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(194, 11, 200);")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setBold(True)
        font.setPointSize(12)
        font.setWeight(75)
        self.label.setFont(font)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(font)
        self.horizontalLayout_7.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(194, 11, 200);")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_8.addWidget(self.label_6)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.label_7.setStyleSheet("color: rgb(194, 11, 200);")
        self.label_7.setFont(font)
        self.horizontalLayout_8.addWidget(self.label_7)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_9.addWidget(self.label_8)
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setObjectName("label_9")
        self.label_9.setStyleSheet("color: rgb(194, 11, 200);")
        self.label_9.setFont(font)
        self.horizontalLayout_9.addWidget(self.label_9)
        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.verticalLayout_4.addWidget(self.frame)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSpacing(7)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setEnabled(True)
        self.label_12.setFont(font)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(6)
        sizePolicy.setHeightForWidth(self.label_12.sizePolicy().hasHeightForWidth())
        self.label_12.setSizePolicy(sizePolicy)
        self.label_12.setFont(font)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_10.addWidget(self.label_12)
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setWordWrap(False)
        self.label_13.setObjectName("label_13")
        self.label_13.setStyleSheet("color: rgb(194, 11, 200);")
        self.label_13.setFont(font)
        self.label_13.setSizePolicy(sizePolicy)
        self.horizontalLayout_10.addWidget(self.label_13)
        self.horizontalLayout.addLayout(self.horizontalLayout_10)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setEnabled(False)
        self.horizontalLayout.addWidget(self.pushButton)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSpacing(7)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_11.addWidget(self.label_10)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.label_11.setStyleSheet("color: rgb(194, 11, 200);")
        self.label_11.setFont(font)
        self.label_11.setSizePolicy(sizePolicy)
        self.horizontalLayout_11.addWidget(self.label_11)
        self.horizontalLayout.addLayout(self.horizontalLayout_11)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(30)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(32)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.radioButton_1 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_1.setEnabled(False)
        self.radioButton_1.setFont(font)
        self.radioButton_1.setObjectName("radioButton_1")
        self.horizontalLayout_4.addWidget(self.radioButton_1)
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setEnabled(False)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_4.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_3.setEnabled(False)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_4.addWidget(self.radioButton_3)
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_4.setEnabled(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_4.setFont(font)
        self.horizontalLayout_4.addWidget(self.radioButton_4)
        self.verticalLayout_3.addLayout(self.horizontalLayout_4)
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.listWidget_2.setStyleSheet("background-color: rgb(5, 189, 255);")
        self.listWidget_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setMouseTracking(True)
        self.listWidget_2.setSpacing(5)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget_2.setFont(font)
        self.verticalLayout_3.addWidget(self.listWidget_2)
        self.horizontalLayout_2.addWidget(self.frame_3)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_14.sizePolicy().hasHeightForWidth())
        self.label_14.setSizePolicy(sizePolicy)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_2.addWidget(self.label_14)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSpacing(19)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_15 = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_15.sizePolicy().hasHeightForWidth())
        self.label_15.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_5.addWidget(self.label_15)
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setObjectName("label_16")
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet("color: rgb(194, 11, 200);")
        self.horizontalLayout_5.addWidget(self.label_16)
        self.progressBar = QtWidgets.QProgressBar(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.progressBar.setFont(font)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setToolTip("")
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setMaximum(11)
        self.progressBar.setProperty("value", 0) 
        self.progressBar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_5.addWidget(self.progressBar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet("background-color: rgb(5, 189, 255);")
        self.listWidget.setMouseTracking(True)
        self.listWidget.setSpacing(5)
        font = QtGui.QFont()
        font.setFamily("Copperplate Gothic Bold")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.listWidget.setFont(font)
        self.verticalLayout_2.addWidget(self.listWidget)
        self.horizontalLayout_2.addWidget(self.frame_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.frame.raise_()
        self.frame_2.raise_()
        self.frame_3.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_11.raise_()
        self.frame_3.raise_()
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 895, 26))
        self.menubar.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        self.menuHelp= QtWidgets.QMenu(self.menubar)
        self.menuHelp.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionIntroduction = QtWidgets.QAction(MainWindow)
        self.actionIntroduction.setObjectName("actionIntroduction")
        self.actionManaging_your_Team = QtWidgets.QAction(MainWindow)
        self.actionManaging_your_Team.setObjectName("actionManaging_your_Team")
        self.actionFantasy_Cricket_Point_System = QtWidgets.QAction(MainWindow)
        self.actionFantasy_Cricket_Point_System.setObjectName("actionFantasy_Cricket_Point_System")
        
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuHelp.addAction(self.actionIntroduction)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionManaging_your_Team)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionFantasy_Cricket_Point_System)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.actionNEW_Team.triggered.connect(self.addNewTeam)
        self.actionOPEN_Team.triggered.connect(self.openExistingTeam)
        self.actionSAVE_Team.triggered.connect(self.saveTeam)
        self.actionEVALUATE_Team.triggered.connect(self.evaluateTeam)
        self.actionIntroduction.triggered.connect(self.displayIntroduction)
        self.actionManaging_your_Team.triggered.connect(self.displayHowtoPlay)
        self.actionFantasy_Cricket_Point_System.triggered.connect(self.displayPointSystem)

        
        self.radioButton_1.clicked.connect(partial(self.createplayerlist,"BAT"))
        self.radioButton_2.clicked.connect(partial(self.createplayerlist,"BWL"))
        self.radioButton_3.clicked.connect(partial(self.createplayerlist,"AR"))
        self.radioButton_4.clicked.connect(partial(self.createplayerlist,"WK"))

        self.listWidget_2.itemDoubleClicked.connect(self.addNewPlayer)
        self.listWidget_2.itemEntered.connect(self.showPlayerStats)
        self.listWidget.itemEntered.connect(self.showPlayerStats)
        self.listWidget.itemDoubleClicked.connect(self.removePlayerAdded)

        self.pushButton.clicked.connect(self.displayTeamPreview)
      
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.label_3.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "Bowlers (BWL)"))
        self.label_5.setText(_translate("MainWindow", "##"))
        self.label_6.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label_7.setText(_translate("MainWindow", "##"))
        self.label_8.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label_9.setText(_translate("MainWindow", "##"))
        self.label_12.setText(_translate("MainWindow", "Points Available"))
        self.label_13.setText(_translate("MainWindow", "####"))
        self.label_10.setText(_translate("MainWindow", "Points used"))
        self.label_11.setText(_translate("MainWindow", "####"))
        self.pushButton.setText(_translate("MainWindow", "Preview Team"))
        self.radioButton_1.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "BWL"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_14.setText(_translate("MainWindow", ">"))
        self.label_15.setText(_translate("MainWindow", "Team Name"))
        self.label_16.setText(_translate("MainWindow", "######"))
        self.progressBar.setFormat(_translate("MainWindow", "Players: %v/11"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionIntroduction.setText(_translate("MainWindow", "Introduction"))
        self.actionManaging_your_Team.setText(_translate("MainWindow", "How to Play"))
        self.actionFantasy_Cricket_Point_System.setText(_translate("MainWindow", "Fantasy Cricket Point System"))
        
#Function to display dialog which shows introduction about the Fantasy Cricket Game on clicking "Introduction" from help menu
    def displayIntroduction(self):
        msg = '''Fantasy Cricket is an online game where you create a virtual team of real cricket players and score points depending on how your chosen players perform in real life matches.

Fantasy Cricket is played by using your sport knowledge and skill. You can pick your own team made up of real players for Cricket.

Create your team within a maximum budget of 1000 credits. Your team earns points based on your chosen players' performance in the real-life matches. It's time to showcase your skill and go for glory!

 To win a tournament,  you must try and get the maximum points and the No. 1 rank amongst other participants.  '''
        self.showmessageBox(msg,"Information","Ok")

#Function to display a dialog which shows how to play the game on clicking "How to play" from help menu
    def displayHowtoPlay(self):
        msg = '''1. Create your Team
Click on 'NEW TEAM' for creating your own team

Select players for your Fantasy Cricket team from all 4 of the categories mentioned below:
BAT - Batsmen (Minimum 3 - Maximum 5 players)
BWL - Bowlers (Minimum 3 - Maximum 5 players)
AR - All-rounders (Minimum 2 - Maximum 3 players)
WK - Wicket-keeper (Only 1 player)

2. Save your Team
Click on 'SAVE TEAM' for saving your team

3. Open your existing Team
You can open an already created team by clicking 'OPEN TEAM' and update the player list.

4. Evaluate the team score
You can evaluate the score by selecting the team and match by clicking 'EVALUATE TEAM'
'''
        self.showmessageBox(msg,"Information","Ok")

#Function to display a dialog which shows fantasy point calculation on clicking "Fantasy Cricket Point System" from help menu
    def displayPointSystem(self):
        msg = '''Here’s how your team earns Fantasy points:

Batting 
● 1 point for 2 runs scored 
● Additional 5 points for half century 
● Additional 10 points for century 
● 2 points for strike rate (runs/balls faced) of 80-100 
● Additional 4 points for strike rate>100 
● 1 point for hitting a boundary (four) and 2 points for over boundary (six) 

Bowling 
● 10 points for each wicket 
● Additional 5 points for three wickets per innings 
● Additional 10 points for 5 wickets or more in innings 
● 4 points for economy rate between 3.5 and 4.5 
● 7  points for economy rate between 2 and 3.5 
● 10 points for economy rate less than 2 
● 10 points for each maiden overs
 
Fielding 
● 10 points each for catch/stumping/run out
'''
        self.showmessageBox(msg,"Information","Ok")

# Function to show the player stats as a tooltip
    def showPlayerStats(self,item):
        text_item = item.text()
        result_list = text_item.rsplit(' (')
        result = result_list[0]
        sql = "SELECT matches,runs,hundreds,fifties,image,ctg,wickets,stumping,catches FROM stats WHERE player = '"+str(result)+"';"
        Mycursor = self.connectDisconnectDatabase("connect")
        Mycursor.execute(sql)
        records = Mycursor.fetchall()
        Mycursor.close()
        self.connectDisconnectDatabase("disconnect")
        recordlist = list(sum(records,()))
        image = recordlist[4]
        ctg = recordlist[5]
        with open("imageToSave.jpg", "wb") as fh:
            fh.write(image)
        icon = QtGui.QIcon("imageToSave.jpg")
        if ctg == "BAT":
            msg = "Name: "+str(result)+"<br>Matches Played: "+str(recordlist[0])+"<br>Runs Scored: "+str(recordlist[1])+"<br>100's: "+str(recordlist[2])+"<br>50's: "+str(recordlist[3])+""
        elif ctg == "BWL":
            msg = "Name: "+str(result)+"<br>Matches Played: "+str(recordlist[0])+"<br>Wickets taken: "+str(recordlist[6])+""
        elif ctg == "AR":
            msg = "Name: "+str(result)+"<br>Matches Played: "+str(recordlist[0])+"<br>Runs Scored: "+str(recordlist[1])+"<br>Wickets taken: "+str(recordlist[6])+""
        elif ctg == "WK":
            msg = "Name: "+str(result)+"<br>Matches Played: "+str(recordlist[0])+"<br>Catches Taken: "+str(recordlist[8])+"<br>Stumping: "+str(recordlist[7])+""
        item.setToolTip('<b>%s</b><br><img src="%s">' % (msg, "imageToSave.jpg"))

# Function to display the preview of the team selection
    def displayTeamPreview(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui4 = Ui_Dialog_4()
        self.ui4.setupUi(self.Dialog)
        for player in self.selectedplayers[::3]:
            sql = "SELECT image,value,ctg FROM stats WHERE player = '"+str(player)+"';"
            Mycursor = self.connectDisconnectDatabase("connect")
            Mycursor.execute(sql)
            records = Mycursor.fetchall()
            self.connectDisconnectDatabase("disconnect")
            recordlist = list(sum(records,()))
            image = recordlist[0]
            value = recordlist[1]
            ctg = recordlist[2]
            name = str(player)
            with open("imageToPreview.jpg", "wb") as fh:
                fh.write(image)
            self.ui4.verticalLayout = QtWidgets.QVBoxLayout()
            self.ui4.verticalLayout.setObjectName("layout")
            self.ui4.label_6 = QtWidgets.QLabel(self.Dialog)
            self.ui4.label_5 = QtWidgets.QLabel(self.Dialog)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
            sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
            self.ui4.label_6.setSizePolicy(sizePolicy)
            self.ui4.label_5.setSizePolicy(sizePolicy)
            self.ui4.label_6.setMaximumSize(QtCore.QSize(60, 60))
            self.ui4.label_5.setMaximumSize(QtCore.QSize(200, 200))
            self.ui4.label_6.setPixmap(QtGui.QPixmap("imageToPreview.jpg"))
            self.ui4.label_6.setScaledContents(True)
            self.ui4.label_5.setText(""+str(name)+"<br>Points: "+str(value)+"")
            self.ui4.verticalLayout.addWidget(self.ui4.label_6, 0, QtCore.Qt.AlignHCenter)
            self.ui4.verticalLayout.addWidget(self.ui4.label_5, 0, QtCore.Qt.AlignHCenter)
            if ctg == "WK":
                self.ui4.horizontalLayout_1.addLayout(self.ui4.verticalLayout)
            elif ctg == "BAT":
                self.ui4.horizontalLayout_2.addLayout(self.ui4.verticalLayout)
            elif ctg == "AR":
                self.ui4.horizontalLayout_3.addLayout(self.ui4.verticalLayout)
            elif ctg == "BWL":
                self.ui4.horizontalLayout_4.addLayout(self.ui4.verticalLayout)
            
        self.Dialog.exec()
        
# Function to add new team on clicking "NEW Team" from "Manage Teams" Menu       
    def addNewTeam(self):
        msg = '''1. Create your team with a name and Pick 11 players within 1000 credits. Keep an eye on the progress bar.

2. Create a balanced Team. Use your skills to pick players from all roles.
   Pick Minimum 3 to Maximum 5 Batsman
   Pick Minimum 3 to Maximum 5 Bowlers
   Pick Minimum 2 to Maximum 3 All-rounders
   Pick only 1 Wicket-keeper
   
3. Save your Team and evaluate the score

    Press 'OK' to continue'''
        self.showmessageBox(msg,"Information","Ok")
        ok_pressed = self.showDialogNewTeamName()
        if ok_pressed:
            self.enableHomepage()
            self.createplayerlist("BAT")
            
# Function to open an already created team on clicking "OPEN Team" from "Manage Teams" Menu  
    def openExistingTeam(self):
        team_name = self.showDialogOpenTeam()
        if team_name != 0:
            self.enableHomepage()
            font = QtGui.QFont()
            font.setFamily("Times New Roman")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.label_16.setText(team_name)
            self.label_16.setFont(font)
            sql = "SELECT players FROM teams WHERE name = '"+team_name+"';"
            Mycursor = self.connectDisconnectDatabase("connect")
            Mycursor.execute(sql)
            records = Mycursor.fetchall()
            Mycursor.close()
            self.connectDisconnectDatabase("disconnect")
            records = list(sum(records,()))
            for player in records:
                if player in self.batsman_record:
                    self.batsman_record = self.updateleftlistOnitemclick(self.batsman_record,player,"BAT")
                    self.label_3.setNum(int(self.label_3.text()) + 1)
                elif player in self.bowlers_record:
                    self.bowlers_record = self.updateleftlistOnitemclick(self.bowlers_record,player,"BWL")
                    self.label_5.setNum(int(self.label_5.text()) + 1)
                elif player in self.allrounders_record:
                    self.allrounders_record = self.updateleftlistOnitemclick(self.allrounders_record,player,"AR")
                    self.label_7.setNum(int(self.label_7.text()) + 1)
                elif player in self.wicketkeepers_record:
                    self.wicketkeepers_record = self.updateleftlistOnitemclick(self.wicketkeepers_record,player,"WK")
                    self.label_9.setNum(int(self.label_9.text()) + 1)
            self.createplayerlist("BAT")
            total_players = int(self.label_3.text())+int(self.label_5.text())+int(self.label_7.text())+int(self.label_9.text())
            self.progressBar.setProperty("value", total_players)

# Function to save the new team or update the already created team on clicking "SAVE Team" from "Manage Teams" Menu         
    def saveTeam(self):
        team_name = self.label_16.text()
        if team_name != "######":
            if len(self.selectedplayers)/3 == 11:
                Mycursor = self.connectDisconnectDatabase("connect")
                sql = "SELECT players FROM teams WHERE name = '"+team_name+"';"
                Mycursor.execute(sql)
                records = Mycursor.fetchall()
                if records == []:
                    # Inserting the team details to the database as new team
                    for row in self.selectedplayers[::3]:
                        Mycursor.execute('''INSERT INTO teams(name,players) VALUES (?,?);''',(team_name,row))
                    Mycursor.close()
                    button_pressed = self.showmessageBox("Your team "+team_name+" created Successfully","Information","Ok")
                else:
                    # Updating the team table with changed player list
                    Mycursor.execute('''DELETE FROM teams WHERE name = "'''+team_name+'''";''')
                    for row in self.selectedplayers[::3]:
                        Mycursor.execute('''INSERT INTO teams(name,players) VALUES (?,?);''',(team_name,row))
                    Mycursor.close()
                    button_pressed = self.showmessageBox("Your team "+team_name+" updated Successfully","Information","Ok")
                self.connectDisconnectDatabase("disconnect")
                self.disableHomepage()
            else:
                button_pressed = self.showmessageBox("Select all 11 players before saving your team ","Critical","Ok")
        else:
            button_pressed = self.showmessageBox("Create your team before saving...","Warning","Ok")
            
# Function to evaluate the fantasyn points for the team on clicking "EVALUATE Team" from "Manage Teams" Menu            
    def evaluateTeam(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui3 = Ui_Dialog_3()
        self.ui3.setupUi(self.Dialog)
        sql = "SELECT DISTINCT name FROM teams;"
        Mycursor = self.connectDisconnectDatabase("connect")
        Mycursor.execute(sql)
        records = Mycursor.fetchall()
        self.connectDisconnectDatabase("disconnect")
        if records == []:
            self.showmessageBox("No Teams created. Please create team first...","Information")
            return 0
        else:
            recordlist = list(sum(records,()))
            matchlist = ['Match1','Match2','Match3','Match4','Match5']
            self.ui3.comboBox_2.addItems(recordlist)
            self.ui3.comboBox.addItems(matchlist)
            self.Dialog.show()
            result = self.Dialog.exec()
            if result == 1:
                team_name = str(self.ui3.comboBox_2.currentText())
                Mycursor = self.connectDisconnectDatabase("connect")
                sql = "SELECT players FROM teams WHERE name = '"+team_name+"';"
                Mycursor.execute(sql)
                records = Mycursor.fetchall()
                Mycursor.close()
                records = list(sum(records,()))
                for row in records:
                    self.ui3.listWidget_2.addItem(row)
                point_list = self.evaluatePoints(records,team_name)
                final_score = 0
                for row in point_list:
                    final_score = final_score+row
                    self.ui3.listWidget.addItem(str(row))
                self.ui3.label_3.setText("Points  "+ str(final_score))
                self.ui3.pushButton.setEnabled(False)
                self.ui3.comboBox_2.setEnabled(False)
                self.ui3.comboBox.setEnabled(False)
                self.Dialog.exec()
                
    
# Function to enable the widgets and clear the data on the home page       
    def enableHomepage(self):
        self.label_13.setNum(1000)
        self.label_11.setNum(0)
        self.label_3.setNum(0)
        self.label_5.setNum(0)
        self.label_7.setNum(0)
        self.label_9.setNum(0)

        self.batsman_record = []
        self.bowlers_record = []
        self.allrounders_record = []
        self.wicketkeepers_record = []
        self.selectedplayers = []
        self.listWidget_2.clear()
        self.listWidget.clear()
         
        self.radioButton_1.setEnabled(True)
        self.radioButton_2.setEnabled(True)
        self.radioButton_3.setEnabled(True)
        self.radioButton_4.setEnabled(True)
        self.radioButton_1.setChecked(True)
        self.pushButton.setEnabled(True)

        self.batsman_record = list(sum(self.fetchplayerdatafromdb("BAT"),()))
        self.bowlers_record = list(sum(self.fetchplayerdatafromdb("BWL"),()))
        self.allrounders_record = list(sum(self.fetchplayerdatafromdb("AR"),()))
        self.wicketkeepers_record = list(sum(self.fetchplayerdatafromdb("WK"),()))
        
# Function to disable the widgets and set the default data on the home page 
    def disableHomepage(self):
        self.batsman_record = []
        self.bowlers_record = []
        self.allrounders_record = []
        self.wicketkeepers_record = []
        self.selectedplayers = []
        self.listWidget_2.clear()
        self.listWidget.clear()     
        self.label_13.setText("####")
        self.label_11.setText("####")
        self.label_16.setText("######")
        self.label_3.setText("##")
        self.label_5.setText("##")
        self.label_7.setText("##")
        self.label_9.setText("##")
        self.radioButton_1.setChecked(False)
        self.radioButton_1.setEnabled(False)
        self.radioButton_2.setEnabled(False)
        self.radioButton_3.setEnabled(False)
        self.radioButton_4.setEnabled(False)
        self.pushButton.setChecked(False)

# Fumction to add/delete the player to/from list on double clicking player name
    def createplayerlist(self,ctg):
        index = 1
        if ctg=="BAT":
            self.listWidget_2.clear()
            for row in self.batsman_record[::3]:
                self.listWidget_2.addItem(row+" (Points: "+str(self.batsman_record[index])+")")
                index = index+3
        elif ctg=="BWL":
            self.listWidget_2.clear()
            for row in self.bowlers_record[::3]:
                self.listWidget_2.addItem(row+" (Points: "+str(self.bowlers_record[index])+")")
                index = index+3
        elif ctg=="AR":
            self.listWidget_2.clear()
            for row in self.allrounders_record[::3]:
                self.listWidget_2.addItem(row+" (Points: "+str(self.allrounders_record[index])+")")
                index = index+3
        elif ctg=="WK":
            self.listWidget_2.clear()
            for row in self.wicketkeepers_record[::3]:
                self.listWidget_2.addItem(row+" (Points: "+str(self.wicketkeepers_record[index])+")")
                index = index+3
        elif ctg=="PLAYERS":
            self.listWidget.clear()
            for row in self.selectedplayers[::3]:
                self.listWidget.addItem(row+" (Points: "+str(self.selectedplayers[index])+")")
                index = index+3
                
 # Fumction to add the player to the team created on double clicking player name from the left side list  
    def addNewPlayer(self,item):
        text_item = item.text()
        result_list = text_item.rsplit(' (')
        result = result_list[0]
        if self.radioButton_1.isChecked():
            check_result = self.checkplayersnumber("BAT")
            if check_result == 1:
                self.batsman_record = self.updateleftlistOnitemclick(self.batsman_record,result,"BAT")
                self.label_3.setNum(self.selectedplayers.count("BAT"))  
        elif self.radioButton_2.isChecked():
            check_result = self.checkplayersnumber("BWL")
            if check_result == 1:
                self.bowlers_record = self.updateleftlistOnitemclick(self.bowlers_record,result,"BWL")
                self.label_5.setNum(self.selectedplayers.count("BWL"))
        elif self.radioButton_3.isChecked():
            check_result = self.checkplayersnumber("AR")
            if check_result == 1:
                self.allrounders_record = self.updateleftlistOnitemclick(self.allrounders_record,result,"AR")
                self.label_7.setNum(self.selectedplayers.count("AR"))
        elif self.radioButton_4.isChecked():
            check_result = self.checkplayersnumber("WK")
            if check_result == 1:
                self.wicketkeepers_record = self.updateleftlistOnitemclick(self.wicketkeepers_record,result,"WK")
                self.label_9.setNum(self.selectedplayers.count("WK"))
        total_players = int(self.selectedplayers.count("BAT"))+int(self.selectedplayers.count("BWL"))+int(self.selectedplayers.count("AR"))+ int(self.selectedplayers.count("WK"))
        self.progressBar.setProperty("value", total_players) # Updating the progress bar
        if check_result == 1:
            if len(self.selectedplayers)/3 == 11:  
                    button_pressed = self.showmessageBox("Are you done with your team selection.Do you want to save the team?","Question","SaveCancel")
                    if button_pressed == QMessageBox.Save:  
                        self.saveTeam()
                        
 # Fumction to delete the player from the team created on double clicking player name from the right side list                
    def removePlayerAdded(self,item):
        text_item = item.text()
        result_list = text_item.rsplit(' (')
        result = result_list[0]
        item_index = self.selectedplayers.index(result)
        if self.selectedplayers[item_index+2] == "BAT":
            self.radioButton_1.setChecked(True)
            self.batsman_record = self.updaterightlistOnitemclick(self.batsman_record,item_index,"BAT")
            self.label_3.setNum(int(self.label_3.text()) - 1)  
        elif self.selectedplayers[item_index+2] == "BWL":
            self.radioButton_2.setChecked(True)
            self.bowlers_record = self.updaterightlistOnitemclick(self.bowlers_record,item_index,"BWL")
            self.label_5.setNum(int(self.label_5.text()) - 1)
        elif self.selectedplayers[item_index+2] == "AR":
            self.radioButton_3.setChecked(True)
            self.allrounders_record = self.updaterightlistOnitemclick(self.allrounders_record,item_index,"AR")
            self.label_7.setNum(int(self.label_7.text()) - 1)
        elif self.selectedplayers[item_index+2] == "WK":
            self.radioButton_4.setChecked(True)
            self.wicketkeepers_record = self.updaterightlistOnitemclick(self.wicketkeepers_record,item_index,"WK")
            self.label_9.setNum(int(self.label_9.text()) - 1)
        total_players = int(self.label_3.text())+int(self.label_5.text())+int(self.label_7.text())+int(self.label_9.text())
        self.progressBar.setProperty("value", total_players)
        
 # Fumction to update the left list by removing the clicked player name and adding it to right                                                                                                
    def updateleftlistOnitemclick(self,player_record,item_selected,ctg):
        item_index = player_record.index(item_selected)
        points_available = int(self.label_13.text())
        points_used = int(self.label_11.text())
        if (points_available - int(player_record[item_index+1])) <=0:
            button_pressed = self.showmessageBox("You don't have enough points to add the player","Critical")
        else:
            # Updating the points available and points used accordingly
            self.label_13.setNum(points_available - int(player_record[item_index+1]))
            self.label_11.setNum(points_used + int(player_record[item_index+1]))
            # Adding player to the selection list
            self.selectedplayers.append(player_record[item_index])
            self.selectedplayers.append(player_record[item_index+1])
            self.selectedplayers.append(player_record[item_index+2])
            # Deleting the player from the player list
            del player_record[item_index+2]
            del player_record[item_index+1]
            del player_record[item_index]
            self.createplayerlist(ctg)
            self.createplayerlist("PLAYERS")           
        return player_record

 # Fumction to update the right list by removing the clicked player name and adding it back to left
    def updaterightlistOnitemclick(self,player_record,item_index,ctg):
        # Adding player back to the player list
        player_record.append(self.selectedplayers[item_index])
        player_record.append(self.selectedplayers[item_index+1])
        player_record.append(self.selectedplayers[item_index+2])
        points_available = int(self.label_13.text()) 
        points_used = int(self.label_11.text())
        # Updating the points available and points used accordingly
        self.label_13.setNum(points_available + int(self.selectedplayers[item_index+1])) 
        self.label_11.setNum(points_used - int(self.selectedplayers[item_index+1]))
        # Deleting the player from the selection list
        del self.selectedplayers[item_index+2]
        del self.selectedplayers[item_index+1] 
        del self.selectedplayers[item_index]
        self.createplayerlist(ctg)
        self.createplayerlist("PLAYERS")
        return player_record

 # Fumction to fetch players stats from database and return the result
    def fetchplayerdatafromdb(self,category):
        sql = "SELECT player,value,ctg FROM stats WHERE ctg = '"+category+"';"
        Mycursor = self.connectDisconnectDatabase("connect")
        Mycursor.execute(sql)
        records = Mycursor.fetchall()
        Mycursor.close()
        self.connectDisconnectDatabase("disconnect")
        return records
    
 # Fumction to check whether the no: of players requirement is satisfied or not and to display appropriate error messages
    def checkplayersnumber(self,ctg):
        batsman_count = int(self.label_3.text())
        bowlers_count = int(self.label_5.text())
        allrounders_count = int(self.label_7.text())
        wicketkeepers_count = int(self.label_9.text())
        balance_player = 11 -(batsman_count+bowlers_count+allrounders_count+wicketkeepers_count)
        result = 1
        if balance_player == 0:
            self.showmessageBox("You cannot pick more than 11 players","Critical") # Display error when no: of players selected is greater then 11
            result = 0
        else:
            if ctg == "BAT":
                if batsman_count == 5:
                    self.showmessageBox("You can only select upto 5 Batsman","Information") # Display error when more than 5 batsman is added
                    result = 0
                else:
                    # Checking that enough no: of slot is available for adding remaining players other than batsman
                    if bowlers_count < 3 and balance_player == (3 - bowlers_count):
                        self.showmessageBox("Please select atleast 3 Bowlers","Warning") 
                        result = 0
                    elif allrounders_count < 2 and balance_player == (2 - allrounders_count):
                        self.showmessageBox("Please select atleast 2 All-rounders","Warning")
                        result = 0
                    elif wicketkeepers_count < 1 and balance_player == (1 - wicketkeepers_count):
                        self.showmessageBox("Please select atleast 1 Wicketkeeper","Warning")
                        result = 0
            elif ctg == "BWL":
                if bowlers_count == 5:
                    self.showmessageBox("You can only select upto 5 Bowlers","Information") # Display error when more than 5 bowlers is added
                    result = 0
                else:
                    # Checking that enough no: of slot is available for adding remaining players other than bowlers
                    if batsman_count < 3 and balance_player == (3 - batsman_count):
                        self.showmessageBox("Please select atleast 3 Batsman","Warning")
                        result = 0
                    elif allrounders_count < 2 and balance_player == (2 - allrounders_count):
                        self.showmessageBox("Please select atleast 2 All-rounders","Warning")
                        result = 0
                    elif wicketkeepers_count < 1 and balance_player == (1 - wicketkeepers_count):
                        self.showmessageBox("Please select atleast 1 Wicketkeeper","Warning")
                        result = 0
            elif ctg == "AR":
                if allrounders_count == 3:
                    self.showmessageBox("You can only select upto 3 All-rounders","Information") # Display error when more than 3 all-rounders is added
                    result = 0
                else:
                    # Checking that enough no: of slot is available for adding remaining players other than all-rounders
                    if batsman_count < 3 and balance_player == (3 - batsman_count):
                        self.showmessageBox("Please select atleast 3 Batsman","Warning")
                        result = 0
                    elif bowlers_count < 3 and balance_player == (3 - bowlers_count):
                        self.showmessageBox("Please select atleast 3 Bowlers","Warning")
                        result = 0
                    elif wicketkeepers_count < 1 and balance_player == (1 - wicketkeepers_count):
                        self.showmessageBox("Please select atleast 1 Wicketkeeper","Warning")
                        result = 0
            elif ctg == "WK":
                if wicketkeepers_count == 1:
                    self.showmessageBox("You can only select 1 Wicket-keeper","Information") # Display error when more than 1 wicket keeper is added
                    result = 0
                else:
                    # Checking that enough no: of slot is available for adding remaining players other than wicket-keeper
                    if batsman_count < 3 and balance_player == (3 - batsman_count):
                        self.showmessageBox("Please select atleast 3 Batsman","Warning")
                        result = 0
                    elif bowlers_count < 3 and balance_player == (3 - bowlers_count):
                        self.showmessageBox("Please select atleast 3 Bowlers","Warning")
                        result = 0
                    elif allrounders_count < 2 and balance_player == (2 - allrounders_count):
                        self.showmessageBox("Please select atleast 2 All-rounders","Warning")
                        result = 0
        return result
                    

# Function to display a custom dialog asking for the new team name
    def showDialogNewTeamName(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui = Ui_Dialog_1()
        self.ui.setupUi(self.Dialog)
        self.Dialog.show()
        result = self.Dialog.exec_()  
        team_name = self.ui.lineEdit.text()
        if result == 1 and team_name == "":
            button_pressed = self.showmessageBox("Team name can't be empty","Critical") # Display error if team name is blank and ok pressed
            self.showDialogNewTeamName()
            return result
        elif result == 1 and team_name != "":
            sql = "SELECT * FROM teams where name='"+team_name+"';"
            Mycursor = self.connectDisconnectDatabase("connect")
            Mycursor.execute(sql)
            records = Mycursor.fetchall()
            self.connectDisconnectDatabase("disconnect")
            if records != []:
                button_pressed = self.showmessageBox("Team Name Already exists. Please select another name...","Warning") # Display warning if team name already exists
                self.showDialogNewTeamName()
            else:
                font = QtGui.QFont()
                font.setFamily("Times New Roman")
                font.setPointSize(12)
                font.setBold(True)
                font.setWeight(75)
                self.label_16.setText(team_name)
                self.label_16.setFont(font)
            return result
        elif result==0:
            return result
        
# Function to display a custom dialog showing the already created name and ask for team name to open      
    def showDialogOpenTeam(self):
        self.Dialog = QtWidgets.QDialog()
        self.ui2 = Ui_Dialog_2()
        self.ui2.setupUi(self.Dialog)
        sql = "SELECT DISTINCT name FROM teams;"
        Mycursor = self.connectDisconnectDatabase("connect")
        Mycursor.execute(sql)
        records = Mycursor.fetchall()
        self.connectDisconnectDatabase("disconnect")
        if records == []:
            self.showmessageBox("No Teams created. Please create team first...","Information") # display Error message for trying to open team with no team created yet.
            return 0
        else:
            recordlist = list(sum(records,()))
            self.ui2.comboBox.addItems(recordlist)
            self.Dialog.show()
            result = self.Dialog.exec_()
            if result == 1:
                selected_team = str(self.ui2.comboBox.currentText())
                return selected_team
            else:
                return 0
            
# Function to evaluate the final score from the player performance
    def evaluatePoints(self,player_records,team):
        point_list = []
        total_points = 0
        Mycursor = self.connectDisconnectDatabase("connect")
        for player in player_records:
            # Fetching each player match details from databnse and saving to separate variables for evaluation
            sql = "SELECT scored,faced,fours,sixes,bowled,maiden,given,wkts,catches,stumping,runout FROM match_details WHERE player = '"+player+"';"
            Mycursor.execute(sql)
            records = list(sum(Mycursor.fetchall(),()))
            runs_scored,balls_faced,fours,sixes = [records[i] for i in (0, 1, 2, 3)]
            bowled,maiden,given,wkts = [records[i] for i in (4, 5, 6, 7)]
            catches,stumping,runout = [records[i] for i in (8, 9, 10)]

            # Calculating the points from batting perfomance
            total_points = int(runs_scored/2) + (fours*1) + (sixes*2)
            if runs_scored > 50:
                total_points = total_points + 5
            if runs_scored > 100:
                total_points = total_points + 10
            if balls_faced != 0:
                strike_rate = (runs_scored/balls_faced)
                if strike_rate >= 80:
                    total_points = total_points + 2
                if strike_rate > 100:
                    total_points = total_points + 4
                    
            # Calculating the points from bowling perfomance        
            total_points = total_points + (wkts*10)
            if wkts >= 3:
                total_points = total_points + 5
            if wkts >= 5:
                total_points = total_points + 10
            if bowled != 0:
                economy_rate = given/(bowled/6)
                if (economy_rate >= 3.5) and (economy_rate <= 4.5):
                    total_points = total_points + 4
                elif (economy_rate >= 2) and (economy_rate < 3.5):
                    total_points = total_points + 7
                elif (economy_rate < 2):
                    total_points = total_points + 10
            total_points = total_points + (10*maiden)

            # Calculating the points from fielding perfomance
            total_points = total_points + (10*catches) + (10*stumping) + (10*runout)
            point_list.append(total_points)
            total_points = str(total_points)

            # Updating the teams table with the points calculated for each player in the team list
            sql = "UPDATE teams SET value = '"+total_points+"' WHERE name = '"+team+"' and players = '"+player+"';" 
            Mycursor.execute(sql)
        Mycursor = self.connectDisconnectDatabase("disconnect")
        return point_list

# Function to open/close the connection to database   
    def connectDisconnectDatabase(self,action):
        if action == "connect":
            self.connection = None
            try:
                self.connection = sqlite3.connect("Fantasy_Cricket.db") # Connecting to the database
                Mycursor = self.connection.cursor()
                return Mycursor
            except Exception:
                print("Connection to database failed")
                button_pressed = self.showmessageBox("Team creation Failed","Warning","Ok")
        elif action == "disconnect":
                    self.connection.commit()
                    self.connection.close()    #Close the database connection 

# Function to display the message box with appropriate messages   
    def showmessageBox(self,msg,icon,buttonlist=""):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Fantasy Cricket")
        msgBox.setText(msg)
        if icon == "Critical":
            msgBox.setIcon(QMessageBox.Critical)
        elif icon == "Question":
            msgBox.setIcon(QMessageBox.Question)
        elif icon == "Information":
            msgBox.setIcon(QMessageBox.Information)
        elif icon == "Warning":
            msgBox.setIcon(QMessageBox.Warning)
        if buttonlist == "Ok":
            msgBox.setStandardButtons(QMessageBox.Ok)
        if buttonlist == "YesNo":
            msgBox.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        if buttonlist == "OkCancel":
            msgBox.setStandardButtons(QMessageBox.Ok|QMessageBox.Cancel)
        if buttonlist == "SaveCancel":
            msgBox.setStandardButtons(QMessageBox.Save|QMessageBox.Cancel)
        button_pressed = msgBox.exec_()
        return button_pressed

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


