from linked_list import LinkedList
from linked_list_node import LinkedListNode


def swap_nodes(head, k):
    curr = head

    for i in range(k - 1):
        curr = curr.next

    left = curr
    right = head

    while curr.next:
        curr = curr.next
        right = right.next

    left.data, right.data = right.data, left.data

    return head
