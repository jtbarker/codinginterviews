
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.next = None

    def detectcycle(self,head):
        visited = set()
        curr = self.head
        while curr:
            if curr in visited:
                return True
            visited.add(curr)
            curr = curr.next
        return False
        