import unittest

class unitest(unittest.TestCase):
    def testEmptyString(self):
        s = ""
        ans = ""
        self.assertEqual(Solution().longestPalindrome(s),ans);
    def testCase1(self):
        s = "cbbd"
        ans = "bb"
        self.assertEqual(Solution().longestPalindrome(s),ans);
    def testCase2(self):
        s = "babad"
        ans = "bab"
        self.assertEqual(Solution().longestPalindrome(s),ans);

class Solution():
    def longestPalindrome(self, s):
        def IsPalindrome(s):
            if s == s[::-1]:
                return True
            else:
                return False
        if s == "":
            return s
        for i in range(1,len(s)+1):
            if IsPalindrome(s[:i]):
                Ans = s[:i]
        ParentAns = Solution().longestPalindrome(s[1:i])
        if len(ParentAns) > len(Ans):
            return ParentAns
        return Ans

if __name__ == '__main__':
    unittest.main()
