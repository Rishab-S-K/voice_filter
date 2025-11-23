# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDoubleSpinBox, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.actionLoad_Default_Recording = QAction(MainWindow)
        self.actionLoad_Default_Recording.setObjectName(u"actionLoad_Default_Recording")
        self.actionLoad_Your_Own_File = QAction(MainWindow)
        self.actionLoad_Your_Own_File.setObjectName(u"actionLoad_Your_Own_File")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.standardproperty = QToolBox(self.centralwidget)
        self.standardproperty.setObjectName(u"standardproperty")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 782, 387))
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.buttonGroup = QHBoxLayout()
        self.buttonGroup.setSpacing(5)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.buttonGroup.setContentsMargins(-1, 0, -1, -1)
        self.lpButton = QRadioButton(self.page)
        self.lpButton.setObjectName(u"lpButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lpButton.sizePolicy().hasHeightForWidth())
        self.lpButton.setSizePolicy(sizePolicy)
        self.lpButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 0px;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 5px 15px;\n"
"    background-color: #ddd;\n"
"    color: #222;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    image: none;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #eee;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #2196F3;\n"
"    color: white;\n"
"    border: 2px solid #1976D2;\n"
"}")

        self.buttonGroup.addWidget(self.lpButton)

        self.hpButton = QRadioButton(self.page)
        self.hpButton.setObjectName(u"hpButton")
        sizePolicy.setHeightForWidth(self.hpButton.sizePolicy().hasHeightForWidth())
        self.hpButton.setSizePolicy(sizePolicy)
        self.hpButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 0px;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 5px 15px;\n"
"    background-color: #ddd;\n"
"    color: #222;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    image: none;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #eee;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #FF9800;\n"
"    color: white;\n"
"    border: 2px solid #F57C00;\n"
"}")

        self.buttonGroup.addWidget(self.hpButton)

        self.bpButton = QRadioButton(self.page)
        self.bpButton.setObjectName(u"bpButton")
        sizePolicy.setHeightForWidth(self.bpButton.sizePolicy().hasHeightForWidth())
        self.bpButton.setSizePolicy(sizePolicy)
        self.bpButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 0px;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 5px 15px;\n"
