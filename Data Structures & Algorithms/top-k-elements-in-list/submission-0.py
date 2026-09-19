class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap ={}
        ans= []
        for i in nums:
            if i not in hashmap:
                hashmap[i] =1
            else:
                hashmap[i] += 1
        top_keys = sorted(hashmap, key=hashmap.get, reverse=True)[:k]
        return top_keys