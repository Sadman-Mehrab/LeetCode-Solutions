class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxNum = arr[-1]
        i = len(arr)-2
        while i >= 0:
            tmp = arr[i]
            arr[i] = maxNum
            if tmp > maxNum:
                maxNum = tmp
            i -= 1
        arr[-1] = -1
        return arr

