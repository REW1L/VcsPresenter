# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(1600, 1200)
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(1600, 1200))
        MainWindow.setMaximumSize(QSize(1600, 1200))
        MainWindow.setBaseSize(QSize(1600, 1200))
        MainWindow.setAutoFillBackground(False)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        self.actionSearch = QAction(MainWindow)
        self.actionSearch.setObjectName(u"actionSearch")
        self.actionLil = QAction(MainWindow)
        self.actionLil.setObjectName(u"actionLil")
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayoutWidget = QWidget(self.centralWidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(10, 110, 321, 524))
        self.LeftMenu = QVBoxLayout(self.verticalLayoutWidget)
        self.LeftMenu.setSpacing(6)
        self.LeftMenu.setContentsMargins(11, 11, 11, 11)
        self.LeftMenu.setObjectName(u"LeftMenu")
        self.LeftMenu.setContentsMargins(0, 0, 0, 0)
        self.lblBrs = QLabel(self.verticalLayoutWidget)
        self.lblBrs.setObjectName(u"lblBrs")

        self.LeftMenu.addWidget(self.lblBrs)

        self.brComboBox = QComboBox(self.verticalLayoutWidget)
        self.brComboBox.setObjectName(u"brComboBox")
        self.brComboBox.setEnabled(False)

        self.LeftMenu.addWidget(self.brComboBox)

        self.lblDevs = QLabel(self.verticalLayoutWidget)
        self.lblDevs.setObjectName(u"lblDevs")

        self.LeftMenu.addWidget(self.lblDevs)

        self.devComboBox = QComboBox(self.verticalLayoutWidget)
        self.devComboBox.setObjectName(u"devComboBox")

        self.LeftMenu.addWidget(self.devComboBox)

        self.lblStartDate = QLabel(self.verticalLayoutWidget)
        self.lblStartDate.setObjectName(u"lblStartDate")

        self.LeftMenu.addWidget(self.lblStartDate)

        self.startDateEdit = QDateTimeEdit(self.verticalLayoutWidget)
        self.startDateEdit.setObjectName(u"startDateEdit")

        self.LeftMenu.addWidget(self.startDateEdit)

        self.lblEndDate = QLabel(self.verticalLayoutWidget)
        self.lblEndDate.setObjectName(u"lblEndDate")

        self.LeftMenu.addWidget(self.lblEndDate)

        self.endDateEdit = QDateTimeEdit(self.verticalLayoutWidget)
        self.endDateEdit.setObjectName(u"endDateEdit")

        self.LeftMenu.addWidget(self.endDateEdit)

        self.btnVisualize = QPushButton(self.verticalLayoutWidget)
        self.btnVisualize.setObjectName(u"btnVisualize")

        self.LeftMenu.addWidget(self.btnVisualize)

        self.btnReset = QPushButton(self.verticalLayoutWidget)
        self.btnReset.setObjectName(u"btnReset")

        self.LeftMenu.addWidget(self.btnReset)

        self.lblMenu = QLabel(self.centralWidget)
        self.lblMenu.setObjectName(u"lblMenu")
        self.lblMenu.setGeometry(QRect(10, 70, 148, 20))
        self.activityView = QGraphicsView(self.centralWidget)
        self.activityView.setObjectName(u"activityView")
        self.activityView.setGeometry(QRect(10, 640, 1580, 440))
        self.activityView.setMinimumSize(QSize(1580, 440))
        self.activityView.setMaximumSize(QSize(1580, 440))
        self.activityView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.activityView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.activityView.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.filesView = QTreeView(self.centralWidget)
        self.filesView.setObjectName(u"filesView")
        self.filesView.setGeometry(QRect(680, 190, 411, 431))
        self.commitsView = QListView(self.centralWidget)
        self.commitsView.setObjectName(u"commitsView")
        self.commitsView.setGeometry(QRect(360, 190, 281, 431))
        self.commitsView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.lblCommits = QLabel(self.centralWidget)
        self.lblCommits.setObjectName(u"lblCommits")
        self.lblCommits.setGeometry(QRect(430, 150, 148, 31))
        self.lblFiles = QLabel(self.centralWidget)
        self.lblFiles.setObjectName(u"lblFiles")
        self.lblFiles.setGeometry(QRect(840, 150, 71, 31))
        self.diffView = QTextBrowser(self.centralWidget)
        self.diffView.setObjectName(u"diffView")
        self.diffView.setGeometry(QRect(1130, 190, 441, 431))
        self.lblChanges = QLabel(self.centralWidget)
        self.lblChanges.setObjectName(u"lblChanges")
        self.lblChanges.setGeometry(QRect(1270, 140, 151, 51))
        self.btnOpenProject = QPushButton(self.centralWidget)
        self.btnOpenProject.setObjectName(u"btnOpenProject")
        self.btnOpenProject.setGeometry(QRect(10, 10, 291, 32))
        self.btnSaveDevs = QPushButton(self.centralWidget)
        self.btnSaveDevs.setObjectName(u"btnSaveDevs")
        self.btnSaveDevs.setEnabled(False)
        self.btnSaveDevs.setGeometry(QRect(310, 10, 341, 32))
        self.btnSearchCommit = QPushButton(self.centralWidget)
        self.btnSearchCommit.setObjectName(u"btnSearchCommit")
        self.btnSearchCommit.setEnabled(False)
        self.btnSearchCommit.setGeometry(QRect(570, 110, 241, 32))
        self.formLayoutWidget = QWidget(self.centralWidget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(1240, 10, 331, 131))
        self.lineChangeLayout = QFormLayout(self.formLayoutWidget)
        self.lineChangeLayout.setSpacing(6)
        self.lineChangeLayout.setContentsMargins(11, 11, 11, 11)
        self.lineChangeLayout.setObjectName(u"lineChangeLayout")
        self.lineChangeLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.lineChangeLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.lblLinesAffected = QLabel(self.formLayoutWidget)
        self.lblLinesAffected.setObjectName(u"lblLinesAffected")

        self.lineChangeLayout.setWidget(0, QFormLayout.FieldRole, self.lblLinesAffected)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.lineChangeLayout.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.lineChangeLayout.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.lblLinesDeleted = QLabel(self.formLayoutWidget)
        self.lblLinesDeleted.setObjectName(u"lblLinesDeleted")

        self.lineChangeLayout.setWidget(2, QFormLayout.FieldRole, self.lblLinesDeleted)

        self.lblLinesAdded = QLabel(self.formLayoutWidget)
        self.lblLinesAdded.setObjectName(u"lblLinesAdded")

        self.lineChangeLayout.setWidget(1, QFormLayout.FieldRole, self.lblLinesAdded)

        self.formLayoutWidget_2 = QWidget(self.centralWidget)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(840, 20, 364, 111))
        self.authorLayout = QFormLayout(self.formLayoutWidget_2)
        self.authorLayout.setSpacing(6)
        self.authorLayout.setContentsMargins(11, 11, 11, 11)
        self.authorLayout.setObjectName(u"authorLayout")
        self.authorLayout.setContentsMargins(0, 0, 0, 0)
        self.editAuthor = QLineEdit(self.formLayoutWidget_2)
        self.editAuthor.setObjectName(u"editAuthor")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.editAuthor.sizePolicy().hasHeightForWidth())
        self.editAuthor.setSizePolicy(sizePolicy1)
        self.editAuthor.setMinimumSize(QSize(250, 0))

        self.authorLayout.setWidget(0, QFormLayout.FieldRole, self.editAuthor)

        self.lblEmail = QLabel(self.formLayoutWidget_2)
        self.lblEmail.setObjectName(u"lblEmail")

        self.authorLayout.setWidget(1, QFormLayout.LabelRole, self.lblEmail)

        self.editEmail = QLineEdit(self.formLayoutWidget_2)
        self.editEmail.setObjectName(u"editEmail")
        sizePolicy1.setHeightForWidth(self.editEmail.sizePolicy().hasHeightForWidth())
        self.editEmail.setSizePolicy(sizePolicy1)
        self.editEmail.setMinimumSize(QSize(250, 0))

        self.authorLayout.setWidget(1, QFormLayout.FieldRole, self.editEmail)

        self.lblAuthor = QLabel(self.formLayoutWidget_2)
        self.lblAuthor.setObjectName(u"lblAuthor")

        self.authorLayout.setWidget(0, QFormLayout.LabelRole, self.lblAuthor)

        self.formLayoutWidget_3 = QWidget(self.centralWidget)
        self.formLayoutWidget_3.setObjectName(u"formLayoutWidget_3")
        self.formLayoutWidget_3.setGeometry(QRect(340, 50, 445, 44))
        self.commitLayout = QFormLayout(self.formLayoutWidget_3)
        self.commitLayout.setSpacing(6)
        self.commitLayout.setContentsMargins(11, 11, 11, 11)
        self.commitLayout.setObjectName(u"commitLayout")
        self.commitLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget_3)
        self.label.setObjectName(u"label")

        self.commitLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.editCommit = QLineEdit(self.formLayoutWidget_3)
        self.editCommit.setObjectName(u"editCommit")
        sizePolicy1.setHeightForWidth(self.editCommit.sizePolicy().hasHeightForWidth())
        self.editCommit.setSizePolicy(sizePolicy1)
        self.editCommit.setMinimumSize(QSize(320, 0))

        self.commitLayout.setWidget(0, QFormLayout.FieldRole, self.editCommit)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1600, 39))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QToolBar(MainWindow)
        self.mainToolBar.setObjectName(u"mainToolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Project visualization", None))
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"Save developers info", None))
        self.actionSearch.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.actionLil.setText(QCoreApplication.translate("MainWindow", u"lil", None))
        self.lblBrs.setText(QCoreApplication.translate("MainWindow", u"Branches", None))
        self.lblDevs.setText(QCoreApplication.translate("MainWindow", u"Developers", None))
        self.lblStartDate.setText(QCoreApplication.translate("MainWindow", u"Start date:", None))
        self.startDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.lblEndDate.setText(QCoreApplication.translate("MainWindow", u"End date:", None))
        self.endDateEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy", None))
        self.btnVisualize.setText(QCoreApplication.translate("MainWindow", u"Visualize", None))
        self.btnReset.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.lblMenu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.lblCommits.setText(QCoreApplication.translate("MainWindow", u"Commits", None))
        self.lblFiles.setText(QCoreApplication.translate("MainWindow", u"Files", None))
        self.lblChanges.setText(QCoreApplication.translate("MainWindow", u"Changes", None))
        self.btnOpenProject.setText(QCoreApplication.translate("MainWindow", u"Open project", None))
        self.btnSaveDevs.setText(QCoreApplication.translate("MainWindow", u"Save developers info", None))
        self.btnSearchCommit.setText(QCoreApplication.translate("MainWindow", u"Search for commit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lines affected:", None))
        self.lblLinesAffected.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Lines added:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Lines deleted:", None))
        self.lblLinesDeleted.setText("")
        self.lblLinesAdded.setText("")
        self.lblEmail.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.lblAuthor.setText(QCoreApplication.translate("MainWindow", u"Author:", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Commit:", None))
    # retranslateUi

