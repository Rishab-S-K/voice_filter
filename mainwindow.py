# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QPushButton

import numpy as np
import scipy as sp
import soundfile as sf
import sounddevice as sd

from ui_mainwindow import Ui_MainWindow  # generated from .ui

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        #declare a variable to store sound array
        self.current_recording = None
        self.filtered_recording = None
        #Sampling Frequency (radio)
        self.freq = 44100
        #Duration (5 seconds)
        self.duration = 5

        sd.default.samplerate = self.freq

        #setup ui variable for accessing widget properties within mainwindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #connecting buttons
        self.ui.record.clicked.connect(self.record_audio)
        self.ui.play.clicked.connect(self.play_audio)




    def record_audio(self):
        self.current_recording = sd.rec(int(self.duration * self.freq), samplerate = self.freq, channels = 1)
        self.filtered_recording = self.current_recording
        sd.wait()


    def play_audio(self):
        sd.play(self.filtered_recording)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
