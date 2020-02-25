# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(963, 485)
        icon = QIcon()
        icon.addFile(u"img/ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"	background-color: #fafafa;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(-20, 0, 491, 411))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.imgLabel = QLabel(self.frame)
        self.imgLabel.setObjectName(u"imgLabel")
        self.imgLabel.setGeometry(QRect(20, 0, 531, 391))
        self.imgLabel.setCursor(QCursor(Qt.ArrowCursor))
        self.imgLabel.setStyleSheet(u"QRadioButton {\n"
"	QCursor: pointing_hand;\n"
"}")
        self.imgLabel.setPixmap(QPixmap(u"img/map.png"))
        self.grodnoRB = QRadioButton(self.frame)
        self.grodnoRB.setObjectName(u"grodnoRB")
        self.grodnoRB.setGeometry(QRect(60, 200, 16, 17))
        self.grodnoRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.volkovyskRB = QRadioButton(self.frame)
        self.volkovyskRB.setObjectName(u"volkovyskRB")
        self.volkovyskRB.setGeometry(QRect(90, 230, 16, 17))
        self.volkovyskRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.lidaRB = QRadioButton(self.frame)
        self.lidaRB.setObjectName(u"lidaRB")
        self.lidaRB.setGeometry(QRect(130, 180, 16, 17))
        self.lidaRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.brestRB = QRadioButton(self.frame)
        self.brestRB.setObjectName(u"brestRB")
        self.brestRB.setGeometry(QRect(50, 310, 16, 17))
        self.brestRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.baranovichiRB = QRadioButton(self.frame)
        self.baranovichiRB.setObjectName(u"baranovichiRB")
        self.baranovichiRB.setGeometry(QRect(160, 240, 16, 17))
        self.baranovichiRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.pinskRB = QRadioButton(self.frame)
        self.pinskRB.setObjectName(u"pinskRB")
        self.pinskRB.setGeometry(QRect(160, 310, 16, 17))
        self.pinskRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.minskRB = QRadioButton(self.frame)
        self.minskRB.setObjectName(u"minskRB")
        self.minskRB.setGeometry(QRect(240, 190, 16, 17))
        self.minskRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.borisobRB = QRadioButton(self.frame)
        self.borisobRB.setObjectName(u"borisobRB")
        self.borisobRB.setGeometry(QRect(270, 150, 16, 17))
        self.borisobRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.soligorskRB = QRadioButton(self.frame)
        self.soligorskRB.setObjectName(u"soligorskRB")
        self.soligorskRB.setGeometry(QRect(230, 260, 16, 17))
        self.soligorskRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.gomelRB = QRadioButton(self.frame)
        self.gomelRB.setObjectName(u"gomelRB")
        self.gomelRB.setGeometry(QRect(380, 290, 16, 17))
        self.gomelRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.mozirRB = QRadioButton(self.frame)
        self.mozirRB.setObjectName(u"mozirRB")
        self.mozirRB.setGeometry(QRect(310, 320, 16, 17))
        self.mozirRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.turovRB = QRadioButton(self.frame)
        self.turovRB.setObjectName(u"turovRB")
        self.turovRB.setGeometry(QRect(240, 320, 16, 21))
        self.turovRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.bobruyskRB = QRadioButton(self.frame)
        self.bobruyskRB.setObjectName(u"bobruyskRB")
        self.bobruyskRB.setGeometry(QRect(300, 230, 16, 17))
        self.bobruyskRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.mogilevRB = QRadioButton(self.frame)
        self.mogilevRB.setObjectName(u"mogilevRB")
        self.mogilevRB.setGeometry(QRect(360, 180, 16, 17))
        self.mogilevRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.vitebskRB = QRadioButton(self.frame)
        self.vitebskRB.setObjectName(u"vitebskRB")
        self.vitebskRB.setGeometry(QRect(340, 70, 16, 17))
        self.vitebskRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.polotskRB = QRadioButton(self.frame)
        self.polotskRB.setObjectName(u"polotskRB")
        self.polotskRB.setGeometry(QRect(280, 60, 16, 17))
        self.polotskRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.orshaRB = QRadioButton(self.frame)
        self.orshaRB.setObjectName(u"orshaRB")
        self.orshaRB.setGeometry(QRect(360, 120, 16, 17))
        self.orshaRB.setCursor(QCursor(Qt.PointingHandCursor))
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(40, 190, 47, 13))
        self.label_10.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(120, 190, 47, 13))
        self.label_11.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(70, 240, 61, 16))
        self.label_12.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(50, 300, 47, 13))
        self.label_13.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(150, 300, 47, 13))
        self.label_14.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(140, 230, 71, 16))
        self.label_15.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(210, 246, 61, 20))
        self.label_16.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_17 = QLabel(self.frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(220, 180, 47, 13))
        self.label_17.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_18 = QLabel(self.frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(260, 140, 47, 13))
        self.label_18.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_19 = QLabel(self.frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(270, 50, 47, 13))
        self.label_19.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_20 = QLabel(self.frame)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setGeometry(QRect(320, 60, 47, 13))
        self.label_20.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_21 = QLabel(self.frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setGeometry(QRect(350, 100, 47, 21))
        self.label_21.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_22 = QLabel(self.frame)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(350, 170, 47, 13))
        self.label_22.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_23 = QLabel(self.frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(290, 216, 51, 16))
        self.label_23.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_24 = QLabel(self.frame)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setGeometry(QRect(360, 280, 47, 13))
        self.label_24.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setGeometry(QRect(300, 310, 47, 13))
        self.label_25.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.label_26 = QLabel(self.frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setGeometry(QRect(230, 310, 47, 13))
        self.label_26.setStyleSheet(u"font-weight: 400;\n"
"font-family: \"Ubuntu\";\n"
"color: #e91d62;")
        self.currentTownLabel = QLabel(self.centralwidget)
        self.currentTownLabel.setObjectName(u"currentTownLabel")
        self.currentTownLabel.setGeometry(QRect(10, 400, 461, 61))
        self.currentTownLabel.setStyleSheet(u"font-size: 28px;\n"
"font-family: 'Ubuntu';\n"
"font-weight: 500;\n"
"color: #e91d62;\n"
"border: 5px solid #e91d62;\n"
"border-radius: 20px;")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(550, 400, 321, 61))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color:none;\n"
"	border: 5px solid #e91d62;\n"
"	border-radius: 20px;\n"
"	color: #e91d62;\n"
"	font-family: \"Ubuntu\";\n"
"	font-size: 32px;\n"
"	font-weight: 500;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"	background-color: rgb(206, 206, 206);\n"
"}")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(470, 0, 491, 391))
        self.tabWidget.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"background-color:#fafafa;\n"
