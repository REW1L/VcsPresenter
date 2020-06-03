import os

from views.commitwindow import Ui_CommitWindow
from Converters.Structures.FileChanges import *

from PySide2 import QtCore, QtWidgets

class CommitView(QtWidgets.QMainWindow, Ui_CommitWindow):

    def __init__(self, controller, hash, parent = None):
        super(CommitView, self).__init__(parent)
        self.setupUi(self)
        self.controller = controller
        self.hash = hash
        commit = controller.getCommit(hash)
        self.txtHash.setText(hash)
        self.txtAuthor.setText(commit.author)
        self.txtDate.setText(QtCore.QDateTime.fromTime_t(int(commit.timestamp)).toString("dd.MM.yyyy hh:mm"))
        self.txtDescription.setText(commit.description)
        self.lblLinesAdded.setText(commit.addedLines)
        if commit.deletedLines != '':
            self.lblLinesDeleted.setText(commit.deletedLines)
        else:
            self.lblLinesDeleted.setText("0")

        filesModel = QtWidgets.QFileSystemModel()
        filesModel.setRootPath(controller.project.getPath())
        dir = QtCore.QDir()
        nameFilters = [x.strip().split(os.sep)[-1] for x in self.controller.getDiff(hash)]
        if nameFilters == []:
            dir.setNameFilters([""])
        else:
            dir.setNameFilters(nameFilters)

        filesModel.setNameFilters(dir.nameFilters())
        print(dir.nameFilters())
        filesModel.setNameFilterDisables(False)

        self.treeFiles.setModel(filesModel)
        self.treeFiles.setRootIndex(filesModel.index(controller.project.getPath()))
        for i in range(1,4):
            self.treeFiles.hideColumn(i)

        self.treeFiles.activated.connect(self.fileDiff)

    @QtCore.Slot()
    def fileDiff(self, index):
        if not index.model().isDir(index):
            file = index.model().filePath(index)
            for line in self.controller.getDiff(firstCommit=self.hash, file=file).getLines():
                if line.status == Status.equal:
                    self.txtChanges.append("<font color=\"Black\">  "+line.line)
                elif line.status == Status.deleted:
                    self.txtChanges.append("<font color=\"Red\">- "+line.line)
                elif line.status == Status.added:
                    self.txtChanges.append("<font color=\"Green\">+ "+line.line)