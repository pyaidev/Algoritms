class Solution:
    def twoSum(self, nums, target):  # nums(sonlar toplami) target=(oddiyson)
        hash = {}  # hashmap
        for i in range(len(nums)):  # sonlarni uzunligi
            if target - nums[i] in hash:
                return [hash[target - nums[i]], i]  # javob bilan i
            hash[nums[i]] = i

