from Cipher import Cipher
import numpy as np

class Vigenere(Cipher):
    # Initialise a Vigenere cipher with a Grid [B, C, D, ..., Y, Z, A]
                                            #  [C, D, E, ..., Z, A, B]
                                                    #     .
                                                    #     .
                                                    #     .
    def __init__(self, ascii_range = [65, 90]):
        self.setAsciiRange(ascii_range)
        grid = np.array([[""]*(self.range[1]-self.range[0]+1)]*(self.range[1]-self.range[0]+1), ndmin=2)

        x = 0
        start_letter = 0
        
        while x < grid.shape[0]:
            y = 0
            start_letter += 1
            for i in grid[x]:
                current_letter = start_letter + y + self.range[0]
                if (current_letter > self.range[1]):
                    current_letter = self.range[0] + (current_letter - self.range[1])-1
                grid[x, y] = chr(current_letter)
                y+=1
            x+=1

        self.grid = grid

    # Uses key set up prior or the key added in the method to encypt the message
    def encrypt(self, message, key = None):
        if (key != None):
            self.addKey(key)

        ciphertext = ""
        key_index = 0
        
        for letter in message:
            capitalised = False

            if (ord(letter.upper()) < self.range[0] or ord(letter.upper()) > self.range[1]):
                ciphertext += letter
                continue
                
            if (key_index >= len(self.key)):
                key_index = 0
            
            if (letter.upper() == letter):
                capitalised = True
                
            letter = letter.upper()

            if (capitalised):
                ciphertext += self.grid[ord(self.key[key_index])-self.range[0]-1, ord(letter)-self.range[0]]
            else:
                ciphertext += self.grid[ord(self.key[key_index])-self.range[0]-1, ord(letter)-self.range[0]].lower()

            key_index+=1
            
        return ciphertext
        
    def decrypt(self, message, key = None):
        if (key != None):
            self.addKey(key)

        plaintext = ""
        key_index = 0
        for letter in message:
            capitalised = False

            if (ord(letter.upper()) < self.range[0] or ord(letter.upper()) > self.range[1]):
                plaintext += letter
                continue
                
            if (key_index >= len(self.key)):
                key_index = 0
            
            if (letter.upper() == letter):
                capitalised = True
                
            letter = letter.upper()

            y = np.where(self.grid[ord(self.key[key_index])-self.range[0]-1] == letter)
            if (capitalised):
                plaintext += chr(y[0][0]+self.range[0])
            else:
                plaintext += chr(y[0][0]+self.range[0]).lower()
            
            key_index+=1
        
        return plaintext