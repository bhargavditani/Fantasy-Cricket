# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openteam.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(320, 240)
        self.open_label = QtWidgets.QLabel(Form)
        self.open_label.setGeometry(QtCore.QRect(10, 60, 301, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.open_label.setFont(font)
        self.open_label.setObjectName("open_label")
        self.ok_button = QtWidgets.QPushButton(Form)
        self.ok_button.setGeometry(QtCore.QRect(110, 180, 85, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ok_button.setFont(font)
        self.ok_button.setAutoDefault(True)
        self.ok_button.setObjectName("ok_button")
        self.teamselect_combobox = QtWidgets.QComboBox(Form)
        self.teamselect_combobox.setGeometry(QtCore.QRect(30, 120, 251, 22))
        self.teamselect_combobox.setObjectName("teamselect_combobox")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Open Team"))
        self.open_label.setText(_translate("Form", "Select Team Name to Open"))
        self.ok_button.setText(_translate("Form", "OK"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
