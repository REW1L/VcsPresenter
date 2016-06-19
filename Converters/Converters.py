import os
import re
from Converters.Structures.Converter import Converter

class Converters:

    available = []

    def __init__(self):
        for file in os.listdir(os.path.dirname(__file__)):
            name = os.path.splitext(os.path.basename(file))[0]
            if re.search(".*Converter$", name) != None:
                nameOfModule = "Converters." + name
                module = __import__(nameOfModule, globals(), locals(), [name, 'getName'])
                self.available.append(getattr(module, name))

    def getConverter(self, path):
        for conv in self.available:
            vcs = conv(path)
            if vcs.isEnabled() and vcs.isValidPath(path):
                return vcs
        return None