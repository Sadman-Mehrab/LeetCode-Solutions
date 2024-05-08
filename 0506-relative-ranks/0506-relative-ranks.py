class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sortedScores = sorted(score, reverse=True)
        scoreMap = {}
        result = []
        
        for i in range(len(sortedScores)):
            if i == 0:
                scoreMap[sortedScores[i]] = 'Gold Medal'
            elif i == 1:
                scoreMap[sortedScores[i]] = 'Silver Medal'
            elif i == 2:
                scoreMap[sortedScores[i]] = 'Bronze Medal'
            else:
                scoreMap[sortedScores[i]] = str(i+1)

        for n in score:
            result.append(scoreMap[n])

        return result
