import LinkedList from "./linked_list.js";
import LinkedListNode from "./linked_list_node.js";

export function reorderList(head) {
	let fast = head;
	let slow = head;

	while (fast && fast.next) {
		fast = fast.next.next;
		slow = slow.next;
	}

	let curr = slow.next;
	slow.next = null;

	let prev = null;
	while (curr) {
		let next = curr.next;
		curr.next = prev;
		prev = curr;
		curr = next;
	}

	let first = head;
	let second = prev;

	while (second) {
		let temp = second.next;
		second.next = first.next;
		first.next = second;
		first = second.next;
		second = temp;
	}

	return head;
}
