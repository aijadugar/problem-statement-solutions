class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to print the linked list
def print_linkedlist(head):
    current = head
    while current:
        print(current.val, end=" -> " if current.next else "")
        current = current.next
    # print()

# Create a linked list manually
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

# Link the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Print the linked list
print("Original linked list:")
print_linkedlist(node1)
