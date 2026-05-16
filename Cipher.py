from abc import ABC, abstractmethod 

class Cipher(ABC):
    def addKey(self, key):
        self.key = key.upper()
    
    @abstractmethod
    def encrypt(self, message):
        pass

    @abstractmethod
    def decrypt(self, message):
        pass