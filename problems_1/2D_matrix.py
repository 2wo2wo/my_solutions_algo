def searchMatrix(matrix: list, target: int) -> bool:
    l, r = 0, len(matrix) - 1
    while l <= r:
        m = l + (r-l) // 2
        if matrix[m][-1] == target:
            return True
        if matrix[m][-1] > target:
            r = m - 1
        else:
            l = m + 1
    if l == len(matrix):
        return False
    left, right = 0, len(matrix[l]) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if matrix[l][mid] == target:
            return True
        if matrix[l][mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return False

import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3), True)
        self.assertEqual(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13), False)

if __name__ == '__main__':
    unittest.main()
