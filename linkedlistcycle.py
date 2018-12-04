
class LinkedList:
    def __init__(self, head):
        self.head = head
        self.next = None
        #O(n) time O(n) space
    def detectcycle(self,head):
        if not self.head or not self.head.next:
            return False
        else:
            visited = set()
            curr = self.head
            while curr:
                if curr in visited:
                    return True
                visited.add(curr)
                curr = curr.next
            return False

def detectmerge(head1,head2):
    visited = set()
    dummy1.next = head1
    dummy2.next = head2
    curr1 = head1
    curr2 = head2
    # There actually might be an edge case here where the intersection happens at the last node -> use a dummy like previous example to catch this maybe
    while dummy1.next is not None and dummy2.next is not None:
        if curr1 and curr2 in visited:
            return curr1
        visited.add(curr1)
        visited.add(curr2)
        curr1 = curr1.next
        curr2 = curr2.next
        dummy1 = dummy1.next
        dummy2 = dummy2.next
        
        
def detectmerge(head1,head2):
    len1 = 0
    len2 = 0
    visited = set()
    dummy1.next = head1
    dummy2.next = head2
    curr1 = head1
    curr2 = head2
    # There actually might be an edge case here where the intersection happens at the last node -> use a dummy like previous example to catch this maybe
    while dummy1.next is not None and dummy2.next is not None:
        if curr1 and curr2 in visited:
            return curr1
        visited.add(curr1)
        visited.add(curr2)
        curr1 = curr1.next
        len1 += 1
        curr2 = curr2.next
        len2 += 1
        dummy1 = dummy1.next
        dummy2 = dummy2.next
        