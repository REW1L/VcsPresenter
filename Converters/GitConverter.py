import os
import re
import subprocess

from Converters.Structures import *

class GitConverter(Converter):

    dir = ""
    commits = []
    committers = []

    def __init__(self, directory):
        self.dir = directory
        self.commits = []
        self.committers = []

    def getProjectCommits(self, branch=''):
        workdir = os.getcwd()
        os.chdir(self.dir)
        if branch == '':
            branch = '--all'
        with subprocess.Popen(["git", "log", "--pretty=format:git<!>%cn<!>%ce<!>%H<!>%s<!>%at", "--shortstat", branch],
                              stdout=subprocess.PIPE, universal_newlines=True) as git:
            for line in git.stdout.readlines():
                line = line.strip()
                lines = line.split('<!>')
                if lines.__len__() > 1:
                    # adding commit
                    commit = Commit(lines.__getitem__(3), lines.__getitem__(5),
                                    lines.__getitem__(2), lines.__getitem__(4))
                    self.commits.append(commit)

                    # adding committer
                    committer = Committer(lines.__getitem__(1), lines.__getitem__(2))
                    com = [com for com in self.committers if com.email == committer.email]
                    if com.__len__() > 0:
                        com[0].commits.append(commit)
                    else:
                        committer.commits.append(commit)
                        self.committers.append(committer)
                else:
                    #adding additional info to commit
                    lines = line.split(', ')
                    if lines.__len__() > 1:
                        commit.changedFiles = lines[0].strip().split(' ')[0]
                        commit.addedLines = lines[1].strip().split(' ')[0]
                    if lines.__len__() > 2:
                        commit.deletedLines = lines[2].strip().split(' ')[0]
        os.chdir(workdir)
        rez = {"commits": self.commits, "committers": self.committers}
        return rez

    def getFilesDiff(self, startCommit, endCommit = ''):
        workdir = os.getcwd()
        os.chdir(self.dir)
        if endCommit == '':
            lines = subprocess.Popen(["git", "show", startCommit, "--pretty=format:", "--name-only"],
                                  stdout=subprocess.PIPE, universal_newlines=True).stdout.readlines()
        else:
            lines = subprocess.Popen(["git", "diff", startCommit, endCommit, "--name-only"],
                                  stdout=subprocess.PIPE, universal_newlines=True).stdout.readlines()
        os.chdir(workdir)
        return lines

    def getFileChanges(self, filePath, firstCommit, secondCommit=''):
        workdir = os.getcwd()
        os.chdir(self.dir)
        fileChanges = FileChanges()
        if secondCommit == '':
            git = subprocess.Popen(["git", "show", firstCommit, "--pretty=format:", "--color=never", "--", filePath],
                                  stdout=subprocess.PIPE, universal_newlines=True)
        else:
            git = subprocess.Popen(["git", "diff", firstCommit, secondCommit, "--pretty=format:", "--color=never", "--", filePath],
                                  stdout=subprocess.PIPE, universal_newlines=True)
        stage = 0
        for line in git.stdout.readlines():
            newChanges = re.search('@@ ([0-9-,+ ]+) @@(.*)', line)
            if newChanges != None:
                # print("new changes "+ line)
                stage = 1
                lineChanges = newChanges.group(1).split()
                linedelnum = int(lineChanges[0].split(",")[0][1:])
                lineaddnum = int(lineChanges[1].split(",")[0][1:])
                linenum = lineaddnum
                # fileChanges.addLine(linenum, Status.equal, newChanges.group(2) + "\n")
            elif stage == 1:
                if line[0] == '-':
                    fileChanges.addLine(linedelnum, Status.deleted, line[1:])
                    linedelnum += 1
                elif line[0] == '+':
                    fileChanges.addLine(lineaddnum, Status.added, line[1:])
                    lineaddnum += 1
                    linenum += 1
                elif line[0] == ' ':
                    fileChanges.addLine(lineaddnum, Status.equal, line[1:])
                    lineaddnum += 1
                    linedelnum += 1
                else:
                    stage = 0
        os.chdir(workdir)
        return fileChanges

    def getName(self):
        return "git"

    def getDirName(self):
        return ".git"

    def isValidPath(self, path='.'):
        workdir = os.getcwd()
        if path != '.':
            os.chdir(path)
        with subprocess.Popen(["git", "status"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True) as git:
            os.chdir(workdir)
            errorLines = git.stderr.readlines()
            if errorLines.__len__() > 0:
                return False
            else:
                return True

    def isEnabled(self):
        try:
            subprocess.Popen(["git"], stdout=subprocess.PIPE) # try to open program of vcs
        except FileNotFoundError:
            return False
        return True

    def getBranches(self):
        workdir = os.getcwd()
        os.chdir(self.dir)
        branches = []
        with subprocess.Popen(["git", "br", "--color=never"], stdout=subprocess.PIPE, universal_newlines=True) as git:
            for line in git.stdout.readlines():
                branches.append(line.strip().split()[-1])
        os.chdir(workdir)
        return branches