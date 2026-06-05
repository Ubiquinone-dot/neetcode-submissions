class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = [a for a in s if a.isalnum()]
        s_ = ''.join(s_).lower().replace("?","").replace(' ',"")
        return s_ == s_[::-1]