import LinkedList from "./_utils/linked_list.js";
import LinkedListNode from "./_utils/linked_list_node.js";

export function reverse(head) {
	let prev = null;
	let next = null;
	let curr = head;

	while (curr) {
		next = curr.next;
		curr.next = prev;
		prev = curr;
		curr = next;
	}

	head = prev;
	return head;
}
