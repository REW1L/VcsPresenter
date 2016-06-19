from Controller.Project import Project
from Converters.Converters import Converters
from Converters.Structures.FileChanges import *


class Controller:

    projects = []
    converters = Converters()
    state = ''

    def __init__(self, project):
        self.state = 'init'
        self.project = [x for x in self.projects if x.getName() == project]
        if self.project == []:
            self.project = Project(project)
            self.projects.append(self.project)
        self.state = 'done'

    def setProjectVcs(self, path):
        self.state = 'setvcs'
        self.project.path = path
        self.project.vcs = self.converters.getConverter(path)
        self.state = 'done'

    def getProjectVcs(self):
        return self.project.getVcs()

    def configureProject(self):
        result = self.project.getVcs().getProjectCommits()
        self.project.commits = result['commits']
        self.project.committers = result['committers']

    def getAuthors(self):
        return self.project.getCommitters()

    def getCommits(self, firstCommit = '', endCommit = '', author='', branch=''):
        self.state = 'getcommits'
        add = False
        rezcommits = []
        if author == '':
            commits = self.project.getCommits()
        else:
            for x in self.project.getCommitters():
                if author == x.email:
                    commits = x.commits
                    break
        if firstCommit == '':
            firstCommit = commits[0].hash
        for commit in commits:
            if commit.hash == firstCommit:
                add = True
            if add:
                rezcommits.append(commit)
            if commit.hash == endCommit:
                break
        self.state = 'done'
        return rezcommits

    def getBranches(self):
        return self.project.vcs.getBranches()

    def getCommit(self, hash):
        for commit in self.project.getCommits():
            if commit.hash == hash:
                return commit

    def searchCommits(self, description):
        return [commit for commit in self.project.getCommits() if commit.description.find(description) != -1]

    def getDiff(self, firstCommit, endCommit='', author='', file=''):
        self.state='diff'
        if author != '':
            committer = [ com for com in self.project.getCommitters() if com.email == author]
            if file == '':
                diffs = []
                for commit in committer[0].commits:
                    for file in self.project.vcs.getFilesDiff(commit):
                        if file not in diffs:
                            diffs.append(file)
            else:
                diffs = FileChanges()
                rightCommits = False
                for commit in committer[0].commits:
                    rightCommits = (commit.hash == firstCommit)
                    if rightCommits:
                        for line in self.project.vcs.getFileChanges(file, commit).getLines():
                            diffs.addLine(line.number, line.status, line)
                    if commit.hash == endCommit:
                        break
        else:
            if file == '':
                diffs = self.project.vcs.getFilesDiff(firstCommit, endCommit)
            else:
                diffs = self.project.vcs.getFileChanges(file, firstCommit, endCommit)
        self.state = 'done'
        return diffs