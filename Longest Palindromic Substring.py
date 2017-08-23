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
        ansLen = 1
        ansStart = 0
        for i in range(1,len(s)):
            checkRange = i - ansLen
            if checkRange > 0 and IsPalindrome(s[checkRange-1:i+1]):
                ansLen += 2
                ansStart = checkRange-1
            elif checkRange >= 0 and  IsPalindrome(s[checkRange:i+1]):
                ansLen += 1
                ansStart = checkRange
        return s[ansStart:ansStart + ansLen]

if __name__ == '__main__':
    unittest.main()
