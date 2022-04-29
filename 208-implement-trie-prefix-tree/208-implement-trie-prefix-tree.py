class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for w in word:
            if cur.children[ord(w) - ord("a")] is None:
                cur.children[ord(w) - ord("a")] = TrieNode() 
            cur = cur.children[ord(w) - ord("a")]
        cur.endOfWord = True
            
                

    def search(self, word: str) -> bool:
        cur = self.root
        
        for w in word:
            if cur.children[ord(w) - ord("a")] is None:
                return False
            cur = cur.children[ord(w) - ord("a")]
        if cur.endOfWord == True:
            return True
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        
        for w in prefix:
            if cur.children[ord(w) - ord("a")] is None:
                return False
            cur = cur.children[ord(w) - ord("a")]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)