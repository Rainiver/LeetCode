class TrieNode:
    def __init__(self):
        self.children = dict()
        self.is_end = False

class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]
        cur.is_end = True

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        return cur.is_end 

    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        """查找是否存在以prefix为前缀的字符串"""
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            else:
                cur = cur.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)