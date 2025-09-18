class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        st = []
        answer = [0] * n
        i = 0

        while i < n:
            while st and temperatures[i] > temperatures[st[-1]]:
                j = st.pop()
                answer[j] = i - j
            
            st.append(i)
            i += 1
        
        return answer