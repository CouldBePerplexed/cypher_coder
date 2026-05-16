import numpy as np
import math
from Cipher import Cipher

class Nihilist(Cipher):
    def __init__(self):
        self.isRow = None
        self.key = None
        self.grid = grid = np.array([["A", "B", "C", "D", "E"], ["F", "G", "H", "I", "K"], ["L", "M", "N", "O", "P"], ["Q", "R", "S", "T", "U"], ["V", "W", "X", "Y", "Z"]])

    def addKey(self, key, row):
        # Edits key
        if (key != None):
            self.isRow = row
            self.key = key
            if (self.isRow):
                self.keyArr = self.__rowEncrypt(key)
            else:
                self.keyArr = self.__columnEncrypt(key)
        # Changes current key to relative type of encryption/decryption
        if (self.isRow != row):
            self.isRow = row
            
            if (self.isRow):
                self.keyArr = self.__rowEncrypt(self.key)
            else:
                self.keyArr = self.__columnEncrypt(self.key)

    def __rowEncrypt(self, message):
        # Encrypting Plaintext
        # creating one long string that replaces I's with J's (will add options later)
        message = message.upper().replace(" ", "").replace("J", "I")
        ciphertext = []
        
        i=0
        while (i < len(message)):
            # checks all items in the grid, left to right, top to bottom (row by row)
            j = 0
            while (j < 5):
                k = 0
                while (k < 5):
                    if (self.grid[j][k] == message[i]):
                        x = j+1
                        y = k+1
                        ciphertext.append(int(str(x)+str(y)))
                        break
                    k+=1
                k-=1
                if (self.grid[j][k] == message[i]):
                    break
                j+=1
            i+=1
        
        return ciphertext

    def __columnEncrypt(self, message):
        # Encrypting Plaintext
        # creating one long string that replaces I's with J's (will add options later)
        message = message.upper().replace(" ", "").replace("J", "I")
        ciphertext = []
        
        i=0
        while (i < len(message)):
            # checks all items in the grid, left to right, top to bottom (row by row)
            j = 0
            while (j < 5):
                k = 0
                while (k < 5):
                    if (self.grid[k][j] == message[i]):
                        x = j+1
                        y = k+1
                        ciphertext.append(int(str(x)+str(y)))
                        break
                    k+=1
                k-=1
                if (self.grid[k][j] == message[i]):
                    break
                j+=1
            i+=1
        
        return ciphertext
    
    def encrypt(self, message, key, row):
        if (key != None or self.row != row):
            self.addKey(key, row)
        
        if (row):
            ciphertext = self.__rowEncrypt(message)
        else:
            ciphertext = self.__columnEncrypt(message)
            pass

        i = 0
        j = 0
        encrypted = ""
        
        while (i < len(ciphertext)):
            if (j >= len(self.keyArr)):
                j = 0
            
            encrypted += str(ciphertext[i]+self.keyArr[j])+" "
            
            i+=1
            j+=1
        
        return encrypted

    def __rowDecrypt(self, message):
        plaintext = ""

        for item in message:
            plaintext+=self.grid[int(item[0])-1][int(item[1])-1]

        return plaintext

    def __columnDecrypt(self, message):
        plaintext = ""

        for item in message:
            plaintext+=self.grid[int(item[1])-1][int(item[0])-1]
        
        return plaintext
    
    def decrypt(self, message, key, row):
        if (key != None or self.isRow != row):
            self.addKey(key, row)
        
        message = message.split(" ")
        message = [int(x) for x in message]

        i = 0
        j = 0
        while (i < len(message)):
            if (j >= len(self.keyArr)):
                j=0
            message[i] -= self.keyArr[j]

            i+=1
            j+=1

        message = [str(x) for x in message]

        if (self.isRow):
            return self.__rowDecrypt(message)
        else:
            return self.__columnDecrypt(message)
