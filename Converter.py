# Uses frequency analysis to determine base of the message, then converts to decimal from there
from Cipher import Cipher
from Frequency import Frequency

class Converter(Cipher):

    def __calcBase(self):
        newDict = {};

        largestInt = -1;
        largestChar = chr(ord("A")-1)
        i = 0
        for char in self.dict:
            try: 
                if (largestInt < int(char)):
                    largestInt = int(char)
                    newDict.update({int(char): self.dict[char]}) 
            except:
                if (ord(largestChar) < ord(char.upper())):
                    largestChar = char.upper()
        if (largestInt <= 1):
            self.fromBase = 2
        elif (largestInt <= 7):
            self.fromBase = 8
        elif (largestInt <= 9):
            self.fromBase = 10
        
        if (ord(largestChar) >= ord("A")):
            if (ord(largestChar) <= ord("F")):
                self.fromBase = 16
            else:
                self.fromBase = "ascii"
        else:
            return
        
    def __init__(self, message = None):
        self.fromBase = None
        self.toBase = None
        self.freq = Frequency()
        if (message!=None):
            self.freq.calc(message.replace(" ", ""))
            self.dict = self.freq.getDict()
            self.message = message
            self.__calcBase()

    def setFromBase(self, newBase):
        self.fromBase = newBase
    def setToBase(self, newBase = None):
        try:
            if (newBase == None or newBase > 16 or newBase < 2):
                try:
                    newBase = int(input("Input to base: "))
                except:
                    print("Invalid int, setting to ascii")
                    newBase = 154998
        except:
            pass
        self.toBase = newBase

    def getFromBase(self, newBase):
        return self.fromBase
    def getToBase(self, newBase):
        return self.toBase
    
    def getMode(self):
        return str(self.fromBase)+" --> "+str(self.toBase)

    def encrypt(self, to_base = None, message = None):
        if (message != None):
            self.setMessage(message)
        
        if (self.message == None):
            response = input("Please input a message before encryption")
            self.setMessage(response)
        
        if (to_base != None or to_base > 16 or to_base < 2 or self.toBase == None):
            self.setToBase(to_base)

        decimal_values = []
        if (self.fromBase == "ascii"):
            for char in self.message:
                decimal_values.append(ord(char))
        else:
            for word in self.message.split(" "):
                decimal_value = 0
                index_value = 1
                try:
                    for char in word[::-1]:
                        decimal_value += int(char)*index_value
                        index_value *= self.fromBase
                    decimal_values.append(decimal_value)
                except:
                    decimal_values.append(int("0x"+word, self.fromBase))

        ciphertext = ""
        
        for dec in decimal_values:
            if (self.toBase == 2):
                ciphertext += f"{dec:b} "
            elif (self.toBase == 8):
                ciphertext += f"{dec:o} "
            elif (self.toBase == 10):
                ciphertext += f"{dec} "
            elif (self.toBase == 16):
                ciphertext += f"{dec:X} "
            else:
                test_value = self.toBase
                while (dec%test_value != dec):
                    test_value *= self.toBase
                
                while (test_value != 1):
                    test_value /= self.toBase
                    ciphertext += str(int(dec//test_value))
                    dec -= (dec//test_value)*test_value

                ciphertext += " "
        return ciphertext

    def decrypt(self, message = None):
        if (self.fromBase == "ascii"):
            return "Cannot decypt using an ascii characters"

        if (message != None):
            self.setMessage(message)
        
        if (self.message == None):
            response = input("Please input a message before decryption")
            self.setMessage(response)
        
        if (self.toBase == None):
            self.setToBase("ascii")

        decimal_values = []
        for word in self.message.split(" "):
            initial_value = 1
            decimal_value = 0
            try:
                for char in word[::-1]:
                    decimal_value += int(char) * initial_value
                    initial_value *= self.fromBase
                decimal_values.append(decimal_value)
            except:
                decimal_values.append(int("0x"+word, self.fromBase))

        plaintext = ""

        for dec in decimal_values:
            if (self.toBase == 2):
                plaintext += f"{dec:b} "
            elif (self.toBase == 8):
                plaintext += f"{dec:o} "
            elif (self.toBase == 10):
                plaintext += f"{dec} "
            elif (self.toBase == 16):
                plaintext += f"{dec:X} "
            elif (str(self.toBase) != self.toBase):
                test_value = self.toBase
                while (dec%test_value != dec):
                    test_value *= self.toBase
                
                while (test_value != 1):
                    test_value /= self.toBase
                    plaintext += str(int(dec//test_value))
                    dec -= (dec//test_value)*test_value

                plaintext += " "
            else:
                plaintext += chr(dec)
                

        return plaintext

    def setMessage(self, message):
        self.__init__(message)