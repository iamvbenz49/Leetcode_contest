"""Input: num = "1210"
Output: true
Explanation:
num[0] = '1'. The digit 0 occurs once in num.
num[1] = '2'. The digit 1 occurs twice in num.
num[2] = '1'. The digit 2 occurs once in num.
num[3] = '0'. The digit 3 occurs zero times in num.
The condition holds true for every index in "1210", so return true"""
num = "1210"

class Solution:
    def digitCount(self, num: str) -> bool:
        lenght = len(num)
        for i in range(lenght):
            count = str(num.count(f"{i}"))
            if num[i] == count:
                continue
            else:
                return False
        else:
            return True

