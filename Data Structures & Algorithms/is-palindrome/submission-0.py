class Solution:
    def isPalindrome(self, s: str) -> bool:
        import re

        a = re.sub(r"[^a-zA-Z0-9]", "", s.lower())
        b = a[::-1].lower()
        if a==b:
            return True
        else:
            return False
