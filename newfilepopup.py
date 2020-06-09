# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'newfilepopup.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        self.teamname_label = QtWidgets.QLabel(Form)
        self.teamname_label.setGeometry(QtCore.QRect(0, 50, 321, 51))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.teamname_label.setFont(font)
        self.teamname_label.setObjectName("teamname_label")

        ####################################################
        ####################################################

        self.newteam_line = QtWidgets.QLineEdit(Form)
        self.newteam_line.setGeometry(QtCore.QRect(30, 110, 261, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.newteam_line.setFont(font)
        self.newteam_line.setClearButtonEnabled(False)
        self.newteam_line.setObjectName("newteam_line")

        #######################################################
        #######################################################

        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(110, 190, 85, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setDefault(True)
        self.ok_button.setFlat(False)
        self.ok_button.setObjectName("ok_button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "New Team"))
        self.teamname_label.setText(_translate("Form", "Enter New Team Name"))
        self.newteam_line.setPlaceholderText(_translate("Form", "e.g. India"))
        self.ok_button.setText(_translate("Form", "OK"))


