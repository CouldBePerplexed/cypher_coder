from Analysis import Analysis

class Frequency(Analysis):
    def __calcNumOfChars(self):
        self.numOfChars = 0
        for char in self.dict.values():
            self.numOfChars += char[0]

    def __sort(self, ascending = False):
        # Bubble sort, might swap for heap later on
        keys = []
        values = []
        for key in self.dict:
            keys.append(key)
            values.append(self.dict.get(key))

        swapped = True
        if (ascending == True):
            while (swapped):
                i = 1
                swapped = False
                while (i < len(keys)):
                    if (values[i-1][0] > values[i][0]):
                        temp_key = keys[i-1]
                        temp_value = values[i-1]
                        keys[i-1] = keys[i]
                        values[i-1] = values[i]
                        keys[i] = temp_key
                        values[i] = temp_value
                        swapped = True
                    i+=1
        else:
            while (swapped):
                i = 1
                swapped = False
                while (i < len(keys)):
                    if (values[i-1][0] < values[i][0]):
                        temp_key = keys[i-1]
                        temp_value = values[i-1]
                        keys[i-1] = keys[i]
                        values[i-1] = values[i]
                        keys[i] = temp_key
                        values[i] = temp_value
                        swapped = True
                    i+=1

        i = 0
        newDict = {}
        while (i < len(keys)):
            newDict[keys[i]] = values[i]
            i += 1

        self.dict = newDict

    def __calcFreqInMessage(self):
        i = 0
        for key in self.dict:
            # Count of each char
            charCount = self.dict.get(key)
            charCount.append(charCount[0]/self.numOfChars)
            self.dict.update({key: charCount})
            i+=1
        

    # Creates a dictionary of all characters in the message, attaching an array for details for each char
    def calc(self, message = None):
        if (message != None):
            self.setMessage(message)
        else:
            if (self.message == None):
                return "Cannot do frequency analysis of no message"
        
        dictionary = {}
        for char in self.message:
            try:
                list(dictionary.keys()).index(char)
                dictionary[char][0] += 1
            except:
                dictionary[char] = [1]

        self.dict = dictionary
        self.__sort()
        self.__calcNumOfChars()
        self.__calcFreqInMessage()
        
        return "Calculated Frequency Successfully"

    def getNumOfChars(self):
        return self.numOfChars

    def getDict(self):
        return self.dict

    def printData(self):
        for key in self.dict:
            print("("+str(ord(key))+": "+key+":)", self.dict.get(key)[0], self.dict.get(key)[1]*100)