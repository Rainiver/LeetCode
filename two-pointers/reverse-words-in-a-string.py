class Solution:
    def reverseWords(self, s: str) -> str:
        # 1. 去除首尾空格 + 按任意空格分割成单词列表
        words = s.strip().split()
        # 2. 反转单词列表 + 用单个空格拼接
        return ' '.join(words[::-1])
        