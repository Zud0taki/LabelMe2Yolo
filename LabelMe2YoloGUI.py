# import necessary libraries and functions
import sys
from PyQt5.QtCore import QThread
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
from LabelMe2Yolo import main


# MainWindow is the Class of the Graphical User Interface
# define the class as QDialog and initialize it with its variables
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        loadUi("LabelMe2Yolo.ui", self)
        self.startButton.clicked.connect(self.mainstart)
        self.imageButton.clicked.connect(self.browseimages)
        self.textButton.clicked.connect(self.browsetext)
        self.outputButton.clicked.connect(self.browseoutput)

    # define browsetext
    # used to open an explorer for the text-folder selection
    def browsetext(self):
        textpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select JSON Folder', r'C:\Users\KIZwei\Desktop')
        self.textBrowser.setText(textpath)

    # define browseimages
    # used to open an explorer for the image-folder selection
    def browseimages(self):
        imgpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Image Folder', r'C:\Users\KIZwei\Desktop')
        self.imageBrowser.setText(imgpath)

    # define browseoutput
    # used to open an explorer for the output-folder selection
    def browseoutput(self):
        outputpath = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder', r'C:\Users\KIZwei\Desktop')
        self.outputBrowser.setText(outputpath)

    # define mainstart
    # used to start the main method in LabelMe2Yolo.py
    def mainstart(self):
        img_folder = self.imageBrowser.toPlainText()
        json_folder = self.textBrowser.toPlainText()
        out_folder = self.outputBrowser.toPlainText()
        main(img_folder, json_folder, out_folder)
        mainend = self.logBrowser.setText("Finished")




app = QApplication(sys.argv)
mainwindow = MainWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(616)
widget.setFixedHeight(361)
widget.show()
sys.exit(app.exec_())
