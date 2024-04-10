class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        result = [0]*n
        indices = deque(range(n))
        deck.sort()

        for d in deck:
            index = indices.popleft()
            result[index] = d
            if indices:
                indices.append(indices.popleft())  

        return result



