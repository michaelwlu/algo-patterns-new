import LinkedList from "./linked_list.js";
import LinkedListNode from "./linked_list_node.js";

export function reverseKGroups(head, k) {
	let prehead = new LinkedListNode(0, head);
	let nodeBefore = prehead;

	while (true) {
		let counter = k;
		let p = nodeBefore;

		while (p && counter > 0) {
			p = p.next;
			counter--;
		}

		if (p === null) {
			break;
		}

		let initialHead = nodeBefore.next;
		let nodeAfter = p.next;

		let curr = initialHead;
		let prev = nodeAfter;

		while (curr != nodeAfter) {
			let next = curr.next;
			curr.next = prev;
			prev = curr;
			curr = next;
		}

		nodeBefore.next = p;
		nodeBefore = initialHead;
	}

	return prehead.next;
}
