from Cipher import Cipher

class Caeser(Cipher):
    def __init__(self):
        self.shift = 0
        self.bruteforce = False

    def encrypt(self, message, shift = 0, right = True, ascii_range = [65, 90]):
        self.setAsciiRange(ascii_range)
        message = message.upper().strip()

        if (shift < 0 or shift > self.range[1]-self.range[0]):
            return "Must be between 0 and "+str(self.range[1]-self.range[0])

        ciphertext = ""

        i = 0
        if (right):
            print("--- Shifting to the right by",str(shift),"---")
        else:
            print("--- Shifting to the left by",str(shift),"---")
        for i in message:
            if (right): # Shift everything to the right
                if(i == " "): # if char is " " just add it
                    ciphertext+=i
                elif (ord(i)+shift <= self.range[1]): # is adding the shift within the range?
                    ciphertext+=chr(ord(i)+shift)
                else:
                    ciphertext+=chr(self.range[0]+((ord(i)+shift)-self.range[1]-1)) # Loop back to beginning of range
            else: # Shift everything to the left
                if(i == " "): # if char is " " just add it
                    ciphertext+=i
                elif (ord(i)-shift >= self.range[0]): # is adding the shift within the range?
                    ciphertext+=chr(ord(i)-shift)
                else:
                    ciphertext+=chr(self.range[1]-(self.range[0]-1 - (ord(i)-shift))) # Loop back to beginning of range
                

        return ciphertext

    def decrypt(self, message, shift = None, right = True):
        plaintext = ""
        if (shift == None): # Bruteforce
            print("--- Bruteforce ---")
            possible_plaintext = []
            shift = 0
            while (shift <= self.range[1]-self.range[0]):
                plaintext = ""
                for i in message:
                    if(i == " "): # if char is " " just add it
                        plaintext+=i
                    elif (ord(i)+shift <= self.range[1]): # is adding the shift within the range?
                        plaintext+=chr(ord(i)+shift)
                    else:
                        plaintext+=chr(self.range[0]+((ord(i)+shift)-self.range[1]-1)) # Loop back to beginning of range
                possible_plaintext.append(plaintext) 
                shift+=1
            return possible_plaintext
        else:
            if (right):
                print("--- Shifting to the right by",str(shift),"---")
            else:
                print("--- Shifting to the left by",str(shift),"---")
            
            for i in message:
                if (right): # Shift everything to the right
                    if(i == " "): # if char is " " just add it
                        plaintext+=i
                    elif (ord(i)+shift <= self.range[1]): # is adding the shift within the range?
                        plaintext+=chr(ord(i)+shift)
                    else:
                        plaintext+=chr(self.range[0]+((ord(i)+shift)-self.range[1]-1)) # Loop back to beginning of range
                else: # Shift everything to the left
                    if(i == " "): # if char is " " just add it
                        plaintext+=i
                    elif (ord(i)-shift >= self.range[0]): # is adding the shift within the range?
                        plaintext+=chr(ord(i)-shift)
                    else:
                        plaintext+=chr(self.range[1]-(self.range[0]-1 - (ord(i)-shift))) # Loop back to beginning of range
            return plaintext