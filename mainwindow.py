import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog

import numpy as np
import scipy as sp
import soundfile as sf
import sounddevice as sd

from ui_mainwindow import Ui_MainWindow  # generated from .ui
from scipy.signal import butter, sosfilt, sosfiltfilt

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
        self.current_filter = None

        sd.default.samplerate = self.freq

        #setup ui variable for accessing widget properties within mainwindow
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #connecting buttons
        self.ui.record.clicked.connect(self.record_audio)
        self.ui.play.clicked.connect(self.play_audio)

        self.ui.lpButton.toggled.connect(self.on_lpButton_toggled)
        self.ui.hpButton.toggled.connect(self.on_hpButton_toggled)
        self.ui.bpButton.toggled.connect(self.on_bpButton_toggled)
        self.ui.bsButton.toggled.connect(self.on_bsButton_toggled)
        self.ui.samplingSpin.valueChanged.connect(self.on_samplingFrequency_changed)
        self.ui.samplingSlider.valueChanged.connect(self.on_samplingSlider_changed)

        self.ui.saveFilter.clicked.connect(self.on_saveFilter_clicked)
        self.ui.playFiltered.clicked.connect(self.on_playFilter_clicked)

        self.ui.volumeSlider.valueChanged.connect(self.on_volume_changed)

        self.ui.actionLoad_Your_Own_File.triggered.connect(self.on_loadFile_triggered)


    #initially record the audio
    def record_audio(self):
        self.current_recording = sd.rec(int(self.duration * self.freq), samplerate = self.freq, channels = 1)
        sd.wait()
        self.current_recording = self.current_recording.flatten()
        #normalize the recording first, then multiply it by volume factor
        self.current_recording = self.normalize(self.current_recording)
        self.current_recording_og = self.current_recording
        self.current_recording = self.current_recording * self.ui.volumeSlider.value()/100
        self.filtered_recording = self.current_recording

    #play the recorded audio
    def play_audio(self):
        sd.play(self.current_recording)

    def on_playFilter_clicked(self):
        sd.play(self.filtered_recording)

    #the following 4 buttons will trigger the properties to be enabled for standard filters
    def on_lpButton_toggled(self, checked):
        self.ui.groupBox.setEnabled(True)
        if checked:
            self.current_filter = 'low'
            self.ui.cutoffSpin2.setEnabled(False)

    def on_hpButton_toggled(self, checked):
        self.ui.groupBox.setEnabled(True)
        if checked:
            self.current_filter = 'high'
            self.ui.cutoffSpin2.setEnabled(False)


    def on_bpButton_toggled(self, checked):
        self.ui.groupBox.setEnabled(True)
        if checked:
            self.current_filter = 'band'
            self.ui.cutoffSpin2.setEnabled(True)


    def on_bsButton_toggled(self, checked):
        self.ui.groupBox.setEnabled(True)
        if checked:
            self.current_filter = 'bandstop'
            self.ui.cutoffSpin2.setEnabled(True)



    #when the sampling spin box is changed, change wn to be 1/2 * fs - 0.1 *nessasary for butter() functionality
    def on_samplingFrequency_changed(self,value):
        self.ui.samplingSlider.setValue(value)

        self.ui.cutoffSpin1.setMaximum(value/2 - 0.1)
        self.ui.cutoffSpin2.setMaximum(value/2 - 0.1)


    #when slider is changed, change the spinbox value too
    def on_samplingSlider_changed(self, value):
        self.ui.samplingSpin.setValue(value)

    def on_saveFilter_clicked(self):
        #check if low cut is greater than high cut
        band = False
        if(self.current_filter in ('band', 'bandstop')):
            band = True
            if(self.ui.cutoffSpin1.value() >= self.ui.cutoffSpin2.value()):
                QMessageBox.warning(self, "Warning", "Invalid range for cutoff frequencies.")

        if (band == False):
            print(self.ui.samplingSpin.value() , self.ui.cutoffSpin1.value())
            filter = butter(
                N=self.ui.orderSpin.value(),
                Wn=self.ui.cutoffSpin1.value(),
                btype=self.current_filter,
                fs=self.ui.samplingSpin.value(),
                output='sos'
                )
        if (band == True):
            filter = butter(
                N=self.ui.orderSpin.value(),
                Wn=[self.ui.cutoffSpin1.value(), self.ui.cutoffSpin2.value()],
                btype=self.current_filter,
                fs=self.ui.samplingSpin.value(),
                output='sos'
            )

        self.filtered_recording = sosfiltfilt(filter, self.current_recording)


    #adjust the levels of each sample  according to its peak amplitude
    def normalize(self, recording):
        peak = np.max(np.abs(recording))
        norm_recording = recording/peak
        return norm_recording


    def on_volume_changed(self, value):
        self.current_recording = self.current_recording_og * value/100.
        return

    def on_loadFile_triggered(self):
        wav_file, _ = QFileDialog.getOpenFileName(
            self,
            "Select an Audio File",
            "",
            "WAV Files (*.wav)"
        )

        if not wav_file:
            print("No .WAV selected.")
            return

        data, fs = sf.read(wav_file)
        self.current_recording = data
        #if stereo
        if data.ndim > 1:
            self.current_recording = self.current_recording.mean(axis = 1)
        #if mono
        else:
            self.current_recording = self.current_recording.flatten()

        #normalize the recording first, then multiply it by volume factor
        self.current_recording = self.normalize(self.current_recording)
        self.current_recording_og = self.current_recording
        self.current_recording = self.current_recording * self.ui.volumeSlider.value()/100
        self.filtered_recording = self.current_recording






if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
