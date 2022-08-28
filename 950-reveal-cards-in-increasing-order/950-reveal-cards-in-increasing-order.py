class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        ans = [None] * n
        i = collections.deque(range(n))
        deck = sorted(deck)
        for card in deck:
            ans[i.popleft()] = card
            if i:
                i.append(i.popleft())

        return ans