class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndWord = False

class Solution:
    def removeSubfolders(self, folders: List[str]) -> List[str]:
        self.root = TrieNode()
        for f in folders:
            cur = self.root
            
            word = f.split('/')
            for w in word:
                if w not in cur.children:
                    cur.children[w] = TrieNode()
                cur = cur.children[w]
            cur.isEndWord = True
            
        
        result = []
        for f in folders:
            cur = self.root
            flag = False
            word = f.split('/')
            for i in range(len(word)):           
                if word[i] in cur.children:
                    cur = cur.children[word[i]]
                if cur.isEndWord and i < len(word)-1:
                    flag = True
                    break
            
            if not flag:
                result.append(f)
                    
        return result