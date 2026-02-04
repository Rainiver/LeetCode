class DLinkedList:
    def __init__(self, key =0, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.pre = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # 存key: node
        self.capacity = capacity

        self.head = DLinkedList()
        self.tail = DLinkedList()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        """
        把原本对应的node删除. 
        node.pre <- node -> node.next -> node.next.next
                        <-          <-
        """
        cur = node
        cur.pre.next = cur.next
        cur.next.pre = cur.pre
        # 把node添加到双向链表的末尾（tail 之前）
        self.move_to_end(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            cur = DLinkedList(key, value)
            self.cache[key] = cur
            # 把node添加到双向链表的末尾（tail 之前）
            self.move_to_end(cur)
            if len(self.cache) > self.capacity:
            
                node = self.head.next # 最前面要删除的节点
                del self.cache[node.key]
                self.head.next = self.head.next.next
                self.head.next.pre = self.head
        else:
            self.cache[key].val = value
              
    
    def move_to_end(self,node):
        self.tail.pre.next = node
        node.pre = self.tail.pre
        node.next = self.tail
        self.tail.pre = node

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)