import LinkedList from "./_utils/linked_list.js";
import LinkedListNode from "./_utils/linked_list_node.js";

export function swapNodes(head, k) {
	let curr = head;

	for (let i = 0; i < k - 1; i++) {
		curr = curr.next;
	}

	let left = curr;
	let right = head;

	while (curr.next) {
		curr = curr.next;
		right = right.next;
	}

	[left.data, right.data] = [right.data, left.data];
	return head;
}
