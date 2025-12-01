class Solution:
    """
    1. 让回文串的数量最多。我们应该优先满足长度短的单词
    2. 找到成对的字符。 多出来的字符，随意扔到奇数长度单词的中间位置
    """
    def maxPalindromesAfterOperations(self, words: List[str]) -> int:
        hashmap = {}
        lengths = [len(word) for word in words]
        lengths.sort()
        
        for word in words:
            for char in word:
                if char not in hashmap:
                    hashmap[char] = 1
                else:
                    hashmap[char] += 1

        total_pair = 0
        for key, value in hashmap.items():
            total_pair += value // 2
        ans = 0
        for length in lengths:
            pair_needs = length // 2
            if total_pair >= pair_needs:
                total_pair -= pair_needs
                ans += 1
            else:
                break

        return ans
        