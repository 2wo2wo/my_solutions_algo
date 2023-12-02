import unittest


class Solution:
    def search_insert(self, nums:list, target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            m = l + (r - l) // 2
            if nums[m] == target:
                return m
            if nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        return l

class TestSearch(unittest.TestCase):

    def test_search_insert(self):
        obj = Solution()
        self.assertEqual(obj.search_insert([1,3,5,7], 3), 1)
        self.assertEqual(obj.search_insert([1,3,5,7], 2), 1)
        self.assertEqual(obj.search_insert([1,3,5,7], 0), 0)
        self.assertEqual(obj.search_insert([1,3,5,7], 8), 4)

if __name__=="__main__":
    unittest.main()
