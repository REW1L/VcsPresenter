

class Commit:
    hash = ''
    timestamp = ''
    author = ''
    deletedLines = '0'
    addedLines = '0'
    description = ''
    changedFiles = ''

    def __init__(self, hash='', timestamp='', author='', description='', numberOfChangedFiles = '',
                 deletedLines='', addedLines=''):
        self.hash = hash
        self.timestamp = timestamp
        self.author = author
        self.deletedLines = deletedLines
        self.addedLines = addedLines
        self.description = description
        self.changedFiles = numberOfChangedFiles

    def __str__(self):
        return self.hash + "\n" + self.timestamp + "\n" + self.author + "\n" + \
               self.deletedLines + "\n" + self.addedLines