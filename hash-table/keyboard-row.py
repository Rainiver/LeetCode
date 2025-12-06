class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        hashmap = {}
        ans = []
        for char in row1:
            hashmap[char] = 1
        for char in row2:
            hashmap[char] = 2
        for char in row3:
            hashmap[char] = 3
        
        for word in words:
            for i in range(1, len(word)):
                check = True
                if hashmap[word[i].lower()] != hashmap[word[i-1].lower()]:
                    check = False
                    break
            if check:
                ans.append(word)
        return ans


        