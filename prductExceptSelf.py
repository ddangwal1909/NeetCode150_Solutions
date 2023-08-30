class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]*len(nums)
        suffix = [1]*len(nums)
        for i in range(1,len(pref)):
            pref[i] = nums[i-1]*pref[i-1]
        for j in range(len(suffix)-2,-1,-1):
            suffix[j] = suffix[j+1]*nums[j+1]
        for i in range(len(pref)):
            pref[i] = pref[i]*suffix[i]
        del suffix
        return pref