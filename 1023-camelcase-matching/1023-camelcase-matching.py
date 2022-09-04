class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = None
        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, pattern):
        current = self.root
        p_index = 0
        follow_pattern = True
        for letter in word:
            if p_index < len(pattern) and letter == pattern[p_index]:
                p_index += 1
            elif p_index < len(pattern) and letter.isupper() and letter != pattern[p_index]:
                # Case for "ForceFeedBack" and "FB" as pattern
                follow_pattern = False
            elif p_index == len(pattern) and letter.isupper():
                # Case for "FooBarTest" and "FB" as pattern
                follow_pattern = False
            current = current.children[letter]
        current.word = word

        return follow_pattern and p_index == len(pattern)

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        tree = Trie()
        return [tree.insert(word, pattern) for word in queries]