from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reverse(head):
    prev = next = None
    curr = head

    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    head = prev
    return head
