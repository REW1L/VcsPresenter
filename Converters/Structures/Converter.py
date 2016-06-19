from abc import ABCMeta, abstractmethod, abstractproperty


class Converter(metaclass=ABCMeta):

    @abstractproperty
    def dir(self):
        pass

    @abstractproperty
    def commits(self):
        pass

    @abstractproperty
    def committers(self):
        pass

    @abstractmethod
    def getProjectCommits(self, branch=''):
        pass

    @abstractmethod
    def __init__(self, directory):
        pass

    @abstractmethod
    def getFilesDiff(self, startCommit, endCommit = ''):
        pass

    @abstractmethod
    def getFileChanges(self, filePath, firstCommit, secondCommit=''):
        pass

    @abstractmethod
    def getName(self):
        pass

    @abstractmethod
    def getDirName(self):
        pass

    @abstractmethod
    def isValidPath(self, path='.'):
        pass

    @abstractmethod
    def isEnabled(self):
        pass

    @abstractmethod
    def getBranches(self):
        pass