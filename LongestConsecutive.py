class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=0
            hashmap[i]+=1
        
        if len(nums)==0:
            return 0

        keys = sorted(list(hashmap.keys()))
        curr_len=1
        curr=keys[0]
        mx_len = 1
        for i in range(1,len(keys)):
            if keys[i]-1 == curr:
                curr=keys[i]
                curr_len+=1
            else:
                mx_len=max(mx_len,curr_len)
                curr_len=1
                curr=keys[i]
        mx_len = max(mx_len,curr_len)

        return mx_len
