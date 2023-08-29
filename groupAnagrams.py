class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for i in strs:
            if ''.join(sorted(i)) not in hashmap:
                hashmap[''.join(sorted(i))] = []
            hashmap[''.join(sorted(i))].append(i)
        res = []
        for k in hashmap:
            res.append(hashmap[k])
        
        return res
