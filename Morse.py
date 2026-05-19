from Cipher import Cipher
from Tree import Tree

class Morse(Cipher):    
    def __init__(self):
        self.root = Tree().createTree(["E", "I", "S", "H", "5", "4", "V", None, "3", "U", "F", None, None, None, None, "2", "A", "R", "L", None, None, None, None, None, "W", "P", None, None, "J", None, "1", "T", "N", "D", "B", "6", None, "X", None, None, "K", None, None, None, "Y", None, None, "M", "G", "Z", "7", None, "Q", None, None, "O", None, "8", None, None, "9", "0"])
    # Prints whole tree
    def printTree(self):
        self.root.printData()

    # Converts morse to plaintext
    def decrypt(self, message):
        improper = False

        if "/" in message:
            message = message.split("/")
        else:
            message = message.split(" ")
            improper = True

        plaintext = []
        for words in message:
            letters = words.strip().split(" ")
            
            plainword = []
            for character in letters:
                if (len(character) > 5):
                    plainword.append("#")
                    continue
                
                i = 0
                temp_node = self.root
                while (i < len(character)):
                    if (character[i] == "."):
                        temp_node = temp_node.left
                        i+=1
                    else:
                        temp_node = temp_node.right
                        i+=1
                
                if (temp_node.data != None):
                    plainword.append(temp_node.data)
                else:
                    plainword.append("#")
            plaintext.append(''.join(plainword))
        
        temp = ""
        if (improper == False):
            for word in plaintext:
                temp += (word)+" "
        else:
            for word in plaintext:
                temp += word
        
        return temp

    # Converts plaintext to morse
    def encrypt(self, message):        
        message = message.upper()
        message = message.replace(" ", "/")
        message = list(message)

        ciphertext = ""
        for character in message:
            char = ""
            if (character == "/"):
                char = "/"
            else: 
                doesContain, char = self.root.contains(character, char)
                if (doesContain):
                    char = char[::-1]
                else:
                    char = "#"
            ciphertext += char+" "
        return ciphertext