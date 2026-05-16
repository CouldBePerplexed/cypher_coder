class TreeNode:
    def __init__(self, data = None):
        self.data = data

    def getData(self):
        return self.data
    def getChildren(self):
        return [self.left, self.right]
    
    def addLeft(self, left):
        self.left = left
    def addRight(self, right):
        self.right = right

    # Pre-order DFS for contains    
    # Determines if current node contains the value being searched
    # if not, checks if the left node or right node contain the value
    def contains(self, data, text):
        if (self.data == data): 
            return True, text

        try:
            left = self.left
            doesContain, text = left.contains(data, text)
            if(doesContain):
                text += "."
                return True, text
        except:
            pass
        
        try:
            right = self.right
            doesContain, text = right.contains(data, text)
            if(doesContain):
                text += "-"
                return True, text
        except:
            pass
        return False, text

    # Prints all data from the left and right nodes
    def printData(self):
        level = 0
        print (f"Level {level}: {self.data}")
        try:
            self.left.printDataRec(level+1)
        except:
            pass

        try:
            self.right.printDataRec(level+1)
        except:
            pass
    
    def printDataRec(self,level):
        print (f"Level {level}: {self.data}")
        try:
            self.left.printDataRec(level+1)
        except:
            pass

        try:
            self.right.printDataRec(level+1)
        except:
            pass

class Tree:
    def __init__(self, root = None):
        self.root = root

    def __dfs_addition(self, array, node, level):
        if (level < 5):
            left = TreeNode(array.pop(0))
            self.__dfs_addition(array, left, level+1)
            node.addLeft(left)
            
            right = TreeNode(array.pop(0))
            self.__dfs_addition(array, right, level+1)
            node.addRight(right)
    
        return node
    
    def createTree(self, array, dfs = True):
        root = TreeNode(None)
        level = 0
        
        dfs_array = array
        try:
            left = TreeNode(dfs_array.pop(0))
            left = self.__dfs_addition(dfs_array, left, level+1)
            root.addLeft(left)
    
            right = TreeNode(dfs_array.pop(0))
            right = self.__dfs_addition(dfs_array, right, level+1)
            root.addRight(right)
        except Exception as e:
            print("loading failure:",e)
        
        return root