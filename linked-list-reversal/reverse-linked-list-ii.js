import LinkedList from "./linked_list.js";
import LinkedListNode from "./linked_list_node.js";

export function reverseBetween(head, left, right) {
	let preHead = new LinkedListNode(0, head);
	let curr = preHead;
	let preLeft = null;

	for (let i = 0; i < left; i++) {
		preLeft = curr;
		curr = curr.next;
	}

	let prev = null;

	for (let i = 0; i < right - left + 1; i++) {
		let next = curr.next;
		curr.next = prev;
		prev = curr;
		curr = next;
	}

	preLeft.next.next = curr;
	preLeft.next = prev;

	return preHead.next;
}