"color: #e91d62;\n"
"font-weight: 500;\n"
"font-size: 10;")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayoutWidget_7 = QWidget(self.tab_3)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(0, 70, 481, 51))
        self.gridLayout_16 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.gridLayout_16.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.gridLayoutWidget_7)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_16.addWidget(self.label_54, 0, 7, 1, 1)

        self.label_55 = QLabel(self.gridLayoutWidget_7)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_16.addWidget(self.label_55, 0, 4, 1, 1)

        self.label_56 = QLabel(self.gridLayoutWidget_7)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_16.addWidget(self.label_56, 0, 2, 1, 1)

        self.label_57 = QLabel(self.gridLayoutWidget_7)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_16.addWidget(self.label_57, 0, 5, 1, 1)

        self.label_58 = QLabel(self.gridLayoutWidget_7)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_16.addWidget(self.label_58, 0, 3, 1, 1)

        self.label_59 = QLabel(self.gridLayoutWidget_7)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_16.addWidget(self.label_59, 0, 1, 1, 1)

        self.label_60 = QLabel(self.gridLayoutWidget_7)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_16.addWidget(self.label_60, 0, 6, 1, 1)

        self.label_61 = QLabel(self.gridLayoutWidget_7)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_16.addWidget(self.label_61, 0, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(self.tab_3)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(0, 0, 481, 71))
        self.gridLayout_17 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.gridLayout_17.setContentsMargins(0, 0, 0, 0)
        self.todayLabel4 = QLabel(self.gridLayoutWidget_2)
        self.todayLabel4.setObjectName(u"todayLabel4")
        self.todayLabel4.setStyleSheet(u"font-family:\"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"padding: 2px;\n"
"background-color: rgb(151, 255, 177);\n"
"border-radius: 10px;\n"
"")

        self.gridLayout_17.addWidget(self.todayLabel4, 0, 2, 2, 1)

        self.todayLabel3 = QLabel(self.gridLayoutWidget_2)
        self.todayLabel3.setObjectName(u"todayLabel3")
        self.todayLabel3.setStyleSheet(u"font-family:\"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"padding: 2px;\n"
"padding-left: 12px;\n"
"")

        self.gridLayout_17.addWidget(self.todayLabel3, 0, 1, 2, 1)

        self.todayLabel1 = QLabel(self.gridLayoutWidget_2)
        self.todayLabel1.setObjectName(u"todayLabel1")
        self.todayLabel1.setStyleSheet(u"font-family:\"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"padding: 2px;\n"
"")

        self.gridLayout_17.addWidget(self.todayLabel1, 0, 0, 1, 1)

        self.todayLabel2 = QLabel(self.gridLayoutWidget_2)
        self.todayLabel2.setObjectName(u"todayLabel2")
        self.todayLabel2.setStyleSheet(u"font-family:\"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"padding: 2px;\n"
"background-color: rgb(151, 255, 177);\n"
"border-radius: 10px;\n"
"")

        self.gridLayout_17.addWidget(self.todayLabel2, 1, 0, 1, 1)

        self.gridLayoutWidget_8 = QWidget(self.tab_3)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(0, 220, 481, 141))
        self.gridLayout_18 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.gridLayout_18.setContentsMargins(0, 0, 0, 0)
        self.temp12_5 = QLabel(self.gridLayoutWidget_8)
        self.temp12_5.setObjectName(u"temp12_5")
        self.temp12_5.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_18.addWidget(self.temp12_5, 0, 4, 1, 1)

        self.temp15_5 = QLabel(self.gridLayoutWidget_8)
        self.temp15_5.setObjectName(u"temp15_5")
        self.temp15_5.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_18.addWidget(self.temp15_5, 0, 5, 1, 1)

        self.temp9_5 = QLabel(self.gridLayoutWidget_8)
        self.temp9_5.setObjectName(u"temp9_5")
        self.temp9_5.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_18.addWidget(self.temp9_5, 0, 3, 1, 1)

        self.temp3_5 = QLabel(self.gridLayoutWidget_8)
        self.temp3_5.setObjectName(u"temp3_5")
        self.temp3_5.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_18.addWidget(self.temp3_5, 0, 1, 1, 1)

        self.temp6_5 = QLabel(self.gridLayoutWidget_8)
        self.temp6_5.setObjectName(u"temp6_5")
        self.temp6_5.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_18.addWidget(self.temp6_5, 0, 2, 1, 1)

        self.temp0_5 = QLabel(self.gridLayoutWidget_8)
        self.temp0_5.setObjectName(u"temp0_5")
        self.temp0_5.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_18.addWidget(self.temp0_5, 0, 0, 1, 1)

        self.temp18_5 = QLabel(self.gridLayoutWidget_8)
        self.temp18_5.setObjectName(u"temp18_5")
        self.temp18_5.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_18.addWidget(self.temp18_5, 0, 6, 1, 1)

        self.temp21_5 = QLabel(self.gridLayoutWidget_8)
        self.temp21_5.setObjectName(u"temp21_5")
        self.temp21_5.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_18.addWidget(self.temp21_5, 0, 7, 1, 1)

        self.wind0_5 = QLabel(self.gridLayoutWidget_8)
        self.wind0_5.setObjectName(u"wind0_5")
        self.wind0_5.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_18.addWidget(self.wind0_5, 2, 0, 1, 1)

        self.wind3_5 = QLabel(self.gridLayoutWidget_8)
        self.wind3_5.setObjectName(u"wind3_5")
        self.wind3_5.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_18.addWidget(self.wind3_5, 2, 1, 1, 1)

        self.wind6_5 = QLabel(self.gridLayoutWidget_8)
        self.wind6_5.setObjectName(u"wind6_5")
        self.wind6_5.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_18.addWidget(self.wind6_5, 2, 2, 1, 1)

        self.wind9_5 = QLabel(self.gridLayoutWidget_8)
        self.wind9_5.setObjectName(u"wind9_5")
        self.wind9_5.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_18.addWidget(self.wind9_5, 2, 3, 1, 1)

        self.wind15_5 = QLabel(self.gridLayoutWidget_8)
        self.wind15_5.setObjectName(u"wind15_5")
        self.wind15_5.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_18.addWidget(self.wind15_5, 2, 5, 1, 1)

        self.wind18_5 = QLabel(self.gridLayoutWidget_8)
        self.wind18_5.setObjectName(u"wind18_5")
        self.wind18_5.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_18.addWidget(self.wind18_5, 2, 6, 1, 1)

        self.wind12_5 = QLabel(self.gridLayoutWidget_8)
        self.wind12_5.setObjectName(u"wind12_5")
        self.wind12_5.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_18.addWidget(self.wind12_5, 2, 4, 1, 1)

        self.wind21_5 = QLabel(self.gridLayoutWidget_8)
        self.wind21_5.setObjectName(u"wind21_5")
        self.wind21_5.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_18.addWidget(self.wind21_5, 2, 7, 1, 1)

        self.label_62 = QLabel(self.gridLayoutWidget_8)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 18px;\n"