"    background-color: #ddd;\n"
"    color: #222;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    image: none;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #eee;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #4CAF50;\n"
"    color: white;\n"
"    border: 2px solid #388E3C;\n"
"}")

        self.buttonGroup.addWidget(self.bpButton)

        self.bsButton = QRadioButton(self.page)
        self.bsButton.setObjectName(u"bsButton")
        sizePolicy.setHeightForWidth(self.bsButton.sizePolicy().hasHeightForWidth())
        self.bsButton.setSizePolicy(sizePolicy)
        self.bsButton.setStyleSheet(u"QRadioButton {\n"
"    spacing: 0px;\n"
"    border: 2px solid #555;\n"
"    border-radius: 6px;\n"
"    padding: 5px 15px;\n"
"    background-color: #ddd;\n"
"    color: #222;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    image: none;\n"
"}\n"
"\n"
"QRadioButton:hover {\n"
"    background-color: #eee;\n"
"}\n"
"\n"
"QRadioButton:checked {\n"
"    background-color: #F44336;\n"
"    color: white;\n"
"    border: 2px solid #D32F2F;\n"
"}")

        self.buttonGroup.addWidget(self.bsButton)


        self.verticalLayout_2.addLayout(self.buttonGroup)

        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setEnabled(False)
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.orderLabel = QLabel(self.groupBox)
        self.orderLabel.setObjectName(u"orderLabel")

        self.verticalLayout_3.addWidget(self.orderLabel)

        self.orderSpin = QSpinBox(self.groupBox)
        self.orderSpin.setObjectName(u"orderSpin")
        self.orderSpin.setMinimum(1)
        self.orderSpin.setMaximum(10)

        self.verticalLayout_3.addWidget(self.orderSpin)

        self.samplingLabel = QLabel(self.groupBox)
        self.samplingLabel.setObjectName(u"samplingLabel")

        self.verticalLayout_3.addWidget(self.samplingLabel)

        self.samplingLayout = QHBoxLayout()
        self.samplingLayout.setObjectName(u"samplingLayout")
        self.samplingSpin = QDoubleSpinBox(self.groupBox)
        self.samplingSpin.setObjectName(u"samplingSpin")
        self.samplingSpin.setMaximum(96000.000000000000000)
        self.samplingSpin.setSingleStep(1000.000000000000000)
        self.samplingSpin.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.samplingLayout.addWidget(self.samplingSpin)

        self.samplingSlider = QSlider(self.groupBox)
        self.samplingSlider.setObjectName(u"samplingSlider")
        self.samplingSlider.setMaximum(96000)
        self.samplingSlider.setSingleStep(100)
        self.samplingSlider.setOrientation(Qt.Orientation.Horizontal)

        self.samplingLayout.addWidget(self.samplingSlider)


        self.verticalLayout_3.addLayout(self.samplingLayout)

        self.cutoffLabel = QLabel(self.groupBox)
        self.cutoffLabel.setObjectName(u"cutoffLabel")

        self.verticalLayout_3.addWidget(self.cutoffLabel)

        self.cutoffLayout = QHBoxLayout()
        self.cutoffLayout.setObjectName(u"cutoffLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)

        self.cutoffLayout.addWidget(self.label)

        self.cutoffSpin1 = QDoubleSpinBox(self.groupBox)
        self.cutoffSpin1.setObjectName(u"cutoffSpin1")
        self.cutoffSpin1.setSingleStep(1000.000000000000000)

        self.cutoffLayout.addWidget(self.cutoffSpin1)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)

        self.cutoffLayout.addWidget(self.label_2)

        self.cutoffSpin2 = QDoubleSpinBox(self.groupBox)
        self.cutoffSpin2.setObjectName(u"cutoffSpin2")
        self.cutoffSpin2.setEnabled(False)
        self.cutoffSpin2.setSingleStep(1000.000000000000000)

        self.cutoffLayout.addWidget(self.cutoffSpin2)


        self.verticalLayout_3.addLayout(self.cutoffLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.standardproperty.addItem(self.page, u"Standard Filters (LP, HP, BP, BS)")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 782, 387))
        self.standardproperty.addItem(self.page_2, u"Custom Filters")

        self.verticalLayout.addWidget(self.standardproperty)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)

        self.playFiltered = QPushButton(self.centralwidget)
        self.playFiltered.setObjectName(u"playFiltered")

        self.gridLayout.addWidget(self.playFiltered, 2, 1, 1, 1)

        self.record = QPushButton(self.centralwidget)
        self.record.setObjectName(u"record")

        self.gridLayout.addWidget(self.record, 0, 0, 1, 1)

        self.saveFilter = QPushButton(self.centralwidget)
        self.saveFilter.setObjectName(u"saveFilter")

        self.gridLayout.addWidget(self.saveFilter, 2, 0, 1, 1)

        self.volumeSlider = QSlider(self.centralwidget)
        self.volumeSlider.setObjectName(u"volumeSlider")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.volumeSlider.sizePolicy().hasHeightForWidth())
        self.volumeSlider.setSizePolicy(sizePolicy2)
        self.volumeSlider.setMaximum(200)
        self.volumeSlider.setSingleStep(10)
        self.volumeSlider.setValue(100)
        self.volumeSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.volumeSlider, 2, 2, 1, 1)

        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")

        self.gridLayout.addWidget(self.play, 0, 1, 1, 1)

        self.telephonePresetButton = QPushButton(self.centralwidget)
        self.telephonePresetButton.setObjectName(u"telephonePresetButton")

        self.gridLayout.addWidget(self.telephonePresetButton, 3, 0, 1, 1)

        self.bassCutPresetButton = QPushButton(self.centralwidget)
        self.bassCutPresetButton.setObjectName(u"bassCutPresetButton")

        self.gridLayout.addWidget(self.bassCutPresetButton, 3, 1, 1, 1)

        self.trebleCutPresetButton = QPushButton(self.centralwidget)
        self.trebleCutPresetButton.setObjectName(u"trebleCutPresetButton")

        self.gridLayout.addWidget(self.trebleCutPresetButton, 3, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 800, 22))
        self.menuOptions = QMenu(self.menuBar)
        self.menuOptions.setObjectName(u"menuOptions")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuOptions.addAction(self.actionLoad_Default_Recording)
        self.menuOptions.addAction(self.actionLoad_Your_Own_File)
        self.menuOptions.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        self.standardproperty.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionLoad_Default_Recording.setText(QCoreApplication.translate("MainWindow", u"Load Default Recording", None))
        self.actionLoad_Your_Own_File.setText(QCoreApplication.translate("MainWindow", u"Load Your Own File", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"Exit", None))
        self.lpButton.setText(QCoreApplication.translate("MainWindow", u"Low-Pass", None))
        self.hpButton.setText(QCoreApplication.translate("MainWindow", u"High-Pass", None))
        self.bpButton.setText(QCoreApplication.translate("MainWindow", u"Band-Pass", None))
        self.bsButton.setText(QCoreApplication.translate("MainWindow", u"Band-Stop", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.orderLabel.setText(QCoreApplication.translate("MainWindow", u"Order (N)", None))
        self.samplingLabel.setText(QCoreApplication.translate("MainWindow", u"Sampling Frequency (fs)", None))
        self.cutoffLabel.setText(QCoreApplication.translate("MainWindow", u"Cutoff Frequency (wn)", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"  Low    :  ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"  High    :  ", None))
        self.standardproperty.setItemText(self.standardproperty.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Standard Filters (LP, HP, BP, BS)", None))
        self.standardproperty.setItemText(self.standardproperty.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Custom Filters", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"    Volume  :", None))
        self.playFiltered.setText(QCoreApplication.translate("MainWindow", u"PLAY FILTERED", None))
        self.record.setText(QCoreApplication.translate("MainWindow", u"RECORD", None))
        self.saveFilter.setText(QCoreApplication.translate("MainWindow", u"SAVE FILTER", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.telephonePresetButton.setText(QCoreApplication.translate("MainWindow", u"TELEPHONE PRESET", None))
        self.bassCutPresetButton.setText(QCoreApplication.translate("MainWindow", u"BASS CUT PRESET", None))
        self.trebleCutPresetButton.setText(QCoreApplication.translate("MainWindow", u"TREBLE CUT PRESET", None))
        self.menuOptions.setTitle(QCoreApplication.translate("MainWindow", u"Options", None))
    # retranslateUi

