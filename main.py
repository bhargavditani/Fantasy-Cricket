#Imported Modules / Files
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sqlite3
from newfilepopup import Ui_Form as newpopup
from openteam import Ui_Form as openteam
from evaluatescore import Ui_Form as evaluatescore


class Ui_CricketGame(object):
    def __init__(self):
        #Setting New File Dialog
        self.newDialog = QtWidgets.QMainWindow()
        self.new_screen = newpopup()
        self.new_screen.setupUi(self.newDialog)

        #Setting Open File Dialog
        self.openDialog = QtWidgets.QMainWindow()
        self.open_screen = openteam()
        self.open_screen.setupUi(self.openDialog)

        #Setting Evaluate Dialog
        self.evaluateDialog = QtWidgets.QMainWindow()
        self.evaluate_screen = evaluatescore()
        self.evaluate_screen.setupUi(self.evaluateDialog)



    def setupUi(self, CricketGame):

        #Total Variables used
        self.batsmancount = 0
        self.wkeepercount = 0
        self.arcount = 0
        self.ballcount = 0
        self.avail = 1000
        self.ptsused = 0
        self.totalcount = 0
        self.listwidget = 0
        self.x = 0
        self.items = []
        self.totalbatsman = []
        self.totalbowler = []
        self.totalallrounder = []
        self.totalwicketkeeper = []
        self.teamscore = []
        self.flag = 0

        #Setting Up all Dialog
        self.get_all()
        self.set_all()

        #Setting UI
        CricketGame.setObjectName("CricketGame")
        CricketGame.resize(823, 600)
        self.centralwidget = QtWidgets.QWidget(CricketGame)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(40, 60, 769, 81))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        #Batsmen Label
        self.batsmen = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batsmen.setFont(font)
        self.batsmen.setAutoFillBackground(False)
        self.batsmen.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.batsmen.setObjectName("batsmen")
        self.horizontalLayout_2.addWidget(self.batsmen)

        #Batsmen Count Label
        self.bat_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bat_count.setFont(font)
        self.bat_count.setObjectName("bat_count")
        self.horizontalLayout_2.addWidget(self.bat_count)

        #Bowlers Label
        self.bowlers = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bowlers.setFont(font)
        self.bowlers.setObjectName("bowlers")
        self.horizontalLayout_2.addWidget(self.bowlers)

        #Bowler Count Label
        self.bow_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bow_count.setFont(font)
        self.bow_count.setObjectName("bow_count")
        self.horizontalLayout_2.addWidget(self.bow_count)

        #Wicket-Keeper Label
        self.wicketkeeper = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wicketkeeper.setFont(font)
        self.wicketkeeper.setObjectName("wicketkeeper")
        self.horizontalLayout_2.addWidget(self.wicketkeeper)

        #Wicket-keeper Count Label
        self.wk_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wk_count.setFont(font)
        self.wk_count.setObjectName("wk_count")
        self.horizontalLayout_2.addWidget(self.wk_count)

        #AllRounder Label
        self.allrounder = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.allrounder.setFont(font)
        self.allrounder.setObjectName("allrounder")
        self.horizontalLayout_2.addWidget(self.allrounder)

        #AllRounder Count Label
        self.ar_count = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ar_count.setFont(font)
        self.ar_count.setObjectName("ar_count")
        self.horizontalLayout_2.addWidget(self.ar_count)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 160, 771, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        #Points Available Label
        self.pts_avail = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pts_avail.setFont(font)
        self.pts_avail.setObjectName("pts_avail")
        self.horizontalLayout.addWidget(self.pts_avail)

        #Points Available Count Label
        self.pts_avail_count = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.pts_avail_count.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pts_avail_count.setFont(font)
        self.pts_avail_count.setObjectName("pts_avail_count")
        self.horizontalLayout.addWidget(self.pts_avail_count)

        #Points Count Label
        self.pts_used = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pts_used.setFont(font)
        self.pts_used.setObjectName("pts_used")
        self.horizontalLayout.addWidget(self.pts_used)
        self.pts_used_count = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pts_used_count.setFont(font)
        self.pts_used_count.setObjectName("pts_used_count")
        self.horizontalLayout.addWidget(self.pts_used_count)

        #Current Player List Widget
        self.current_player = QtWidgets.QListWidget(self.centralwidget)
        self.current_player.setGeometry(QtCore.QRect(40, 250, 311, 291))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.current_player.setFont(font)
        self.current_player.setObjectName("current_player")

        #Select Player List Widget
        self.selected_player = QtWidgets.QListWidget(self.centralwidget)
        self.selected_player.setGeometry(QtCore.QRect(420, 250, 321, 291))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.selected_player.setFont(font)
        self.selected_player.setObjectName("selected_player")

        #Arrow Label (>)
        self.arrow = QtWidgets.QLabel(self.centralwidget)
        self.arrow.setGeometry(QtCore.QRect(380, 390, 21, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.arrow.setFont(font)
        self.arrow.setObjectName("arrow")

        #Batsman Radio Button
        self.bat_button = QtWidgets.QRadioButton(self.centralwidget)
        self.bat_button.setGeometry(QtCore.QRect(60, 220, 51, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bat_button.setFont(font)
        self.bat_button.setObjectName("bat_button")

        #Bowler Radio Button
        self.bow_button = QtWidgets.QRadioButton(self.centralwidget)
        self.bow_button.setGeometry(QtCore.QRect(120, 220, 61, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.bow_button.setFont(font)
        self.bow_button.setObjectName("bow_button")
        self.ar_button = QtWidgets.QRadioButton(self.centralwidget)

        #AllRounder Radio Button
        self.ar_button.setGeometry(QtCore.QRect(190, 220, 41, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.ar_button.setFont(font)
        self.ar_button.setObjectName("ar_button")

        #Wicket-Keeper Radio Button
        self.wk_button = QtWidgets.QRadioButton(self.centralwidget)
        self.wk_button.setGeometry(QtCore.QRect(240, 220, 61, 18))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.wk_button.setFont(font)
        self.wk_button.setObjectName("wk_button")

        #Show Team Name Label
        self.team_name = QtWidgets.QLabel(self.centralwidget)
        self.team_name.setGeometry(QtCore.QRect(430, 220, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.team_name.setFont(font)
        self.team_name.setObjectName("team_name")
        self.show_team_name = QtWidgets.QLabel(self.centralwidget)
        self.show_team_name.setGeometry(QtCore.QRect(523, 203, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.show_team_name.setFont(font)
        self.show_team_name.setText("")
        self.show_team_name.setObjectName("show_team_name")

        #Your Selection Label
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(40, 29, 111, 31))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.your_selection = QtWidgets.QLabel(self.gridLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.your_selection.setFont(font)
        self.your_selection.setScaledContents(False)
        self.your_selection.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.your_selection.setObjectName("your_selection")
        self.gridLayout.addWidget(self.your_selection, 0, 0, 1, 1)
        CricketGame.setCentralWidget(self.centralwidget)

        #Status Bar Defining
        self.statusbar = QtWidgets.QStatusBar(CricketGame)
        self.statusbar.setObjectName("statusbar")
        CricketGame.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(CricketGame)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 823, 25))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        CricketGame.setMenuBar(self.menubar)
        self.actionNEW_Team = QtWidgets.QAction(CricketGame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.actionNEW_Team.setFont(font)
        self.actionNEW_Team.setObjectName("actionNEW_Team")

        #New File Triggered
        self.actionNEW_Team.triggered.connect(self.new_file)

        self.actionOPEN_Team = QtWidgets.QAction(CricketGame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.actionOPEN_Team.setFont(font)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")

        #Open Triggerred
        self.actionOPEN_Team.triggered.connect(self.open_file)

        self.actionSAVE_Team = QtWidgets.QAction(CricketGame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.actionSAVE_Team.setFont(font)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")

        #Save Triggered
        self.actionSAVE_Team.triggered.connect(self.save_file)

        self.actionEVALUATE_Team = QtWidgets.QAction(CricketGame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.actionEVALUATE_Team.setFont(font)
        self.actionEVALUATE_Team.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")

        #Evaluate Triggered
        self.actionEVALUATE_Team.triggered.connect(self.evaluate)

        self.actionQuit_Team = QtWidgets.QAction(CricketGame)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.actionQuit_Team.setFont(font)
        self.actionQuit_Team.setShortcutContext(QtCore.Qt.WidgetShortcut)
        self.actionQuit_Team.setObjectName("actionQuit_Team")

        #Quit Triggered
        self.actionQuit_Team.triggered.connect(self.quit)

        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menuManage_Teams.addSeparator()
        self.menuManage_Teams.addAction(self.actionQuit_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        #Connections Between Methods
        self.bat_button.clicked.connect(self.load_names)
        self.bow_button.clicked.connect(self.load_names)
        self.ar_button.clicked.connect(self.load_names)
        self.wk_button.clicked.connect(self.load_names)
        self.current_player.itemDoubleClicked.connect(self.remove_current_player)
        self.selected_player.itemDoubleClicked.connect(self.remove_selected_player)
        self.open_screen.ok_button.clicked.connect(self.open_my_team)
        self.new_screen.ok_button.clicked.connect(self.get_team_name)
        self.evaluate_screen.selectteam_combobox.activated.connect(self.player_evaluate)
        self.evaluate_screen.selectmatch_combobox.activated.connect(self.match_evaluate)
        self.evaluate_screen.calscore_button.clicked.connect(self.show_point)

        self.retranslateUi(CricketGame)
        QtCore.QMetaObject.connectSlotsByName(CricketGame)

    def retranslateUi(self, CricketGame):

        _translate = QtCore.QCoreApplication.translate
        CricketGame.setWindowTitle(_translate("CricketGame", "Fantasy Cricket"))
        self.batsmen.setText(_translate("CricketGame", "Batsmen (BAT)"))
        self.bat_count.setText(_translate("CricketGame", "0"))
        self.bowlers.setText(_translate("CricketGame", "Bowlers (BOW)"))
        self.bow_count.setText(_translate("CricketGame", "0"))
        self.wicketkeeper.setText(_translate("CricketGame", "Wicket-keeper (WK)"))
        self.wk_count.setText(_translate("CricketGame", "0"))
        self.allrounder.setText(_translate("CricketGame", "Allrounders (AR)"))
        self.ar_count.setText(_translate("CricketGame", "0"))
        self.pts_avail.setText(_translate("CricketGame", "Points Available"))
        self.pts_avail_count.setText(_translate("CricketGame", "1000"))
        self.pts_used.setText(_translate("CricketGame", "Points Used"))
        self.pts_used_count.setText(_translate("CricketGame", "0"))
        self.arrow.setText(_translate("CricketGame", ">"))
        self.bat_button.setText(_translate("CricketGame", "BAT"))
        self.bow_button.setText(_translate("CricketGame", "BOW"))
        self.ar_button.setText(_translate("CricketGame", "AR"))
        self.wk_button.setText(_translate("CricketGame", "WK"))
        self.team_name.setText(_translate("CricketGame", "Team Name"))
        self.show_team_name.setText(_translate("CricketGame", "--"))
        self.your_selection.setText(_translate("CricketGame", "Your Selections"))

        #Menu
        self.menuManage_Teams.setTitle(_translate("CricketGame", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("CricketGame", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("CricketGame", "Ctrl+N"))
        self.actionOPEN_Team.setText(_translate("CricketGame", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("CricketGame", "Ctrl+O"))
        self.actionSAVE_Team.setText(_translate("CricketGame", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("CricketGame", "Ctrl+S"))
        self.actionEVALUATE_Team.setText(_translate("CricketGame", "EVALUATE Team"))
        self.actionQuit_Team.setText(_translate("CricketGame", "Quit"))

    def get_all(self):
        Batsman = 'BAT'
        WicketKeeper = 'WK'
        Allrounder = 'AR'
        Bowler = 'BWL'

        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        sql1 = "SELECT player FROM stats WHERE ctg = '"+Batsman+"';"
        sql2 = "SELECT player FROM stats WHERE ctg = '"+WicketKeeper+"';"
        sql3 = "SELECT player FROM stats WHERE ctg ='"+Allrounder+"';"
        sql4 = "SELECT player FROM stats WHERE ctg = '"+Bowler+"';"

        dbcursor.execute(sql1)
        BT = dbcursor.fetchall()
        for i in range(len(BT)):
            self.totalbatsman.append(BT[i][0])
        dbcursor.execute(sql2)
        WK = dbcursor.fetchall()
        for i in range(len(WK)):
            self.totalwicketkeeper.append(WK[i][0])
        dbcursor.execute(sql3)
        AL = dbcursor.fetchall()
        for i in range(len(AL)):
            self.totalallrounder.append(AL[i][0])
        dbcursor.execute(sql4)
        BL = dbcursor.fetchall()
        for i in range(len(BL)):
            self.totalbowler.append(BL[i][0])
        dbroot.close()


    def set_all(self):

        #Setting Open Screen Dialog
        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        dbcursor.execute("SELECT name FROM teams;")
        team = dbcursor.fetchall()
        team_list = []
        team_list.clear()
        self.open_screen.teamselect_combobox.clear()
        self.open_screen.teamselect_combobox.addItem("")
        self.open_screen.teamselect_combobox.setItemText(0, "SELECT TEAM")
        for i in range(len(team)):
            team_list.append(team[i][0])
        for name in set(team_list):
            self.open_screen.teamselect_combobox.addItem(name)

        #Setting Evaluate Screen Dialog
        dbcursor.execute("SELECT name FROM teams;")
        team = dbcursor.fetchall()
        team_list = []
        team_list.clear()
        self.teamscore.clear()
        self.evaluate_screen.selectteam_combobox.clear()
        self.evaluate_screen.selectmatch_combobox.clear()
        self.evaluate_screen.pts_count_label.setText("")
        self.evaluate_screen.player_list.clear()
        self.evaluate_screen.matchpts_list.clear()

        self.evaluate_screen.selectteam_combobox.addItem("")
        self.evaluate_screen.selectmatch_combobox.addItem("")
        self.evaluate_screen.selectmatch_combobox.addItem("")

        self.evaluate_screen.selectteam_combobox.setItemText(0, "SELECT TEAM")
        self.evaluate_screen.selectmatch_combobox.setItemText(0, "SELECT MATCH")
        self.evaluate_screen.selectmatch_combobox.setItemText(1, "MATCH 1")

        for i in range(len(team)):
            team_list.append(team[i][0])

        for name in set(team_list):
            self.evaluate_screen.selectteam_combobox.addItem(name)

        dbroot.close()

    #new file menu_action
    def new_file(self):
        self.newDialog.show()

    #open file menu_action
    def open_file(self):
        self.set_all()
        self.openDialog.show()

    #Save File Method
    def save_file(self):
        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        for i in range(self.selected_player.count()):
            self.items.append(self.selected_player.item(i).text())

        tname = self.show_team_name.text()
        sql = "SELECT name FROM teams WHERE name = '"+tname+"';"
        dbcursor.execute(sql)
        result = dbcursor.fetchone()
        if result == []:
            for i in range(len(self.items)):
                dbcursor.execute("INSERT INTO teams ('name', 'player', 'value') VALUES (?, ?, ?);" , (tname, self.items[i], int(self.ptsused)))
                dbroot.commit()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Saved Successfully!")
            msg.setWindowTitle("Done!")
            msg.exec_()
        else:
            sql1 = ("DELETE FROM teams WHERE name = '"+tname+"';")
            dbcursor.execute(sql1)
            dbroot.commit()
            for i in range(len(self.items)):
                dbcursor.execute("INSERT INTO teams ('name', 'player', 'value') VALUES (?, ?, ?);" , (tname, self.items[i], int(self.ptsused)))
                dbroot.commit()
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Saved Successfully!")
            msg.setWindowTitle("Done!")
            msg.exec_()
        self.items.clear()
        dbroot.close()

    #Evaluate file menu_action
    def evaluate(self):
        self.set_all()
        self.evaluateDialog.show()

    #Set Team Name Method
    def get_team_name(self):
        self.reset()
        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        self.teamname = self.new_screen.newteam_line.text()
        dbcursor.execute("SELECT name FROM teams WHERE name = '"+self.teamname+"';")
        result = dbcursor.fetchone()
        if result == None:
            self.show_team_name.setText(self.teamname)
            self.listwidget = 1
            self.bat_button.setChecked(True)
            self.load_names()
            self.newDialog.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Team Name Already Exists!")
            msg.setWindowTitle("Error")
            msg.exec_()

    #Open Existing Team Method
    def open_my_team(self):
        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        myteamname = self.open_screen.teamselect_combobox.currentText()
        if myteamname != "SELECT TEAM":
            self.reset()
            self.show_team_name.setText(myteamname)
            self.listwidget = 1
            dbcursor.execute("SELECT player, value FROM teams WHERE name = '"+myteamname+"';")
            result = dbcursor.fetchall()
            self.avail -= result[-1][-1]
            self.ptsused = result[-1][-1]
            for i in range(len(result)):
                dbcursor.execute("SELECT ctg FROM stats WHERE player = '"+result[i][0]+"';")
                record = dbcursor.fetchall()
                for j in range(len(record)):
                    if record[j][0] == "BAT":
                        self.totalbatsman.remove(result[i][0])
                        self.batsmancount += 1
                        break
                    elif record[j][0] == "BWL":
                        self.totalbowler.remove(result[i][0])
                        self.ballcount += 1
                        break
                    elif record[j][0] == "WK":
                        self.totalwicketkeeper.remove(result[i][0])
                        self.wkeepercount += 1
                        break
                    elif record[j][0] == "AR":
                        self.totalallrounder.remove(result[i][0])
                        self.arcount += 1
                        break
                self.selected_player.addItem(result[i][0])
            self.bat_count.setText(str(self.batsmancount))
            self.bow_count.setText(str(self.ballcount))
            self.wk_count.setText(str(self.wkeepercount))
            self.ar_count.setText(str(self.arcount))
            self.pts_avail_count.setText(str(self.avail))
            self.pts_used_count.setText(str(self.ptsused))
            self.bat_button.setChecked(True)
            self.load_names()
            dbroot.close()
            self.openDialog.close()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Select Team")
            msg.setWindowTitle("Error")
            msg.exec_()

    #Load Players in Both List Widget Method
    def load_names(self):
        if self.listwidget == 1:
            if self.bat_button.isChecked() == True:
                self.current_player.clear()
                for i in range(len(self.totalbatsman)):
                    self.current_player.addItem(self.totalbatsman[i])

            if self.wk_button.isChecked() == True:
                self.current_player.clear()
                for i in range(len(self.totalwicketkeeper)):
                    self.current_player.addItem(self.totalwicketkeeper[i])

            if self.ar_button.isChecked() == True:
                self.current_player.clear()
                for i in range(len(self.totalallrounder)):
                    self.current_player.addItem(self.totalallrounder[i])

            if self.bow_button.isChecked() == True:
                self.current_player.clear()
                for i in range(len(self.totalbowler)):
                    self.current_player.addItem(self.totalbowler[i])
        else:
            self.newDialog.show()

    #Remove Player From Current_Player List Widget
    def remove_current_player(self, item):
        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        sql = ("SELECT value FROM stats WHERE player = '"+item.text()+"';")
        dbcursor.execute(sql)
        result = dbcursor.fetchall()
        if self.bat_button.isChecked() == True:
            if self.avail >= result[0][0]:
                self.batsmancount += 1
                self.totalcount = self.selected_player.count()
                self.x = self.error()
                if self.x != 1:
                    self.avail -= result[0][0]
                    self.ptsused += result[0][0]
                    self.current_player.takeItem(self.current_player.row(item))
                    self.totalbatsman.remove(item.text())
                    self.selected_player.addItem(item)
                    self.bat_count.setText(str(self.batsmancount))
                    self.pts_used_count.setText(str(self.ptsused))
                    self.pts_avail_count.setText(str(self.avail))
                else:
                    self.x = 0
                    self.batsmancount -= 1
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("Not Enough Points!")
                msg.setWindowTitle("Error")
                msg.exec_()

        elif self.wk_button.isChecked() == True:
            if self.avail >= result[0][0]:
                self.wkeepercount += 1
                self.totalcount = self.selected_player.count()
                self.x = self.error()
                if self.x != 1:
                    self.avail -= result[0][0]
                    self.ptsused += result[0][0]
                    self.current_player.takeItem(self.current_player.row(item))
                    self.totalwicketkeeper.remove(item.text())
                    self.selected_player.addItem(item)
                    self.wk_count.setText(str(self.wkeepercount))
                    self.pts_used_count.setText(str(self.ptsused))
                    self.pts_avail_count.setText(str(self.avail))
                else:
                    self.x = 0
                    self.wkeepercount -= 1
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("Not Enough Points!")
                msg.setWindowTitle("Error")
                msg.exec_()

        elif self.ar_button.isChecked()==True:
            if self.avail>=result[0][0]:
                self.arcount+=1
                self.totalcount=self.selected_player.count()
                self.x=self.error()
                if self.x!=1:
                    self.avail -= result[0][0]
                    self.ptsused += result[0][0]
                    self.current_player.takeItem(self.current_player.row(item))
                    self.totalallrounder.remove(item.text())
                    self.selected_player.addItem(item)
                    self.ar_count.setText(str(self.arcount))
                    self.pts_used_count.setText(str(self.ptsused))
                    self.pts_avail_count.setText(str(self.avail))
                else:
                    self.x=0
                    self.arcount-=1
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("Not Enough Points!")
                msg.setWindowTitle("Error")
                msg.exec_()

        elif self.bow_button.isChecked()==True:
            if self.avail >= result[0][0]:
                self.ballcount += 1
                self.totalcount = self.selected_player.count()
                self.x = self.error()
                if self.x != 1:
                    self.avail -= result[0][0]
                    self.ptsused += result[0][0]
                    self.current_player.takeItem(self.current_player.row(item))
                    self.totalbowler.remove(item.text())
                    self.selected_player.addItem(item)
                    self.bow_count.setText(str(self.ballcount))
                    self.pts_used_count.setText(str(self.ptsused))
                    self.pts_avail_count.setText(str(self.avail))
                else:
                    self.x = 0
                    self.ballcount -= 1
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Error")
                msg.setInformativeText("Not Enough Points!")
                msg.setWindowTitle("Error")
                msg.exec_()
        dbroot.close()

    #Remove Player From Selected_Player List Widget
    def remove_selected_player(self, item):
        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        sql = ("SELECT ctg, player, value FROM stats WHERE player = '"+item.text()+"';")
        dbcursor.execute(sql)
        result=dbcursor.fetchone()
        if result[0] == "BAT":
            self.batsmancount -= 1
            self.x = self.error2()
            if self.x != 1:
                self.avail += result[2]
                self.ptsused -= result[2]
                self.selected_player.takeItem(self.selected_player.row(item))
                self.totalbatsman.append(result[1])
                if self.bat_button.isChecked()==True:
                    self.current_player.addItem(item)
                self.bat_count.setText(str(self.batsmancount))
                self.pts_used_count.setText(str(self.ptsused))
                self.pts_avail_count.setText(str(self.avail))
            else:
                self.x = 0
                self.batsmancount += 1

        elif result[0] == "BWL":
            self.ballcount -= 1
            self.x = self.error2()
            if self.x!=1:
                self.avail += result[2]
                self.ptsused -= result[2]
                self.selected_player.takeItem(self.selected_player.row(item))
                self.totalbowler.append(result[1])
                if self.bow_button.isChecked()==True:
                    self.current_player.addItem(item)
                self.bow_count.setText(str(self.ballcount))
                self.pts_used_count.setText(str(self.ptsused))
                self.pts_avail_count.setText(str(self.avail))
            else:
                self.x = 0
                self.ballcount += 1

        elif result[0] == "AR":
            self.arcount -= 1
            self.x = self.error2()
            if self.x!=1:
                self.avail += result[2]
                self.ptsused -= result[2]
                self.selected_player.takeItem(self.selected_player.row(item))
                self.totalallrounder.append(result[1])
                if self.ar_button.isChecked()==True:
                    self.current_player.addItem(item)
                self.ar_count.setText(str(self.arcount))
                self.pts_used_count.setText(str(self.ptsused))
                self.pts_avail_count.setText(str(self.avail))
            else:
                self.x = 0
                self.arcount +=1

        elif result[0] == "WK":
            self.wkeepercount -= 1
            self.x = self.error2()
            if self.x!=1:
                self.avail += result[2]
                self.ptsused -= result[2]
                self.selected_player.takeItem(self.selected_player.row(item))
                self.totalwicketkeeper.append(result[1])
                if self.wk_button.isChecked()==True:
                    self.current_player.addItem(item)
                self.wk_count.setText(str(self.wkeepercount))
                self.pts_used_count.setText(str(self.ptsused))
                self.pts_avail_count.setText(str(self.avail))
            else:
                self.x = 0
                self.wkeepercount +=1
        dbroot.close()

    #Error Detection in Current Player Removal
    def error(self):

        if self.batsmancount<0 or self.batsmancount>5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than 5 Batsman")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

        if self.wkeepercount<0 or self.wkeepercount>1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than one Wicketkeeper")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

        if self.arcount<0 or self.arcount>3:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than 3 Allrounder")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

        if self.ballcount<0 or self.ballcount>5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than 5 Bowler")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

        if self.totalcount<0 or self.totalcount>=11:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than 11 Players")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

    #Error Detection in Selected_Player Removal
    def error2(self):
        if self.batsmancount<0 or self.batsmancount>5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than 5 Batsman")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

        if self.wkeepercount<0 or self.wkeepercount>1:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than one Wicketkeeper")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

        if self.arcount<0 or self.arcount>3:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than 3 Allrounder")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

        if self.ballcount<0 or self.ballcount>5:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("You can't select more than 5 Bowler")
            msg.setWindowTitle("Error")
            msg.exec_()
            return 1

    #Reset Everything
    def reset(self):
        self.batsmancount = 0
        self.wkeepercount = 0
        self.arcount = 0
        self.ballcount = 0
        self.avail = 1000
        self.ptsused = 0
        self.totalcount = 0
        self.listwidget = 0
        self.x = 0
        self.items = []
        self.totalbatsman = []
        self.totalbowler = []
        self.totalallrounder = []
        self.totalwicketkeeper = []
        self.current_player.clear()
        self.selected_player.clear()
        self.bat_count.setText(str(self.batsmancount))
        self.bow_count.setText(str(self.ballcount))
        self.ar_count.setText(str(self.arcount))
        self.wk_count.setText(str(self.wkeepercount))
        self.pts_avail_count.setText(str(self.avail))
        self.pts_used_count.setText(str(self.ptsused))
        self.get_all()

    #Add Selected Player in List in Evaluate Dialog
    def player_evaluate(self):
        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        selected_team = self.evaluate_screen.selectteam_combobox.currentText()
        if selected_team != "SELECT TEAM":
            dbcursor.execute("SELECT player FROM teams WHERE name ='"+selected_team+"';")
            self.result = dbcursor.fetchall()
            self.flag = 1
            self.evaluate_screen.player_list.clear()
            for i in range(len(self.result)):
                self.evaluate_screen.player_list.addItem(self.result[i][0])
        dbroot.close()

    #Add Points in List in Evaluate Dialog
    def match_evaluate(self):
        dbroot = sqlite3.connect('cricket.db')
        dbcursor = dbroot.cursor()
        selected_match = self.evaluate_screen.selectmatch_combobox.currentText()
        if selected_match != "SELECT MATCH" and self.flag!=0:
            record = []
            for i in range(len(self.result)):
                dbcursor.execute("SELECT points FROM match WHERE player = '"+self.result[i][0]+"';")
                record.append(dbcursor.fetchone())
            for i in range(len(record)):
                self.teamscore.append(record[i][0])
            self.evaluate_screen.matchpts_list.clear()
            for i in range(len(record)):
                self.evaluate_screen.matchpts_list.addItem(str(record[i][0]))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Select Team first!")
            msg.setWindowTitle("Error")
            msg.exec_()
        dbroot.close()

    #Show Points in Evaluate Dialog
    def show_point(self):
        if self.teamscore != []:
            self.evaluate_screen.pts_count_label.setText(str(sum(self.teamscore)))
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Select Team And Match")
            msg.setWindowTitle("Error")
            msg.exec_()

    #Quit Method
    def quit(self):
        sys.exit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CricketGame = QtWidgets.QMainWindow()
    ui = Ui_CricketGame()
    ui.setupUi(CricketGame)
    CricketGame.show()
    sys.exit(app.exec_())