"font-weight: 400;\n"
"font-style: italic;\n"
"padding: 0px 10px;")

        self.gridLayout_18.addWidget(self.label_62, 1, 0, 1, 4)

        self.gridLayoutWidget_9 = QWidget(self.tab_3)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(0, 120, 481, 101))
        self.gridLayout_19 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lab21_5 = QLabel(self.gridLayoutWidget_9)
        self.lab21_5.setObjectName(u"lab21_5")
        self.lab21_5.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_19.addWidget(self.lab21_5, 0, 7, 1, 1)

        self.lab18_5 = QLabel(self.gridLayoutWidget_9)
        self.lab18_5.setObjectName(u"lab18_5")
        self.lab18_5.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_19.addWidget(self.lab18_5, 0, 6, 1, 1)

        self.lab15_5 = QLabel(self.gridLayoutWidget_9)
        self.lab15_5.setObjectName(u"lab15_5")
        self.lab15_5.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_19.addWidget(self.lab15_5, 0, 5, 1, 1)

        self.lab9_5 = QLabel(self.gridLayoutWidget_9)
        self.lab9_5.setObjectName(u"lab9_5")
        self.lab9_5.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_19.addWidget(self.lab9_5, 0, 3, 1, 1)

        self.lab12_5 = QLabel(self.gridLayoutWidget_9)
        self.lab12_5.setObjectName(u"lab12_5")
        self.lab12_5.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_19.addWidget(self.lab12_5, 0, 4, 1, 1)

        self.lab6_5 = QLabel(self.gridLayoutWidget_9)
        self.lab6_5.setObjectName(u"lab6_5")
        self.lab6_5.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_19.addWidget(self.lab6_5, 0, 2, 1, 1)

        self.lab0_5 = QLabel(self.gridLayoutWidget_9)
        self.lab0_5.setObjectName(u"lab0_5")
        self.lab0_5.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_19.addWidget(self.lab0_5, 0, 0, 1, 1)

        self.lab3_5 = QLabel(self.gridLayoutWidget_9)
        self.lab3_5.setObjectName(u"lab3_5")
        self.lab3_5.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_19.addWidget(self.lab3_5, 0, 1, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.gridLayoutWidget_4 = QWidget(self.tab_4)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(0, 70, 481, 51))
        self.gridLayout_12 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.gridLayoutWidget_4)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_12.addWidget(self.label_45, 0, 7, 1, 1)

        self.label_46 = QLabel(self.gridLayoutWidget_4)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_12.addWidget(self.label_46, 0, 4, 1, 1)

        self.label_47 = QLabel(self.gridLayoutWidget_4)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_12.addWidget(self.label_47, 0, 2, 1, 1)

        self.label_48 = QLabel(self.gridLayoutWidget_4)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_12.addWidget(self.label_48, 0, 5, 1, 1)

        self.label_49 = QLabel(self.gridLayoutWidget_4)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_12.addWidget(self.label_49, 0, 3, 1, 1)

        self.label_50 = QLabel(self.gridLayoutWidget_4)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_12.addWidget(self.label_50, 0, 1, 1, 1)

        self.label_51 = QLabel(self.gridLayoutWidget_4)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_12.addWidget(self.label_51, 0, 6, 1, 1)

        self.label_52 = QLabel(self.gridLayoutWidget_4)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:#e91d62;\n"
