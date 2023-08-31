# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(550, 350)
        Widget.setAcceptDrops(False)
        self.gridLayout = QGridLayout(Widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_2 = QPushButton(Widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setAcceptDrops(True)

        self.gridLayout.addWidget(self.pushButton_2, 3, 2, 1, 1)

        self.label_4 = QLabel(Widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 3)

        self.label_3 = QLabel(Widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.gridLayout.addWidget(self.label_3, 4, 1, 1, 1)

        self.pushButton_3 = QPushButton(Widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setAutoFillBackground(True)

        self.gridLayout.addWidget(self.pushButton_3, 6, 1, 1, 1)

        self.label_5 = QLabel(Widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout.addWidget(self.label_5, 1, 0, 1, 3)

        self.label_2 = QLabel(Widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_2.setWordWrap(True)

        self.gridLayout.addWidget(self.label_2, 4, 2, 1, 1)

        self.label_1 = QLabel(Widget)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_1.setWordWrap(True)

        self.gridLayout.addWidget(self.label_1, 4, 0, 1, 1)

        self.pushButton_1 = QPushButton(Widget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setAcceptDrops(True)

        self.gridLayout.addWidget(self.pushButton_1, 3, 0, 1, 1)

        self.progressBar = QProgressBar(Widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setTextDirection(QProgressBar.TopToBottom)

        self.gridLayout.addWidget(self.progressBar, 5, 0, 1, 3)


        self.retranslateUi(Widget)

        self.pushButton_3.setDefault(True)


        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"AI Covers", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"Style Image", None))
        self.label_4.setText(QCoreApplication.translate("Widget", u"AI Covers - make your own book/album covers with AI quickly and for free!", None))
        self.label_3.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Widget", u"Run neural-art", None))
        self.label_5.setText(QCoreApplication.translate("Widget", u"Pick two images to run neural-art on:", None))
        self.label_2.setText(QCoreApplication.translate("Widget", u"path/to/style", None))
        self.label_1.setText(QCoreApplication.translate("Widget", u"path/to/content", None))
        self.pushButton_1.setText(QCoreApplication.translate("Widget", u"Content Image", None))
    # retranslateUi

