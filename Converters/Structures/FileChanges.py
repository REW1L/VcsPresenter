from enum import Enum

class Status(Enum):
    equal = 0
    deleted = 1
    added = 2

class Line:
    number = 0
    status = Status.equal
    line = ""

    def __init__(self, number, status, line):
        self.number = number
        self.status = status
        self.line = line

class FileChanges:

    def __init__(self):
        self.lines = []

    def addLine(self, lineNumber, status, line):
        self.lines.append(Line(lineNumber, status, line))

    def __str__(self):
        rez = ''
        tempNumber = 0
        for line in self.lines:
            if line.number > tempNumber+1:
                rez += "<...>\n"
            rez += str(line.number) + " " + str(line.status) + line.line
            tempNumber = line.number
        return rez

    def replaceLine(self, lineNumber, oldStatus, newStatus, newLine):
        for index, line in enumerate(self.lines):
            if line.number == lineNumber and line.status == oldStatus:
                self.lines[index] = newLine
                break

    def getLinesByNum(self, lineNumber):
        return [line for line in self.lines if line.number == lineNumber]

    def getLines(self):
        return self.lines