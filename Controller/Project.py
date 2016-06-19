

class Project:

    def __init__(self, name):
        self.name = name

    def __init__(self, name, path='', commits='', committers=''):
        self.commits = commits
        self.committers = committers
        self.name = name
        self.path = path
        self.vcs = None

    def setVcs(self, vcs):
        self.vcs = vcs

    def getVcs(self):
        return self.vcs

    def getCommits(self):
        return self.commits

    def getCommitters(self):
        return self.committers

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPath(self):
        return self.path
