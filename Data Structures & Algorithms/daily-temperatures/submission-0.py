class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        for i, val in enumerate(temperatures):
            while stack and stack[-1][0] < val:
                _ , index = stack.pop()
                result[index] = i - index 
            stack.append([val, i])
        return result