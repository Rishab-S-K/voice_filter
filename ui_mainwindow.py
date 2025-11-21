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
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGroupBox, QHBoxLayout,
    QLabel, QLayout, QMainWindow, QPushButton,
    QRadioButton, QSizePolicy, QSlider, QSpinBox,
    QStatusBar, QToolBox, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.standardproperty = QToolBox(self.centralwidget)
        self.standardproperty.setObjectName(u"standardproperty")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 778, 445))
        self.verticalLayout_2 = QVBoxLayout(self.page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.radioButton = QRadioButton(self.page)
        self.radioButton.setObjectName(u"radioButton")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.radioButton.sizePolicy().hasHeightForWidth())
        self.radioButton.setSizePolicy(sizePolicy)
        self.radioButton.setStyleSheet(u"QRadioButton {\n"
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

        self.horizontalLayout_2.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.page)
        self.radioButton_2.setObjectName(u"radioButton_2")
        sizePolicy.setHeightForWidth(self.radioButton_2.sizePolicy().hasHeightForWidth())
        self.radioButton_2.setSizePolicy(sizePolicy)
        self.radioButton_2.setStyleSheet(u"QRadioButton {\n"
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

        self.horizontalLayout_2.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.page)
        self.radioButton_3.setObjectName(u"radioButton_3")
        sizePolicy.setHeightForWidth(self.radioButton_3.sizePolicy().hasHeightForWidth())
        self.radioButton_3.setSizePolicy(sizePolicy)
        self.radioButton_3.setStyleSheet(u"QRadioButton {\n"
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

        self.horizontalLayout_2.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.page)
        self.radioButton_4.setObjectName(u"radioButton_4")
        sizePolicy.setHeightForWidth(self.radioButton_4.sizePolicy().hasHeightForWidth())
        self.radioButton_4.setSizePolicy(sizePolicy)
        self.radioButton_4.setStyleSheet(u"QRadioButton {\n"
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

        self.horizontalLayout_2.addWidget(self.radioButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.groupBox = QGroupBox(self.page)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.orderLabel = QLabel(self.groupBox)
        self.orderLabel.setObjectName(u"orderLabel")

        self.verticalLayout_3.addWidget(self.orderLabel)

        self.orderSpin = QSpinBox(self.groupBox)
        self.orderSpin.setObjectName(u"orderSpin")

        self.verticalLayout_3.addWidget(self.orderSpin)

        self.samplingLabel = QLabel(self.groupBox)
        self.samplingLabel.setObjectName(u"samplingLabel")

        self.verticalLayout_3.addWidget(self.samplingLabel)

        self.samplingLayout = QHBoxLayout()
        self.samplingLayout.setObjectName(u"samplingLayout")
        self.samplingSpin = QDoubleSpinBox(self.groupBox)
        self.samplingSpin.setObjectName(u"samplingSpin")

        self.samplingLayout.addWidget(self.samplingSpin)

        self.samplingSlider = QSlider(self.groupBox)
        self.samplingSlider.setObjectName(u"samplingSlider")
        self.samplingSlider.setOrientation(Qt.Orientation.Horizontal)

        self.samplingLayout.addWidget(self.samplingSlider)


        self.verticalLayout_3.addLayout(self.samplingLayout)

        self.cutoffLabel = QLabel(self.groupBox)
        self.cutoffLabel.setObjectName(u"cutoffLabel")

        self.verticalLayout_3.addWidget(self.cutoffLabel)

        self.cutoffLayout = QHBoxLayout()
        self.cutoffLayout.setObjectName(u"cutoffLayout")
        self.cutoffSpin = QDoubleSpinBox(self.groupBox)
        self.cutoffSpin.setObjectName(u"cutoffSpin")

        self.cutoffLayout.addWidget(self.cutoffSpin)

        self.cutoffSlider = QSlider(self.groupBox)
        self.cutoffSlider.setObjectName(u"cutoffSlider")
        self.cutoffSlider.setOrientation(Qt.Orientation.Horizontal)

        self.cutoffLayout.addWidget(self.cutoffSlider)


        self.verticalLayout_3.addLayout(self.cutoffLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.standardproperty.addItem(self.page, u"Standard Filters (LP, HP, BP, BS)")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 778, 445))
        self.standardproperty.addItem(self.page_2, u"Custom Filters")

        self.verticalLayout.addWidget(self.standardproperty)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.record = QPushButton(self.centralwidget)
        self.record.setObjectName(u"record")

        self.horizontalLayout.addWidget(self.record)

        self.play = QPushButton(self.centralwidget)
        self.play.setObjectName(u"play")

        self.horizontalLayout.addWidget(self.play)


        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.standardproperty.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Low-Pass", None))
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"High-Pass", None))
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Band-Pass", None))
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Band-Stop", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Properties", None))
        self.orderLabel.setText(QCoreApplication.translate("MainWindow", u"Order (N)", None))
        self.samplingLabel.setText(QCoreApplication.translate("MainWindow", u"Sampling Frequency (fs)", None))
        self.cutoffLabel.setText(QCoreApplication.translate("MainWindow", u"Cutoff Frequency (wn)", None))
        self.standardproperty.setItemText(self.standardproperty.indexOf(self.page), QCoreApplication.translate("MainWindow", u"Standard Filters (LP, HP, BP, BS)", None))
        self.standardproperty.setItemText(self.standardproperty.indexOf(self.page_2), QCoreApplication.translate("MainWindow", u"Custom Filters", None))
        self.record.setText(QCoreApplication.translate("MainWindow", u"RECORD", None))
        self.play.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
    # retranslateUi

