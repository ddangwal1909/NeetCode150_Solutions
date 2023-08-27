class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for k in range(len(nums)):
            complement = target-nums[k]
            if complement in hashmap.keys():
                return [k,hashmap[complement]]
            hashmap[nums[k]]=k