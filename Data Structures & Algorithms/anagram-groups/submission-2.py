class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for s in strs:
            sorte = ''.join(sorted(s))
            ans[sorte].append(s)

        return  list(ans.values())