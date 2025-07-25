# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filieres.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(805, 593)
        Dialog.setStyleSheet("background-color:#E3F0AF;")
        
        self.addbtn = QtWidgets.QPushButton(Dialog)
        self.addbtn.setGeometry(QtCore.QRect(630, 280, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.addbtn.setFont(font)
        self.addbtn.setStyleSheet("background-color:#118B50;color:#FBF6E9;")
        self.addbtn.setObjectName("addbtn")
        
        self.deletebtn = QtWidgets.QPushButton(Dialog)
        self.deletebtn.setGeometry(QtCore.QRect(630, 450, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.deletebtn.setFont(font)
        self.deletebtn.setStyleSheet("background-color:#118B50;color:#FBF6E9;")
        self.deletebtn.setObjectName("deletebtn")
        
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(90, 250, 441, 271))
        self.tableWidget.setStyleSheet("background-color:white;")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Nom de la Filière"])
        self.tableWidget.setObjectName("tableWidget")
        
        self.editbtn = QtWidgets.QPushButton(Dialog)
        self.editbtn.setGeometry(QtCore.QRect(630, 370, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.editbtn.setFont(font)
        self.editbtn.setStyleSheet("background-color:#118B50;color:#FBF6E9;")
        self.editbtn.setObjectName("editbtn")
        
        self.name = QtWidgets.QLineEdit(Dialog)
        self.name.setGeometry(QtCore.QRect(360, 60, 291, 31))
        self.name.setStyleSheet("background-color:white;")
        self.name.setObjectName("name")
        
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(90, 40, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label.setFont(font)
        self.label.setStyleSheet("color:#118B50;")
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.db = sqlite3.connect('school.db')
        self.db.execute("PRAGMA foreign_keys = ON;") 
        self.cursor = self.db.cursor()

        self.load_data()

        self.addbtn.clicked.connect(self.add_filiere)
        self.editbtn.clicked.connect(self.edit_filiere)
        self.deletebtn.clicked.connect(self.delete_filiere)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.addbtn.setText(_translate("Dialog", "Ajouter"))
        self.deletebtn.setText(_translate("Dialog", "Supprimer"))
        self.editbtn.setText(_translate("Dialog", "Modifier"))
        self.label.setText(_translate("Dialog", "Entrer le nom de la filière:"))

    def add_filiere(self):
        name = self.name.text().strip()
        if name:
            self.cursor.execute("INSERT INTO filieres (name) VALUES (?)", (name,))
            self.db.commit()
            self.load_data()

    def edit_filiere(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            filiere_id = self.tableWidget.item(row, 0).text()
            new_name = self.name.text().strip()
            if new_name:
                self.cursor.execute("UPDATE filieres SET name = ? WHERE id = ?", (new_name, filiere_id))
                self.db.commit()
                self.load_data()

    def delete_filiere(self):
        row = self.tableWidget.currentRow()
        if row >= 0:
            filiere_id = self.tableWidget.item(row, 0).text()

            self.cursor.execute("DELETE FROM etudiants WHERE classe_id = ?", (filiere_id,))
            self.db.commit()

            self.cursor.execute("DELETE FROM filieres WHERE id = ?", (filiere_id,))
            self.db.commit()

            self.load_data()


    def load_data(self):
        self.cursor.execute("SELECT * FROM filieres")
        filieres = self.cursor.fetchall()
        self.tableWidget.setRowCount(0)
        for filiere in filieres:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(rowPosition, 0, QtWidgets.QTableWidgetItem(str(filiere[0])))
            self.tableWidget.setItem(rowPosition, 1, QtWidgets.QTableWidgetItem(filiere[1]))

    def closeEvent(self, event):
        self.db.close()
        event.accept()



