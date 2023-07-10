from linked_list import LinkedList
from linked_list_node import LinkedListNode


def go_to_kth_node(curr, k):
    while curr and k > 0:
        curr = curr.next
        k -= 1

    return curr


def reverse_k_groups(head, k):
    # create dummy node before original head
    prehead = LinkedListNode(0, head)

    # store a copy for the first k sublist
    node_before = prehead

    while True:
        # attempt to traverse k steps
        kth = go_to_kth_node(node_before, k)

        # if no more nodes, end loop
        if not kth:
            break

        # store node after sublist
        node_after = kth.next

        # reverse the sublist starting from the original sublist head

        # use node_after as the first prev to link the original head
        # aka after-reversal tail to the next sublist head
        initial_head = node_before.next
        curr, prev = initial_head, node_after

        while curr != node_after:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # move the node_before's link to sublist new head (original tail)
        node_before.next = kth
        # assign node_before as sublist new tail (original head)
        node_before = initial_head

    return prehead.next