"font-weight: 500;\n"
"padding: 4px;\n"
"margin: 14px 2px 2px 0px;\n"
"")

        self.gridLayout_12.addWidget(self.label_52, 0, 0, 1, 1)

        self.gridLayoutWidget_5 = QWidget(self.tab_4)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(0, 120, 481, 101))
        self.gridLayout_13 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.gridLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lab21_4 = QLabel(self.gridLayoutWidget_5)
        self.lab21_4.setObjectName(u"lab21_4")
        self.lab21_4.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_13.addWidget(self.lab21_4, 0, 7, 1, 1)

        self.lab18_4 = QLabel(self.gridLayoutWidget_5)
        self.lab18_4.setObjectName(u"lab18_4")
        self.lab18_4.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_13.addWidget(self.lab18_4, 0, 6, 1, 1)

        self.lab15_4 = QLabel(self.gridLayoutWidget_5)
        self.lab15_4.setObjectName(u"lab15_4")
        self.lab15_4.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_13.addWidget(self.lab15_4, 0, 5, 1, 1)

        self.lab9_4 = QLabel(self.gridLayoutWidget_5)
        self.lab9_4.setObjectName(u"lab9_4")
        self.lab9_4.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_13.addWidget(self.lab9_4, 0, 3, 1, 1)

        self.lab12_4 = QLabel(self.gridLayoutWidget_5)
        self.lab12_4.setObjectName(u"lab12_4")
        self.lab12_4.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_13.addWidget(self.lab12_4, 0, 4, 1, 1)

        self.lab6_4 = QLabel(self.gridLayoutWidget_5)
        self.lab6_4.setObjectName(u"lab6_4")
        self.lab6_4.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_13.addWidget(self.lab6_4, 0, 2, 1, 1)

        self.lab0_4 = QLabel(self.gridLayoutWidget_5)
        self.lab0_4.setObjectName(u"lab0_4")
        self.lab0_4.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_13.addWidget(self.lab0_4, 0, 0, 1, 1)

        self.lab3_4 = QLabel(self.gridLayoutWidget_5)
        self.lab3_4.setObjectName(u"lab3_4")
        self.lab3_4.setStyleSheet(u"padding-left: 4px;")

        self.gridLayout_13.addWidget(self.lab3_4, 0, 1, 1, 1)

        self.gridLayoutWidget_6 = QWidget(self.tab_4)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(0, 220, 481, 141))
        self.gridLayout_14 = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.gridLayout_14.setContentsMargins(0, 0, 0, 0)
        self.temp12_4 = QLabel(self.gridLayoutWidget_6)
        self.temp12_4.setObjectName(u"temp12_4")
        self.temp12_4.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_14.addWidget(self.temp12_4, 0, 4, 1, 1)

        self.temp15_4 = QLabel(self.gridLayoutWidget_6)
        self.temp15_4.setObjectName(u"temp15_4")
        self.temp15_4.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_14.addWidget(self.temp15_4, 0, 5, 1, 1)

        self.temp9_4 = QLabel(self.gridLayoutWidget_6)
        self.temp9_4.setObjectName(u"temp9_4")
        self.temp9_4.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_14.addWidget(self.temp9_4, 0, 3, 1, 1)

        self.temp3_4 = QLabel(self.gridLayoutWidget_6)
        self.temp3_4.setObjectName(u"temp3_4")
        self.temp3_4.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_14.addWidget(self.temp3_4, 0, 1, 1, 1)

        self.temp6_4 = QLabel(self.gridLayoutWidget_6)
        self.temp6_4.setObjectName(u"temp6_4")
        self.temp6_4.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_14.addWidget(self.temp6_4, 0, 2, 1, 1)

        self.temp0_4 = QLabel(self.gridLayoutWidget_6)
        self.temp0_4.setObjectName(u"temp0_4")
        self.temp0_4.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_14.addWidget(self.temp0_4, 0, 0, 1, 1)

        self.temp18_4 = QLabel(self.gridLayoutWidget_6)
        self.temp18_4.setObjectName(u"temp18_4")
        self.temp18_4.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_14.addWidget(self.temp18_4, 0, 6, 1, 1)

        self.temp21_4 = QLabel(self.gridLayoutWidget_6)
        self.temp21_4.setObjectName(u"temp21_4")
        self.temp21_4.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"background-color: rgb(151, 255, 177);\n"
