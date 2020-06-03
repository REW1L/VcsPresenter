import os
import datetime

from views.mainwindow import Ui_MainWindow
from Controller.Controller import Controller
from Converters.Structures.FileChanges import *
from views.commitview import CommitView

from PySide2 import QtWidgets, QtCore, QtGui


class MainView(QtWidgets.QMainWindow, Ui_MainWindow):

    def __init__(self, parent = None):
        super(MainView, self).__init__(parent)
        self.setupUi(self)
        palette = QtGui.QPalette()
        # palette.setColor(QtGui.QPalette.Background, QtGui.QColor(0x5e490f))
        self.setAutoFillBackground(True)
        self.setPalette(palette)
        self.windows = []

        # self.activityView.setBackgroundBrush(QtWidgets.QBrush(QtWidgets.QColor(0x302608)))
        # self.activityView.drawBackground(QtWidgets.QPainter(), QtCore.QRectF(0, 0, self.activityView.maximumWidth(),
        #                                                                self.activityView.maximumHeight()))
        self.btnOpenProject.clicked.connect(self.openProject)
        self.commitsView.doubleClicked.connect(self.showCommitInfo)
        self.filesView.activated.connect(self.fileDiff)
        self.btnVisualize.clicked.connect(self.visualize)
        self.commitLayout.parent().hide()
        self.authorLayout.parent().hide()
        self.activityView.setScene(QtWidgets.QGraphicsScene())
        self.controller = None



    @QtCore.Slot()
    def openProject(self):
        dialog = QtWidgets.QFileDialog()
        dialog.setFileMode(QtWidgets.QFileDialog.Directory)
        dialog.setOption(QtWidgets.QFileDialog.ShowDirsOnly, True)
        path = dialog.getExistingDirectory(self, "Select Directory")
        if path != '':
            projectName = path.split(os.pathsep)[-1]
            controller = Controller(projectName)
            controller.setProjectVcs(path)
            controller.configureProject()
            self.controller = controller
            commits = controller.getCommits()
            lastCommit = commits[0]
            firstCommit = commits[0]
            for x in commits:
                if x.timestamp < firstCommit.timestamp:
                    firstCommit = x
                if x.timestamp > lastCommit.timestamp:
                    lastCommit = x
            minDate = QtCore.QDateTime.fromTime_t(int(firstCommit.timestamp))
            maxDate = QtCore.QDateTime.fromTime_t(int(lastCommit.timestamp))
            self.startDateEdit.setDateTimeRange(minDate, maxDate)
            self.startDateEdit.setDateTime(minDate)
            self.endDateEdit.setDateTimeRange(minDate, maxDate)
            self.endDateEdit.setDateTime(maxDate)

            self.brComboBox.addItems(["all"] + self.controller.getBranches())

            self.devComboBox.addItems(["all"] + [x.email for x in self.controller.getAuthors()])

            self.outCommitFiles(commits)

            self.drawLines(commits)

    def outCommitFiles(self, commits):
        filesModel = QtWidgets.QFileSystemModel()
        filesModel.setNameFilterDisables(False)
        filesModel.setRootPath(self.controller.project.getPath())
        dir = QtCore.QDir()
        filesModel.setNameFilterDisables(False)
        if commits == []:
            dir.setNameFilters("[!@#$%^&*]+.[/]+")
        else:
            firstCommit = commits[-1]
            lastCommit = commits[0]

            self.commitsView.setModel(QtCore.QStringListModel([x.hash for x in commits]))
            dir.setNameFilters([x.strip().split(os.sep)[-1] for x in self.controller.getDiff(firstCommit.hash, lastCommit.hash)])
        filesModel.setNameFilters(dir.nameFilters())
        self.filesView.setModel(filesModel)
        self.filesView.setRootIndex(filesModel.index(self.controller.project.getPath()))
        for i in range(1,4):
            self.filesView.hideColumn(i)

    def drawLines(self, commits):
        affectedLines = []
        alladded = 0
        alldeleted = 0
        commitsCount = commits.__len__()

        for commit in commits:
            if commit.addedLines != '':
                added = int(commit.addedLines)
            else:
                added = 0
            if commit.deletedLines != '':
                deleted = int(commit.deletedLines)
            else:
                deleted = 0

            alldeleted += deleted
            alladded += added
            affectedLines.append({'deleted': deleted, 'added': added})

        self.lblLinesAdded.setText(str(alladded))
        self.lblLinesDeleted.setText(str(alldeleted))
        self.lblLinesAffected.setText(str(alldeleted+alladded))

        scene = self.activityView.scene()
        scene.clear()
        self.activityView.viewport().update()

        if commitsCount > 0:
            max_y = 0
            for a in affectedLines:
                if a['deleted'] > max_y:
                    max_y = a['deleted']
                if a['added'] > max_y:
                    max_y = a['added']
            xshift = self.activityView.minimumWidth()/commitsCount
            if max_y >= self.activityView.minimumHeight():
                yshift = (self.activityView.minimumHeight()-22)/(max_y+1)
            else:
                yshift = 1

            addedQPen = QtGui.QPen(QtGui.QColor(0x00FF00))
            deletedQPen = QtGui.QPen(QtGui.QColor(0xFF0000))
            addedQPen.setWidth(3)
            deletedQPen.setWidth(3)
            height = self.activityView.minimumHeight() - 22
            startadd = [0,height]
            startdel = [0,height]
            for a in affectedLines:
                scene.addLine(startadd[0], startadd[1], startadd[0]+xshift, height - a['added']*yshift, addedQPen)
                scene.addLine(startdel[0], startdel[1], startdel[0]+xshift, height - a['deleted']*yshift, deletedQPen)
                startadd[0] += xshift
                startdel[0] = startadd[0]
                startadd[1] = height - a['added']*yshift
                startdel[1] = height - a['deleted']*yshift


    @QtCore.Slot()
    def fileDiff(self, index):
        if not index.model().isDir(index):
            file = index.model().filePath(index)
            branch = self.brComboBox.itemText(self.brComboBox.currentIndex())
            if branch == "all":
                branch = ''
            committer = self.devComboBox.itemText(self.devComboBox.currentIndex())
            if committer == "all":
                committer = ''
            startCommit = ''
            endCommit = ''

            for commit in self.controller.getCommits():
                if startCommit == '' and int(commit.timestamp) >= self.startDateEdit.dateTime().toTime_t():
                    startCommit = commit.hash

                if endCommit == '' and int(commit.timestamp) <= self.startDateEdit.dateTime().toTime_t():
                    endCommit = commit.hash
            self.diffView.setText("")
            for line in self.controller.getDiff(endCommit, startCommit, committer, file).getLines():
                if line.status == Status.equal:
                    self.diffView.append("<font color=\"Black\">  "+line.line)
                elif line.status == Status.deleted:
                    self.diffView.append("<font color=\"Red\">- "+line.line)
                elif line.status == Status.added:
                    self.diffView.append("<font color=\"Green\">+ "+line.line)

    @QtCore.Slot()
    def showCommitInfo(self, index):
        hash = index.model().itemData(index)[0]
        view = CommitView(self.controller, hash)
        view.show()
        self.windows.append(view)

    @QtCore.Slot()
    def visualize(self):
        branch = self.brComboBox.itemText(self.brComboBox.currentIndex())
        if branch == "all":
            branch = ''
        committer = self.devComboBox.itemText(self.devComboBox.currentIndex())

        if committer == "all":
            committer = ''
        startCommit = ''
        endCommit = ''
        lastCommit = None
        commits = self.controller.getCommits(author=committer)
        for commit in reversed(commits):
            if endCommit == '' and int(commit.timestamp) >= self.startDateEdit.dateTime().toTime_t():
                endCommit = commit.hash

            if startCommit == '' and int(commit.timestamp) >= self.endDateEdit.dateTime().toTime_t():
                if lastCommit != None and int(commit.timestamp) != self.endDateEdit.dateTime().toTime_t():
                    startCommit = lastCommit.hash
                else:
                    startCommit = commit.hash
                break
            lastCommit = commit
        commits = self.controller.getCommits(startCommit, endCommit, committer)
        self.outCommitFiles(commits)
        self.drawLines(commits)