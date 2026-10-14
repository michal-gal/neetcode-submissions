class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr.append(-1)
        for i in range(len(arr)-2,-1,-1):
            arr[i] = max(arr[i+1],arr[i])         
        arr = arr[1:]
        return arr
        