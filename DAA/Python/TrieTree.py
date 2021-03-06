class Trie:
    def __init__(self):
        self.root = {}
        self.endmarker = "$"

    def AddWord(self,word):
        temp = self.root
        for i in word:
            try:
                _ = temp[i]
            except:
                temp[i] = {} 
            temp[self.endmarker] = temp.get(self.endmarker,0) +  1
            temp = temp[i] 
        temp[self.endmarker] = temp.get(self.endmarker,0) +  1


    def FindLike(self,word):
        temp = self.root
        for i in word:
            try:
                temp = temp[i]
            except:
                return 0
        if("$" not in temp.keys()):return 0
        return temp["$"]