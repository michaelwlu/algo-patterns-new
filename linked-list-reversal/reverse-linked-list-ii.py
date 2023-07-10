from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse_between(head, left, right):
    prehead = LinkedListNode(0, head)
    curr = prehead

    # phase 1: traverse until left position node
    for i in range(left - 1):  # get to node just before left
        curr = curr.next

    # save that node, then move to left position node
    node_before = curr
    curr = curr.next

    # phase 2: begin reversing for the specified length
    prev = None
    for i in range(right - left + 1):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # phase 2: connect links
    # connect reversed tail to node-after-right
    node_before.next.next = curr
    # connect node-before-left to reversed head
    node_before.next = prev

    # return head
    return prehead.next
