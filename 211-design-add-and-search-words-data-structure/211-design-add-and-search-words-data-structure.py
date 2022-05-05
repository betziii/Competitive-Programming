class TrieNode:
    def __init__(self):
        self.children =  {}
        self.isEndWord = False
    # self.value = ""
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isEndWord = True
        
    def dfs(self, index,word, cur):
        for i in range(index, len(word)):
            w = word[i]
            if w == ".":
                for w in cur.children:
                    if self.dfs(i + 1, word, cur.children[w]):
                        return True
                return False
            if w not in cur.children:
                return False
            cur = cur.children[w]
        return cur.isEndWord == True
            
    
    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)
    


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)