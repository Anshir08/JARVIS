from jarvis import Ui_JarvisGUI
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
import sys, os, subprocess

# class MainThread(QThread):

#     def __init__(self):
#         super(MainThread,self).__init__()

#     def run(self):are you there

#         # os.startfile("C://Users//Anshir//Desktop//Some Folder//Final Year Project//main.py")
#         # subprocess.Popen([sys.executable, "C://Users//Anshir//Desktop//Some Folder//Final Year Project//main.py"], 
#         #                             stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
#         # subprocess.call("C://Users//Anshir//Desktop//Some Folder//Final Year Project//main.py", shell=True)
#         exec(open("C://Users//Anshir//Desktop//Some Folder//Final Year Project//main.py").read())

# startFunctions = MainThread()

class Gui_Start(QMainWindow):

    def __init__(self):
        super().__init__()
        self.jarvis_ui = Ui_JarvisGUI()
        self.jarvis_ui.setupUi(self)
        self.startFunc()
        # self.jarvis_ui.pushButton.clicked.connect(self.startFunc)
        # self.jarvis_ui.pushButton_2.clicked.connect(self.close)
    
    def startFunc(self):
        self.jarvis_ui.movies_2 = QtGui.QMovie("Iron_Template_1.gif")
        self.jarvis_ui.iron_man.setMovie(self.jarvis_ui.movies_2)
        self.jarvis_ui.movies_2.start()

        self.jarvis_ui.movies_3 = QtGui.QMovie("initial.gif")
        self.jarvis_ui.Initialize.setMovie(self.jarvis_ui.movies_3)
        self.jarvis_ui.movies_3.start()

        self.jarvis_ui.movies_4 = QtGui.QMovie("__1.gif")
        self.jarvis_ui.Voice_rec.setMovie(self.jarvis_ui.movies_4)
        self.jarvis_ui.movies_4.start()

        self.jarvis_ui.movies_5 = QtGui.QMovie("Health_Template.gif")
        self.jarvis_ui.Scan.setMovie(self.jarvis_ui.movies_5)
        self.jarvis_ui.movies_5.start()

        self.jarvis_ui.movies_6 = QtGui.QMovie("B.G_Template_1.gif")
        self.jarvis_ui.terminal.setMovie(self.jarvis_ui.movies_6)
        self.jarvis_ui.movies_6.start()

        self.jarvis_ui.movies_7 = QtGui.QMovie("Earth_Template.gif")
        self.jarvis_ui.label.setMovie(self.jarvis_ui.movies_7)
        self.jarvis_ui.movies_7.start()

        

Gui_App = QApplication(sys.argv)
Gui_Jarvis = Gui_Start()
Gui_Jarvis.show()
exit(Gui_App.exec_())
