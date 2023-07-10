from linked_list import LinkedList
from linked_list_node import LinkedListNode


def reorder_list(head):
    # traverse to middle node of list using fast/slow pointer
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    curr = slow.next
    slow.next = None

    # reverse second half of list
    prev = None
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    # zipper merge the two lists
    first, second = head, prev

    while second:
        tmp = second.next
        second.next = first.next
        first.next = second
        first = second.next
        second = tmp

    return head
