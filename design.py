# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import main


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(520, 397)
        MainWindow.setMouseTracking(False)
        MainWindow.setTabletTracking(False)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(24, 32, 35);")
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(40, 50, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_name.setFont(font)
        self.lineEdit_name.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_name.setStyleSheet("border-style: outset;\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: beige;\n"
"")
        self.lineEdit_name.setInputMask("")
        self.lineEdit_name.setText("")
        self.lineEdit_name.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_name.setDragEnabled(False)
        self.lineEdit_name.setReadOnly(False)
        self.lineEdit_name.setPlaceholderText("")
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.lineEdit_job = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_job.setGeometry(QtCore.QRect(40, 260, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_job.setFont(font)
        self.lineEdit_job.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_job.setStyleSheet("border-style: outset;\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: beige;\n"
"")
        self.lineEdit_job.setText("")
        self.lineEdit_job.setPlaceholderText("")
        self.lineEdit_job.setObjectName("lineEdit_job")
        self.lineEdit_email = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_email.setGeometry(QtCore.QRect(40, 190, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_email.setFont(font)
        self.lineEdit_email.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_email.setStyleSheet("border-style: outset;\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: beige;\n"
"")
        self.lineEdit_email.setText("")
        self.lineEdit_email.setPlaceholderText("")
        self.lineEdit_email.setObjectName("lineEdit_email")
        self.lineEdit_phone_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_phone_number.setGeometry(QtCore.QRect(40, 120, 291, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(13)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEdit_phone_number.setFont(font)
        self.lineEdit_phone_number.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.lineEdit_phone_number.setStyleSheet("border-style: outset;\n"
"font: 13pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"border-width: 2px;\n"
"border-radius: 5px;\n"
"border-color: beige;\n"
"")
        self.lineEdit_phone_number.setText("")
        self.lineEdit_phone_number.setPlaceholderText("")
        self.lineEdit_phone_number.setObjectName("lineEdit_phone_number")

        self.pushButton_add = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add.setGeometry(QtCore.QRect(350, 50, 131, 30))
        self.pushButton_add.setMouseTracking(False)
        self.pushButton_add.setTabletTracking(False)
        self.pushButton_add.setAcceptDrops(False)
        self.pushButton_add.setAutoFillBackground(False)
        self.pushButton_add.setStyleSheet("background-color: rgb(97, 142, 150);\n"
"border-radius: 5px;\n"
"font: 12pt \"Fixedsys\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_add.clicked.connect(lambda: main.add_contact(self.lineEdit_name.text(),self.lineEdit_phone_number.text(),self.lineEdit_email.text(),self.lineEdit_job.text()))
        # ^ clicking on the button calls the add_contact function from the main.py file

        self.pushButton_create_db = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_create_db.setGeometry(QtCore.QRect(40, 320, 191, 41))
        self.pushButton_create_db.setStyleSheet("background-color: rgb(115, 170, 180);\n"
"border-radius: 5px;\n"
"font: 12pt \"Fixedsys\";\n"
"color: rgb(24, 32, 35);")
        self.pushButton_create_db.setObjectName("pushButton_create_db")
        self.pushButton_create_db.clicked.connect(lambda: main.create_database(main.contact_list))  # clicking on the button calls the create_database function from the main.py file

        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(350, 120, 131, 30))
        self.pushButton_delete.setStyleSheet("background-color: rgb(97, 142, 150);\n"
"border-radius: 5px;\n"
"font: 12pt \"Fixedsys\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.pushButton_delete.clicked.connect(lambda: main.delete_contact(main.contact_list))  # clicking on the button calls the delete_contact function from the main.py file

        self.pushButton_find = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_find.setGeometry(QtCore.QRect(350, 190, 131, 30))
        self.pushButton_find.setStyleSheet("background-color: rgb(97, 142, 150);\n"
"border-radius: 5px;\n"
"font: 12pt \"Fixedsys\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_find.setObjectName("pushButton_find")
        self.pushButton_find.clicked.connect(lambda: main.find_contact(main.contact_list))  # clicking on the button calls the find_contact function from the main.py file

        self.pushButton_save = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save.setGeometry(QtCore.QRect(350, 260, 131, 30))
        self.pushButton_save.setStyleSheet("background-color: rgb(97, 142, 150);\n"
"border-radius: 5px;\n"
"font: 12pt \"Fixedsys\";\n"
"color: rgb(255, 255, 255);")
        self.pushButton_save.setObjectName("pushButton_save")
        self.pushButton_save.clicked.connect(lambda: main.save_contact_list(main.contact_list))  # clicking on the button calls the save_contact_list function from the main.py file

        self.label_name = QtWidgets.QLabel(self.centralwidget)
        self.label_name.setGeometry(QtCore.QRect(40, 30, 131, 16))
        self.label_name.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Fixedsys\";")
        self.label_name.setObjectName("label_name")
        self.label_phone_number = QtWidgets.QLabel(self.centralwidget)
        self.label_phone_number.setGeometry(QtCore.QRect(40, 100, 131, 16))
        self.label_phone_number.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Fixedsys\";")
        self.label_phone_number.setObjectName("label_phone_number")
        self.label_email = QtWidgets.QLabel(self.centralwidget)
        self.label_email.setGeometry(QtCore.QRect(40, 170, 131, 16))
        self.label_email.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Fixedsys\";")
        self.label_email.setObjectName("label_email")
        self.label_job = QtWidgets.QLabel(self.centralwidget)
        self.label_job.setGeometry(QtCore.QRect(40, 240, 131, 16))
        self.label_job.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 15pt \"Fixedsys\";")
        self.label_job.setObjectName("label_job")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Contact Book"))
        self.pushButton_add.setText(_translate("MainWindow", "ADD"))
        self.pushButton_create_db.setText(_translate("MainWindow", "Create database"))
        self.pushButton_delete.setText(_translate("MainWindow", "DELETE"))
        self.pushButton_find.setText(_translate("MainWindow", "FIND"))
        self.pushButton_save.setText(_translate("MainWindow", "SAVE"))
        self.label_name.setText(_translate("MainWindow", "Full name"))
        self.label_phone_number.setText(_translate("MainWindow", "Phone number"))
        self.label_email.setText(_translate("MainWindow", "Email"))
        self.label_job.setText(_translate("MainWindow", "Job"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())