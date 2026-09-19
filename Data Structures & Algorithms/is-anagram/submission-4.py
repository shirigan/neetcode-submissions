class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS, countT = [0] * 26, [0] *26
        for c in s:
            countS[ord(c) - ord('a') ] +=1
        for c in t:
            countT[ord(c) - ord('a')] +=1
        return countS == countT