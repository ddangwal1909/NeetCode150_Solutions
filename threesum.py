class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        pivot = 0
        res = set()
        while pivot<(len(nums)-2):
            
            i=pivot+1
            j=len(nums)-1

            while i<j:
                if nums[pivot]+nums[i]+nums[j]==0:
                    res.add((nums[pivot],nums[i],nums[j]))
                    i+=1
                    j-=1
                elif nums[pivot]+nums[i]+nums[j]<0:
                    i+=1
                else:
                    j-=1
            pivot+=1
        
        return list(res)