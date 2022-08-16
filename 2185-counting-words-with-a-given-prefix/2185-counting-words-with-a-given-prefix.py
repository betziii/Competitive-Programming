class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.count = 0

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        root = TrieNode()
        
        for w in words:
            node = root
            for c in w:
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                node.count += 1
        
        node = root

        for c in pref:
            if c in node.children:
                node = node.children[c]
            else:
                return 0
                
        return node.count