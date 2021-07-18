from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QFontDialog
import os

class Ui_MainWindow(object):
    text = ""
    cur_file = "Untitled - Notepad"
    def setupUi(self, MainWindow):
        MainWindow.setWindowTitle("Untitled - Notepad")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(941, 750)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, -4, 941, 701))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 941, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuFont = QtWidgets.QMenu(self.menubar)
        self.menuFont.setObjectName("menuFont")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionNew.setFont(font)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionOpen.setFont(font)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionSave.setFont(font)
        self.actionSave.setObjectName("actionSave")
        self.actionCut = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionCut.setFont(font)
        self.actionCut.setObjectName("actionCut")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionCopy.setFont(font)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionPaste.setFont(font)
        self.actionPaste.setObjectName("actionPaste")
        self.actionFont_Size = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionFont_Size.setFont(font)
        self.actionFont_Size.setObjectName("actionFont_Size")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setCheckable(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.actionAbout.setFont(font)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave)
        self.menuEdit.addAction(self.actionCut)
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actionPaste)
        self.menuFont.addAction(self.actionFont_Size)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFont.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.mainWindow = MainWindow
        self.actionAbout.triggered.connect(self.about)
        self.actionCut.triggered.connect(self.cut_text)
        self.actionPaste.triggered.connect(self.paste_text)
        self.actionCopy.triggered.connect(self.copy_text)
        self.actionFont_Size.triggered.connect(self.font_size)
        self.actionNew.triggered.connect(self.new)
        self.actionOpen.triggered.connect(self.open)
        self.actionSave.triggered.connect(self.save)

        self.statusbar.showMessage("Status Bar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def new(self):
        if self.textEdit.toPlainText() != "":
            if self.cur_file == "Untitled - Notepad":
                ans = QMessageBox.question(self.textEdit, "Information", "Do you want to save changes to untitled")
                if ans == QMessageBox.Yes:
                    self.save()
                else:
                    self.mainWindow.setWindowTitle("Untitled - Notepad")
                    self.textEdit.clear()
                    self.cur_file == "Untitled - Notepad"
            else:
                if self.text != self.textEdit.toPlainText():
                    ans = QMessageBox.question(self.textEdit, "Information", "Do you want to save changes to untitled")
                    if ans == QMessageBox.Yes:
                        self.save()
                        self.mainWindow.setWindowTitle("Untitled - Notepad")
                        self.textEdit.clear()
                        self.cur_file = "Untitled - Notepad"
                    else:
                        self.mainWindow.setWindowTitle("Untitled - Notepad")
                        self.textEdit.clear()
                        self.cur_file = "Untitled - Notepad"
                else:
                    self.mainWindow.setWindowTitle("Untitled - Notepad")
                    self.textEdit.clear()
                    self.cur_file == "Untitled - Notepad"

        else:
            if self.text != self.textEdit.toPlainText():
                ans = QMessageBox.question(self.textEdit, "Information", "Do you want to save changes to untitled")
                if ans == QMessageBox.Yes:
                    self.save()
                    self.mainWindow.setWindowTitle("Untitled - Notepad")
                    self.textEdit.clear()
                    self.cur_file == "Untitled - Notepad"
                else:
                    self.mainWindow.setWindowTitle("Untitled - Notepad")
                    self.textEdit.clear()
                    self.cur_file == "Untitled - Notepad"

            else:
                self.mainWindow.setWindowTitle("Untitled - Notepad")
                self.textEdit.clear()
                self.cur_file == "Untitled - Notepad"

        self.text = ""

    def save(self):
        if self.cur_file == "Untitled - Notepad":
            name = QtWidgets.QFileDialog.getSaveFileName(self.textEdit, "Save File")
            if name == ("",""):
                pass
            else:
                file = open(name[0], 'w')
                self.text = self.textEdit.toPlainText()
                file.write(self.text)
                self.cur_file = name[0]
                file.close
                l = name[0].split("/")
                self.mainWindow.setWindowTitle(l[len(l)-1] + " - Notepad")
        else:
            file = open(self.cur_file, 'w')
            self.text = self.textEdit.toPlainText()
            file.write(self.text)
            file.close

    def open(self):
        if self.cur_file == "Untitled - Notepad" and self.textEdit.toPlainText() != "":
            ans = QMessageBox.question(self.textEdit, "Information", "Do you want to save changes to untitled")
            if ans == QMessageBox.Yes:
                self.save()
            else:
                name = QtWidgets.QFileDialog.getOpenFileName(self.textEdit, "Open File")
                if name == ("",""):
                    pass
                else:
                    file = open(name[0], 'r')
                    text = file.read()
                    self.textEdit.setText(text)
                    self.cur_file = name[0]
                    l = name[0].split("/")
                    self.mainWindow.setWindowTitle(l[len(l)-1] + " - Notepad")

        else:
            if self.text != self.textEdit.toPlainText():
                ans = QMessageBox.question(self.textEdit, "Information", "Do you want to save changes to untitled")
                if ans == QMessageBox.Yes:
                    self.save()
                    name = QtWidgets.QFileDialog.getOpenFileName(self.textEdit, "Open File")
                    if name == ("",""):
                        pass
                    else:
                        file = open(name[0], 'r')
                        text = file.read()
                        self.textEdit.setText(text)
                        self.cur_file = name[0]
                        l = name[0].split("/")
                        self.mainWindow.setWindowTitle(l[len(l)-1] + " - Notepad")
                else:
                    name = QtWidgets.QFileDialog.getOpenFileName(self.textEdit, "Open File")
                    if name == ("",""):
                        pass
                    else:
                        file = open(name[0], 'r')
                        text = file.read()
                        self.textEdit.setText(text)
                        self.cur_file = name[0]
                        l = name[0].split("/")
                        self.mainWindow.setWindowTitle(l[len(l)-1] + " - Notepad")
            else:
                name = QtWidgets.QFileDialog.getOpenFileName(self.textEdit, "Open File")
                if name == ("",""):
                    pass
                else:
                    file = open(name[0], 'r')
                    self.text = file.read()
                    self.textEdit.setText(self.text)
                    self.cur_file = name[0]
                    l = name[0].split("/")
                    self.mainWindow.setWindowTitle(l[len(l)-1] + " - Notepad")


    def font_size(self):
        self.font, ans = QFontDialog.getFont()
        if ans:
            self.textEdit.setFont(self.font)

    def about(self):
        QMessageBox.about(self.centralwidget, "About","Notepad is made by Jwalant Modi")

    def cut_text(self):
        self.textEdit.cut()

    def copy_text(self):
        self.textEdit.copy()

    def paste_text(self):
        self.textEdit.paste()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        # MainWindow.setWindowTitle(_translate("MainWindow", "Notepad"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuFont.setTitle(_translate("MainWindow", "Font"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionCut.setText(_translate("MainWindow", "Cut"))
        self.actionCut.setShortcut(_translate("MainWindow", "Ctrl+X"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionCopy.setShortcut(_translate("MainWindow", "Ctrl+C"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionPaste.setShortcut(_translate("MainWindow", "Ctrl+V"))
        self.actionFont_Size.setText(_translate("MainWindow", "Font Size"))
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