"border-bottom: 2px solid rgb(54, 162, 79);\n"
"padding: 12px 0px 12px 12px;")

        self.gridLayout_14.addWidget(self.temp21_4, 0, 7, 1, 1)

        self.wind0_4 = QLabel(self.gridLayoutWidget_6)
        self.wind0_4.setObjectName(u"wind0_4")
        self.wind0_4.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_14.addWidget(self.wind0_4, 2, 0, 1, 1)

        self.wind3_4 = QLabel(self.gridLayoutWidget_6)
        self.wind3_4.setObjectName(u"wind3_4")
        self.wind3_4.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_14.addWidget(self.wind3_4, 2, 1, 1, 1)

        self.wind6_4 = QLabel(self.gridLayoutWidget_6)
        self.wind6_4.setObjectName(u"wind6_4")
        self.wind6_4.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_14.addWidget(self.wind6_4, 2, 2, 1, 1)

        self.wind9_4 = QLabel(self.gridLayoutWidget_6)
        self.wind9_4.setObjectName(u"wind9_4")
        self.wind9_4.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_14.addWidget(self.wind9_4, 2, 3, 1, 1)

        self.wind15_4 = QLabel(self.gridLayoutWidget_6)
        self.wind15_4.setObjectName(u"wind15_4")
        self.wind15_4.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_14.addWidget(self.wind15_4, 2, 5, 1, 1)

        self.wind18_4 = QLabel(self.gridLayoutWidget_6)
        self.wind18_4.setObjectName(u"wind18_4")
        self.wind18_4.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_14.addWidget(self.wind18_4, 2, 6, 1, 1)

        self.wind12_4 = QLabel(self.gridLayoutWidget_6)
        self.wind12_4.setObjectName(u"wind12_4")
        self.wind12_4.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_14.addWidget(self.wind12_4, 2, 4, 1, 1)

        self.wind21_4 = QLabel(self.gridLayoutWidget_6)
        self.wind21_4.setObjectName(u"wind21_4")
        self.wind21_4.setStyleSheet(u"background-color: rgb(220, 220, 220);\n"
"padding: 6px;\n"
"margin: 6px;\n"
"border-radius: 3px;\n"
"color: #e91d62;\n"
"font-family: \"Ubuntu\";\n"
"font-size: 10px;\n"
"font-weight: 500;")

        self.gridLayout_14.addWidget(self.wind21_4, 2, 7, 1, 1)

        self.label_53 = QLabel(self.gridLayoutWidget_6)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font-family: \"Ubuntu\";\n"
