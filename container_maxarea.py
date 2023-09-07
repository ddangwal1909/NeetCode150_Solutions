class Solution:
    def area(self,height,i,j):
        return min(height[i],height[j])*(j-i)
    
    def maxArea(self, height: List[int]) -> int:
        i=0
        j=len(height)-1
        mx=0
        while i<j:
            mx = max(mx,self.area(height,i,j))
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        
        return mx
