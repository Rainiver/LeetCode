class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_stk = []
        str_stk = []
        cur_str = ""
        cur_num = 0
        for char in s:
            if char.isdigit():
                cur_num = cur_num*10 + int(char)
            elif char == '[':
                num_stk.append(cur_num)
                str_stk.append(cur_str)
                # 入栈后重置临时变量
                cur_num = 0
                cur_str = ""
            elif char == ']': 
                k = num_stk.pop()  
                j = str_stk.pop()
                cur_str = j + cur_str*k
            else:
                cur_str += char
                
        return cur_str