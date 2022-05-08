class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.stringEnds=[]

    def insert(self, word):
        cur = self.root
        for w in word:
            cur = cur.children[w]
        self.stringEnds.append((cur,len(word)+1))

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        t = Trie()
        for w in set(words):
            t.insert(w[::-1])
        result = 0
        for curr,length in t.stringEnds:
            if not curr.children:
                result += length
        return result   