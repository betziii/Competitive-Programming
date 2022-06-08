# class TrieNode:
#     def __init__(self):
#         self.children = defaultdict(int)
#         self.isEndWord = False
#         self.value = ""

# class Trie:
#     def __init__(self):
#         self.root = TrieNode()
    
#     def insert(self, word):
#         cur  = self.root
        
#         for w in word:
#             if cur.children[ord(w) - ord('a')] is None:
#                 cur.children[ord(w) - ord('a')] = TrieNode()
#             cur = cur.children[ord(w) - ord('a')]
#         cur.isEndWord = word
    
#     def search(self, word):
#         cur = self.root
        
#         for w in word:
#             if cur.children[ord(w) - ord('a')] is None:
#                 return False
#             cur = cur.children[ord(w) - ord('a')]
#         result.append(cur.value)
#         return True

# class Solution:
#     def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
#         t = Trie()
#         result = []
#         n = len(searchWord)
#         products.sort()
        
#         for product in products:
#             t.insert(product)


from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.suggestion = []
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.suggestion.append(word)
            node.suggestion.sort()
            if len(node.suggestion) > 3:
                node.suggestion.pop()

    def search(self, word):
        ans, node = [], self.root
        for char in word:
            if node:
                node = node.children.get(char)
            ans.append(node.suggestion if node else [])
        return ans


class Solution:
    def suggestedProducts(self, products, searchWord):
        trie = Trie()
        for product in sorted(products):
            trie.insert(product)
        return trie.search(searchWord)