class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndWord = False
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root
        
        for w in word:
            if cur.children[ord(w) - ord("a")] is None:
                cur.children[ord(w) - ord("a")] = TrieNode()
            cur = cur.children[ord(w) - ord("a")] 
        cur.isEndWord = True
        
    def search(self, word):
        cur = self.root
        
        for w in word:
            if cur.children[ord(w) - ord("a")] is None:
                return False
            cur = cur.children[ord(w) - ord("a")] 
        if cur.isEndWord == True:
            return True
        else:
            return False
    

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        t = Trie()
        answer1 = defaultdict(int)
        
        for w in words:
            if t.search(w):
                answer1[w] += 1
            else:
                t.insert(w)
                answer1[w] += 1
        
        sortedAnswer = list(OrderedDict(sorted(answer1.items(), key = lambda x: (-x[1], x[0]))))
        return (sortedAnswer[:k])
            
        