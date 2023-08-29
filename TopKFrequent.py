class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=0
            hashmap[i]+=1
        
        lst = [(i,hashmap[i]) for i in hashmap]
        lst.sort(key=lambda x : x[1],reverse=True)
        res = [ele[0] for ele in lst]
        return res[:k]

