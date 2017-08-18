import unittest

class unitest(unittest.TestCase):
    def testEmptyString(self):
        s = ""
        ans = ""
        self.assertEqual(Solution().longestPalindrome(s),ans);

class Solution():
    def longestPalindrome(self, s):
        if s == "":
            return s

if __name__ == '__main__':
    unittest.main()
