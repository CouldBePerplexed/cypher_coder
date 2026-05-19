from abc import ABC, abstractmethod

class Analysis(ABC):
    def __init__(self, message = None):
        self.message = message

    def getMessage(self):
        return self.message

    def setMessage(self, message):
        self.message = message
    