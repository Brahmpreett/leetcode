class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findleft(arr, target):
            ans = -1
            left, right = 0, len(arr) - 1
            while left<= right:
                mid = (left + right)//2

                if nums[mid] == target:
                    ans = mid
                    right = mid-1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid-1
            return ans
        def findright(arr, target):
            ans = -1
            left, right = 0, len(arr) - 1
            while left<= right:
                mid = (left + right)//2

                if nums[mid] == target:
                    ans = mid
                    left = mid+1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid-1
            return ans
        return [findleft(nums, target), findright(nums, target)]