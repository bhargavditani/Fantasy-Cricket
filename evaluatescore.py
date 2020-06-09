# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluatescore.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(706, 488)
        self.evaluate_label = QtWidgets.QLabel(Form)
        self.evaluate_label.setGeometry(QtCore.QRect(10, 20, 681, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.evaluate_label.setFont(font)
        self.evaluate_label.setObjectName("evaluate_label")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 50, 691, 71))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.selectteam_combobox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.selectteam_combobox.setFont(font)
        self.selectteam_combobox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.selectteam_combobox.setObjectName("selectteam_combobox")



        self.horizontalLayout.addWidget(self.selectteam_combobox)
        self.selectmatch_combobox = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.selectmatch_combobox.setFont(font)
        self.selectmatch_combobox.setInsertPolicy(QtWidgets.QComboBox.InsertAtTop)
        self.selectmatch_combobox.setObjectName("selectmatch_combobox")
        self.horizontalLayout.addWidget(self.selectmatch_combobox)



        self.player_label = QtWidgets.QLabel(Form)
        self.player_label.setGeometry(QtCore.QRect(20, 140, 54, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.player_label.setFont(font)
        self.player_label.setObjectName("player_label")
        self.points_label = QtWidgets.QLabel(Form)
        self.points_label.setGeometry(QtCore.QRect(370, 140, 54, 14))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.points_label.setFont(font)
        self.points_label.setObjectName("points_label")
        self.pts_count_label = QtWidgets.QLabel(Form)
        self.pts_count_label.setGeometry(QtCore.QRect(450, 130, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pts_count_label.setFont(font)
        self.pts_count_label.setObjectName("pts_count_label")
        self.calscore_button = QtWidgets.QPushButton(Form)
        self.calscore_button.setGeometry(QtCore.QRect(300, 440, 111, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.calscore_button.setFont(font)
        self.calscore_button.setDefault(True)
        self.calscore_button.setObjectName("calscore_button")
        self.player_list = QtWidgets.QListWidget(Form)
        self.player_list.setGeometry(QtCore.QRect(20, 160, 311, 251))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.player_list.setFont(font)
        self.player_list.setObjectName("player_list")
        self.matchpts_list = QtWidgets.QListWidget(Form)
        self.matchpts_list.setGeometry(QtCore.QRect(370, 160, 311, 241))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.matchpts_list.setFont(font)
        self.matchpts_list.setObjectName("matchpts_list")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Score Evaluation"))
        self.evaluate_label.setText(_translate("Form", "Evaluate the Performance of your Fantasy Team"))
        self.player_label.setText(_translate("Form", "Players"))
        self.points_label.setText(_translate("Form", "Points"))
        self.pts_count_label.setText(_translate("Form", "00"))
        self.calscore_button.setText(_translate("Form", "Calculate Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
