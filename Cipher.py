from abc import ABC, abstractmethod 

class Cipher(ABC):
    def setAsciiRange(self, ascii_range):
        self.range = ascii_range
    
    def setKey(self, key):
        self.key = key.upper()

    def setMessage(self, message):
        self.message = message

    def getMessage(self):
        return self.message
    
    @abstractmethod
    def encrypt(self, message):
        pass

    @abstractmethod
    def decrypt(self, message):
        pass