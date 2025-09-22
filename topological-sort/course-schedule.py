class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # 构造邻接表
        adj = [[] for _ in range(numCourses)]
        # 构造入度表
        in_degree = [0] * numCourses
        for a, b in prerequisites:
            adj[b].append(a)
            in_degree[a] += 1 # a的入度+1
        
        queue = []
        # 找到所有入度为 0 的节点，加入队列
        for i in range(numCourses):
            if in_degree[i] == 0:
                queue.append(i)

        # 对这些节点，找到邻接节点，入度-1，如果减到0则加入队列
        while queue:
            for item in queue: # 队列中的每个节点
                for i in adj[item]: # 节点的邻接点是一个列表
                    in_degree[i] -= 1
                    if in_degree[i] == 0:
                        queue.append(i)
                
            queue.pop(0)
        # 如果in_degree每个值都为0，则true，否则false
        for i in range(len(in_degree)):
            if in_degree[i] > 0:
                return False
        return True
        
        
        