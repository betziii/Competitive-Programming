class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.result = ""
    def insert(self, word: str) -> None:
        cur = self.root
        count = 0
        for w in word:
            if cur.children[ord(w) - ord("a")] is None:
                cur.children[ord(w) - ord("a")] = TrieNode() 
            if  cur.endOfWord:
                count += 1
            cur = cur.children[ord(w) - ord("a")]
        cur.endOfWord = True
        
        if count == len(word) - 1:
            a = word
            if len(a) > len(self.result):
                self.result = a
    def getResult(self):
        return self.result
            

class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        t = Trie()
        for word in words:
            t.insert(word)
        return t.getResult()