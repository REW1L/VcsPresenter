# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'commitwindow.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_CommitWindow(object):
    def setupUi(self, CommitWindow):
        if not CommitWindow.objectName():
            CommitWindow.setObjectName(u"CommitWindow")
        CommitWindow.resize(1439, 698)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(CommitWindow.sizePolicy().hasHeightForWidth())
        CommitWindow.setSizePolicy(sizePolicy)
        CommitWindow.setMinimumSize(QSize(1439, 698))
        CommitWindow.setMaximumSize(QSize(1439, 698))
        self.formLayoutWidget = QWidget(CommitWindow)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 80, 498, 494))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.txtHash = QLineEdit(self.formLayoutWidget)
        self.txtHash.setObjectName(u"txtHash")
        self.txtHash.setMinimumSize(QSize(300, 0))
        self.txtHash.setMaximumSize(QSize(240, 16777215))
        self.txtHash.setReadOnly(True)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.txtHash)

        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.txtDate = QLineEdit(self.formLayoutWidget)
        self.txtDate.setObjectName(u"txtDate")
        self.txtDate.setMinimumSize(QSize(300, 0))
        self.txtDate.setMaximumSize(QSize(240, 16777215))
        self.txtDate.setReadOnly(True)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.txtDate)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_2)

        self.txtTime = QLineEdit(self.formLayoutWidget)
        self.txtTime.setObjectName(u"txtTime")
        self.txtTime.setMinimumSize(QSize(300, 0))
        self.txtTime.setMaximumSize(QSize(240, 16777215))
        self.txtTime.setReadOnly(True)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.txtTime)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.txtAuthor = QLineEdit(self.formLayoutWidget)
        self.txtAuthor.setObjectName(u"txtAuthor")
        self.txtAuthor.setMinimumSize(QSize(300, 0))
        self.txtAuthor.setMaximumSize(QSize(240, 16777215))
        self.txtAuthor.setReadOnly(True)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.txtAuthor)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_5)

        self.label_8 = QLabel(self.formLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_8)

        self.lblLinesAdded = QLabel(self.formLayoutWidget)
        self.lblLinesAdded.setObjectName(u"lblLinesAdded")

        self.formLayout.setWidget(5, QFormLayout.FieldRole, self.lblLinesAdded)

        self.label_9 = QLabel(self.formLayoutWidget)
        self.label_9.setObjectName(u"label_9")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_9)

        self.lblLinesDeleted = QLabel(self.formLayoutWidget)
        self.lblLinesDeleted.setObjectName(u"lblLinesDeleted")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.lblLinesDeleted)

        self.txtDescription = QTextBrowser(self.formLayoutWidget)
        self.txtDescription.setObjectName(u"txtDescription")
        self.txtDescription.setMinimumSize(QSize(300, 0))
        self.txtDescription.setMaximumSize(QSize(1000, 16777215))

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.txtDescription)

        self.treeFiles = QTreeView(CommitWindow)
        self.treeFiles.setObjectName(u"treeFiles")
        self.treeFiles.setGeometry(QRect(550, 80, 341, 601))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.treeFiles.sizePolicy().hasHeightForWidth())
        self.treeFiles.setSizePolicy(sizePolicy1)
        self.treeFiles.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.treeFiles.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.label_6 = QLabel(CommitWindow)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(680, 40, 71, 31))
        self.label_7 = QLabel(CommitWindow)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(170, 40, 71, 41))
        self.label_12 = QLabel(CommitWindow)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(1110, 40, 121, 41))
        self.txtChanges = QTextBrowser(CommitWindow)
        self.txtChanges.setObjectName(u"txtChanges")
        self.txtChanges.setGeometry(QRect(930, 80, 491, 601))

        self.retranslateUi(CommitWindow)

        QMetaObject.connectSlotsByName(CommitWindow)
    # setupUi

    def retranslateUi(self, CommitWindow):
        CommitWindow.setWindowTitle(QCoreApplication.translate("CommitWindow", u"Commit", None))
        self.label_4.setText(QCoreApplication.translate("CommitWindow", u"Hash", None))
        self.label.setText(QCoreApplication.translate("CommitWindow", u"Date:", None))
        self.label_2.setText(QCoreApplication.translate("CommitWindow", u"Time:", None))
        self.label_3.setText(QCoreApplication.translate("CommitWindow", u"Author:", None))
        self.label_5.setText(QCoreApplication.translate("CommitWindow", u"Description:", None))
        self.label_8.setText(QCoreApplication.translate("CommitWindow", u"Lines added:", None))
        self.lblLinesAdded.setText("")
        self.label_9.setText(QCoreApplication.translate("CommitWindow", u"Lines deleted:", None))
        self.lblLinesDeleted.setText("")
        self.label_6.setText(QCoreApplication.translate("CommitWindow", u"Files:", None))
        self.label_7.setText(QCoreApplication.translate("CommitWindow", u"Info:", None))
        self.label_12.setText(QCoreApplication.translate("CommitWindow", u"Changes:", None))
    # retranslateUi