"font-size: 18px;\n"
"font-weight: 400;\n"
"font-style: italic;\n"
"padding: 0px 10px;")

        self.gridLayout_14.addWidget(self.label_53, 1, 0, 1, 4)

        self.gridLayoutWidget = QWidget(self.tab_4)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 481, 71))
        self.gridLayout_15 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_15.setContentsMargins(0, 0, 0, 0)
        self.tomorrowLabel2 = QLabel(self.gridLayoutWidget)
        self.tomorrowLabel2.setObjectName(u"tomorrowLabel2")
        self.tomorrowLabel2.setStyleSheet(u"font-family:\"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"padding: 2px;\n"
"background-color: rgb(151, 255, 177);\n"
"border-radius: 10px;\n"
"")

        self.gridLayout_15.addWidget(self.tomorrowLabel2, 1, 0, 1, 1)

        self.tomorrowLabel1 = QLabel(self.gridLayoutWidget)
        self.tomorrowLabel1.setObjectName(u"tomorrowLabel1")
        self.tomorrowLabel1.setStyleSheet(u"font-family:\"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"padding: 2px;\n"
"")

        self.gridLayout_15.addWidget(self.tomorrowLabel1, 0, 0, 1, 1)

        self.tomorrowLabel3 = QLabel(self.gridLayoutWidget)
        self.tomorrowLabel3.setObjectName(u"tomorrowLabel3")
        self.tomorrowLabel3.setStyleSheet(u"font-family:\"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"padding: 2px;\n"
"padding-left:12px;\n"
"\n"
"")

        self.gridLayout_15.addWidget(self.tomorrowLabel3, 0, 1, 2, 1)

        self.tomorrowLabel4 = QLabel(self.gridLayoutWidget)
        self.tomorrowLabel4.setObjectName(u"tomorrowLabel4")
        self.tomorrowLabel4.setStyleSheet(u"font-family:\"Ubuntu\";\n"
"font-size: 12px;\n"
"color:rgb(85, 170, 255);\n"
"font-weight: 500;\n"
"padding: 2px;\n"
"background-color: rgb(151, 255, 177);\n"
"border-radius: 10px;\n"
"")

        self.gridLayout_15.addWidget(self.tomorrowLabel4, 0, 2, 2, 1)

        self.tabWidget.addTab(self.tab_4, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u043e\u0433\u043d\u043e\u0437 \u043f\u043e\u0433\u043e\u0434\u044b", None))
        self.imgLabel.setText("")
        self.grodnoRB.setText("")
        self.volkovyskRB.setText("")
        self.lidaRB.setText("")
        self.brestRB.setText("")
        self.baranovichiRB.setText("")
        self.pinskRB.setText("")
        self.minskRB.setText("")
        self.borisobRB.setText("")
        self.soligorskRB.setText("")
        self.gomelRB.setText("")
        self.mozirRB.setText("")
        self.turovRB.setText("")
        self.bobruyskRB.setText("")
        self.mogilevRB.setText("")
        self.vitebskRB.setText("")
        self.polotskRB.setText("")
        self.orshaRB.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u0413\u0440\u043e\u0434\u043d\u043e", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u041b\u0438\u0434\u0430", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043e\u043b\u043a\u043e\u0432\u044b\u0441\u043a", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0440\u0435\u0441\u0442", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0438\u043d\u0441\u043a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"\u0411\u0430\u0440\u0430\u043d\u043e\u0432\u0438\u0447\u0438", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043e\u043b\u0438\u0433\u043e\u0440\u0441\u043a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0438\u043d\u0441\u043a", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u0440\u0438\u0441\u043e\u0432", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u043b\u043e\u0446\u043a", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0438\u0442\u0435\u0431\u0441\u043a", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0440\u0448\u0430", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0433\u0438\u043b\u0451\u0432", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"\u0411\u043e\u0431\u0440\u0443\u0439\u0441\u043a", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"\u0413\u043e\u043c\u0435\u043b\u044c", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"\u041c\u043e\u0437\u044b\u0440\u044c", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"\u0422\u0443\u0440\u043e\u0432", None))
        self.currentTownLabel.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u043d\u043d\u044b\u0439 \u0433\u043e\u0440\u043e\u0434:", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u043f\u043e\u0433\u043e\u0434\u0443", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"21:00", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"12:00", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"06:00", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"15:00", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"09:00", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"03:00", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"18:00", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.todayLabel4.setText("")
        self.todayLabel3.setText("")
        self.todayLabel1.setText("")
        self.todayLabel2.setText("")
        self.temp12_5.setText("")
        self.temp15_5.setText("")
        self.temp9_5.setText("")
        self.temp3_5.setText("")
        self.temp6_5.setText("")
        self.temp0_5.setText("")
        self.temp18_5.setText("")
        self.temp21_5.setText("")
        self.wind0_5.setText("")
        self.wind3_5.setText("")
        self.wind6_5.setText("")
        self.wind9_5.setText("")
        self.wind15_5.setText("")
        self.wind18_5.setText("")
        self.wind12_5.setText("")
        self.wind21_5.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0435\u0442\u0440\u0430, \u043c/\u0441:</p></body></html>", None))
        self.lab21_5.setText("")
        self.lab18_5.setText("")
        self.lab15_5.setText("")
        self.lab9_5.setText("")
        self.lab12_5.setText("")
        self.lab6_5.setText("")
        self.lab0_5.setText("")
        self.lab3_5.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430 \u043d\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"21:00", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"12:00", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"06:00", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"15:00", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"09:00", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"03:00", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"18:00", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"00:00", None))
        self.lab21_4.setText("")
        self.lab18_4.setText("")
        self.lab15_4.setText("")
        self.lab9_4.setText("")
        self.lab12_4.setText("")
        self.lab6_4.setText("")
        self.lab0_4.setText("")
        self.lab3_4.setText("")
        self.temp12_4.setText("")
        self.temp15_4.setText("")
        self.temp9_4.setText("")
        self.temp3_4.setText("")
        self.temp6_4.setText("")
        self.temp0_4.setText("")
        self.temp18_4.setText("")
        self.temp21_4.setText("")
        self.wind0_4.setText("")
        self.wind3_4.setText("")
        self.wind6_4.setText("")
        self.wind9_4.setText("")
        self.wind15_4.setText("")
        self.wind18_4.setText("")
        self.wind12_4.setText("")
        self.wind21_4.setText("")
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>\u0421\u043a\u043e\u0440\u043e\u0441\u0442\u044c \u0432\u0435\u0442\u0440\u0430, \u043c/\u0441:</p></body></html>", None))
        self.tomorrowLabel2.setText("")
        self.tomorrowLabel1.setText("")
        self.tomorrowLabel3.setText("")
        self.tomorrowLabel4.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0433\u043e\u0434\u0430 \u043d\u0430 \u0437\u0430\u0432\u0442\u0440\u0430", None))
    # retranslateUi

