class Solution:
    def arraysIntersection(self, arr1: list[int], arr2: list[int], arr3: list[int]) -> list[int]:
        outList = []
        for item in arr1:
            if item in arr2 and item in arr3:
                outList.append(item)
        return(outList)
