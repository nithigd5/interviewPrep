
class Node:
         def __init__(self,data):
             self.data = data
             self.map = dict()
             self.isTerminal = False
             
class Trie:
    def __init__(self):
            self.root = Node('0')
    
    def insert(self,word):
            t = self.root
            for c in word:
                if not t.map.get(c,False):
                    t.map[c] = Node(c)
                t = t.map[c]
            t.isTerminal = True
    def search(self, word):
        t = self.root
        if(not t.map.get(word[0],False)):
            return -1;
        for c in word:
            if not t.map.get(c, False):
                 return t
            t = t.map[c]
        return t
    def get(self, word):
        t = self.root
        w = ""
        if(not t.map.get(word[0],False)):
            return -1;
        for c in word:
            if(not t.map.get(c,False)):
                break
            if t.isTerminal:
                break
            else:
                w += t.map[c].data
            t = t.map[c]
        if(t.isTerminal):
            return w
        else:
            return -1
