from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class MainWindow(QMainWindow):

    img_save = ""
    cur_file = "Untitled - Drawing Book"

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Untitled - Drawing Book")
        self.setGeometry(50, 50, 1200, 800)

        self.setFixedSize(1200, 800)

        self.image = QImage(self.size(), QImage.Format_RGB32)

        self.color = Qt.white

        self.image.fill(self.color)

        self.last_point = QPoint()

        self.brushColor = QColor(0,255,0)

        self.brushSize = 5

        self.draw = False

        # creating menu bar
        mainMenu = self.menuBar()

        fileMenu = mainMenu.addMenu("File")

        brushMenu = mainMenu.addMenu("Brush Color")

        self.brushSizeMenu = mainMenu.addMenu("Brush Size")

        EraseMenu = mainMenu.addMenu("Erase")

        backgroundColorMenu = mainMenu.addMenu("Background Color")

        # 

        new_action = QAction("New", self)

        new_action.setShortcut("Ctrl+N")

        new_action.triggered.connect(self.new_file)

        fileMenu.addAction(new_action)

        open_action = QAction("Open", self)

        open_action.setShortcut("Ctrl+O")

        open_action.triggered.connect(self.open_file)

        fileMenu.addAction(open_action)

        save_action = QAction("Save", self)

        save_action.setShortcut("Ctrl+S")

        fileMenu.addAction(save_action)

        save_action.triggered.connect(self.save)

        #

        brush_color_action = QAction("Choose Color", self)

        brushMenu.addAction(brush_color_action)

        brush_color_action.triggered.connect(self.changeBrushColor)
        

        #

        brush_size_3Px = QAction("3Px", self)

        self.brushSizeMenu.addAction(brush_size_3Px)

        brush_size_3Px.triggered.connect(lambda: self.changeBrushSize(3))

        brush_size_5Px = QAction("5Px", self)

        self.brushSizeMenu.addAction(brush_size_5Px)

        brush_size_5Px.triggered.connect(lambda: self.changeBrushSize(5))

        brush_size_7Px = QAction("7Px", self)

        self.brushSizeMenu.addAction(brush_size_7Px)

        brush_size_7Px.triggered.connect(lambda: self.changeBrushSize(7))

        brush_size_10Px = QAction("10Px", self)

        self.brushSizeMenu.addAction(brush_size_10Px)

        brush_size_10Px.triggered.connect(lambda: self.changeBrushSize(10))

        brush_size_12Px = QAction("12Px", self)

        self.brushSizeMenu.addAction(brush_size_12Px)

        brush_size_12Px.triggered.connect(lambda: self.changeBrushSize(12))

        #

        clear_action = QAction("Clear", self)

        clear_action.triggered.connect(self.clear)

        EraseMenu.addAction(clear_action)

        #

        bgcolor_action = QAction("Choose Color", self)

        bgcolor_action.triggered.connect(self.choose_background_color)

        backgroundColorMenu.addAction(bgcolor_action)

    def open_file(self):
        open_file = QFileDialog.getOpenFileName(self, "Open File", "", "PNG(*.png);;JPEG(*.jpeg)")

        l = open_file[0].split("/")

        if open_file[0] != "" and open_file[1] != "":
            self.image = QImage(open_file[0])
            self.cur_file = f"{l[len(l)-1]} - Drawing Book"
            name = l[len(l)-1].split(".")[0]
            self.setWindowTitle(f"{name} - Drawing Book")
            self.img_save = open_file[0]

    def new_file(self):
        self.image.fill(self.color)
        self.update()
        self.setWindowTitle("Untitled - Drawing Book")
        self.cur_file = "Untitled - Drawing Book"

    def choose_background_color(self):

        if self.cur_file == "Untitled - Drawing Book":

            ans = QMessageBox.question(self, "Alert", "you want to save, if No then, content will be lost")
            if ans == QMessageBox.Yes:
                self.save()
            else:
                self.color = QColorDialog.getColor()
                self.image.fill(self.color)
                self.update()
        
        else:
            self.save()
            self.color = QColorDialog.getColor()
            self.new_file()

    def clear(self):
        self.image.fill(self.color)
        self.update()

    def changeBrushColor(self):
        self.brushColor = QColorDialog.getColor()

    def changeBrushSize(self, i):
        self.brushSize = i
        self.brushSizeMenu.setTitle(f"Brush Size - {i}")

    def save(self):
        if self.cur_file == "Untitled - Drawing Book":
            file_name = QFileDialog.getSaveFileName(self, "Save Image", "Untitled", "PNG(*.png);;JPEG(*.jpeg);;All Files(*.*)")
            if file_name[0] == "" and file_name[1] == "":
                return
            else:
                self.image.save(file_name[0])
                self.img_save = file_name[0]
                l = file_name[0].split("/")
                name = l[len(l)-1].split(".")[0]
                self.setWindowTitle(f"{name} - Drawing Book")
                self.cur_file = f"{l[len(l)-1]} - Drawing Book"
        
        else:
            QMessageBox.about(self, "Successfull", "Your File Saved Successfully")
            self.image.save(self.img_save)

    def mousePressEvent(self, event):
        self.draw = True
        self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        if self.draw:
            painter = QPainter(self.image)

            painter.setPen(QPen(self.brushColor, self.brushSize, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))

            painter.drawLine(self.last_point, event.pos())

            self.last_point = event.pos()

            self.update()

    def mouseReleaseEvent(self, event):
        self.draw = False

    def paintEvent(self, event):
        canvas_painter = QPainter(self)

        canvas_painter.drawImage(self.rect(), self.image)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
