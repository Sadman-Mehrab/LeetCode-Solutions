from collections import Counter


class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        freq = Counter(moves)
        if freq.get('L', 0) > freq.get('R', 0):
            return freq.get('L', 0) + freq.get('_', 0) - freq.get('R', 0)
        else:
            return freq.get('R', 0) + freq.get('_', 0) - freq.get('L', 0)
