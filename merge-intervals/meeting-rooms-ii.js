import { Interval } from "./interval.js";

export function findSets(intervals) {
	const start = intervals.map(({ start }) => start).sort((a, b) => a - b);
	const end = intervals.map(({ end }) => end).sort((a, b) => a - b);

	let result = 0;
	let count = 0;

	let sIdx = 0;
	let eIdx = 0;

	while (sIdx < intervals.length) {
		if (start[sIdx] < end[eIdx]) {
			sIdx++;
			count++;

			result = Math.max(result, count);
		} else {
			eIdx++;
			count--;
		}
	}

	return result;
}
