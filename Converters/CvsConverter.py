from Converters.Structures.Converter import Converter


class CvsConverter(Converter):

    dir = ""
    commits = []
    committers = []

    def __init__(self, directory):
        self.dir = directory
        self.commits = []
        self.committers = []

    def getProjectCommits(self, branch=''):
        return "Not implemented"

    def getFilesDiff(self, startCommit, endCommit = ''):
        return "Not implemented"

    def getFileChanges(self, filePath, firstCommit, secondCommit=''):
        return "Not implemented"

    def getName(self):
        return "cvs"

    def getDirName(self):
        return ".cvs"

    def isValidPath(self, path='.'):
        return False

    def isEnabled(self):
        return False

    def getBranches(self):
        return "Not implemented"