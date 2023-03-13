# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSlider, QSpinBox, QVBoxLayout, QWidget)
import ui.resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QSize(640, 480))
        MainWindow.setMaximumSize(QSize(640, 480))
        icon = QIcon()
        icon.addFile(u":/icons/resources/app_icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"    background-color: #ececec;\n"
"    color: #142d4c;\n"
"    font-family: Roboto;\n"
"    font-size: 16pt;\n"
"    margin: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"    border: 2px solid #385170;\n"
"	padding: 10px;\n"
"    border-radius: 5px;\n"
"	margin: 0 5px 0 0;\n"
"}\n"
"\n"
"QPushButton#btn_lower, #btn_upper, #btn_digits, #btn_punct{\n"
"    padding: 10px 0;\n"
"	margin-left: 5px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    border-color: #9fd3c7;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    border: 6px solid #385170;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"    background-color: #9fd3c7;\n"
"    border: 4px solid #385170;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border: 2px solid #385170;\n"
"	border-radius: 5px;\n"
"    margin-left: 5px;\n"
"    font-size: 20pt;\n"
"}\n"
"\n"
"QSlider::groove:horizontal {\n"
"    background-color: transparent;\n"
"    height: 5px;\n"
"}\n"
"\n"
"QSlider::sub-page:horizontal {\n"
"    background-color: #9fd3c7;\n"
"}\n"
"\n"
"QSlider::a"
                        "dd-page:horizontal {\n"
"    background-color: #385170;\n"
"}\n"
"\n"
"QSlider::handle:horizontal {\n"
"    background-color: #ececec;\n"
"	border: 2px solid #385170;\n"
"    width: 18px;\n"
"    border-radius: 10px;\n"
"    margin-top: -8px;\n"
"    margin-bottom: -8px;\n"
"}\n"
"\n"
"QSpinBox {\n"
"    background: transparent;\n"
"    border: 2px solid #385170;\n"
"	padding: 10px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QSpinBox:hover {\n"
"    border-color: #9fd3c7;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.line_password = QLineEdit(self.centralwidget)
        self.line_password.setObjectName(u"line_password")
        self.line_password.setReadOnly(True)

        self.horizontalLayout.addWidget(self.line_password)

        self.btn_refresh = QPushButton(self.centralwidget)
        self.btn_refresh.setObjectName(u"btn_refresh")
        icon1 = QIcon()
        icon1.addFile(u":/icons/resources/autorenew_black_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_refresh.setIcon(icon1)

        self.horizontalLayout.addWidget(self.btn_refresh)

        self.btn_copy = QPushButton(self.centralwidget)
        self.btn_copy.setObjectName(u"btn_copy")
        icon2 = QIcon()
        icon2.addFile(u":/icons/resources/content_copy_black_24dp.svg", QSize(), QIcon.Normal, QIcon.On)
        self.btn_copy.setIcon(icon2)

        self.horizontalLayout.addWidget(self.btn_copy)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.layout_info = QHBoxLayout()
        self.layout_info.setObjectName(u"layout_info")
        self.label_entropy = QLabel(self.centralwidget)
        self.label_entropy.setObjectName(u"label_entropy")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_entropy.sizePolicy().hasHeightForWidth())
        self.label_entropy.setSizePolicy(sizePolicy)
        self.label_entropy.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_entropy)

        self.label_strength = QLabel(self.centralwidget)
        self.label_strength.setObjectName(u"label_strength")
        sizePolicy.setHeightForWidth(self.label_strength.sizePolicy().hasHeightForWidth())
        self.label_strength.setSizePolicy(sizePolicy)
        self.label_strength.setAlignment(Qt.AlignCenter)

        self.layout_info.addWidget(self.label_strength)


        self.verticalLayout.addLayout(self.layout_info)

        self.layout_length = QHBoxLayout()
        self.layout_length.setObjectName(u"layout_length")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.layout_length.addWidget(self.label)

        self.slider_length = QSlider(self.centralwidget)
        self.slider_length.setObjectName(u"slider_length")
        self.slider_length.setCursor(QCursor(Qt.PointingHandCursor))
        self.slider_length.setValue(15)
        self.slider_length.setOrientation(Qt.Horizontal)

        self.layout_length.addWidget(self.slider_length)

        self.spinbox_length = QSpinBox(self.centralwidget)
        self.spinbox_length.setObjectName(u"spinbox_length")
        self.spinbox_length.setAlignment(Qt.AlignCenter)
        self.spinbox_length.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.spinbox_length.setValue(15)

        self.layout_length.addWidget(self.spinbox_length)


        self.verticalLayout.addLayout(self.layout_length)

        self.layout_characters = QHBoxLayout()
        self.layout_characters.setObjectName(u"layout_characters")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.layout_characters.addWidget(self.label_2)

        self.btn_lower = QPushButton(self.centralwidget)
        self.btn_lower.setObjectName(u"btn_lower")
        self.btn_lower.setCheckable(True)
        self.btn_lower.setChecked(True)

        self.layout_characters.addWidget(self.btn_lower)

        self.btn_upper = QPushButton(self.centralwidget)
        self.btn_upper.setObjectName(u"btn_upper")
        self.btn_upper.setCheckable(True)
        self.btn_upper.setChecked(True)

        self.layout_characters.addWidget(self.btn_upper)

        self.btn_digits = QPushButton(self.centralwidget)
        self.btn_digits.setObjectName(u"btn_digits")
        self.btn_digits.setCheckable(True)
        self.btn_digits.setChecked(True)

        self.layout_characters.addWidget(self.btn_digits)

        self.btn_punct = QPushButton(self.centralwidget)
        self.btn_punct.setObjectName(u"btn_punct")
        self.btn_punct.setCheckable(True)
        self.btn_punct.setChecked(False)

        self.layout_characters.addWidget(self.btn_punct)


        self.verticalLayout.addLayout(self.layout_characters)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Generator", None))
        self.line_password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Generated password", None))
        self.btn_refresh.setText("")
        self.btn_copy.setText("")
        self.label_entropy.setText("")
        self.label_strength.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Password length:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Include:", None))
        self.btn_lower.setText(QCoreApplication.translate("MainWindow", u"[a-z]", None))
        self.btn_upper.setText(QCoreApplication.translate("MainWindow", u"[A-Z]", None))
        self.btn_digits.setText(QCoreApplication.translate("MainWindow", u"[0-9]", None))
        self.btn_punct.setText(QCoreApplication.translate("MainWindow", u"[#@!$%...]", None))
    # retranslateUi

