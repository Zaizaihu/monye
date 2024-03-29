# -*- coding:utf-8 -*-
'''给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。
给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。
'''

class Solution:
    def letterCombinations(self, digits: str) :
        if not digits: return []
        res = []
        phone = {'2': ['a', 'b', 'c'],
                 '3': ['d', 'e', 'f'],
                 '4': ['g', 'h', 'i'],
                 '5': ['j', 'k', 'l'],
                 '6': ['m', 'n', 'o'],
                 '7': ['p', 'q', 'r', 's'],
                 '8': ['t', 'u', 'v'],
                 '9': ['w', 'x', 'y', 'z']}

        # def backtrack(conbination, nextdigit):
        #     if len(nextdigit) == 0:
        #         res.append(conbination)
        #     else:
        #         for letter in phone[nextdigit[0]]:
        #             backtrack(conbination + letter, nextdigit[1:])
        # backtrack('', digits)
        # return res

print(Solution().letterCombinations(str(23)))