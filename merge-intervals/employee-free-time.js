import { Interval } from "./interval.js";
import { MinHeap } from "./min_heap.js";

export function employeeFreeTime(schedule) {
	if (schedule.length === 0) {
		return [];
	}

	const heap = new MinHeap();
	for (let i = 0; i < schedule.length; i++) {
		heap.offer([schedule[i][0].start, schedule[i][0].end, i, 0]);
	}

	const result = [];
	let latestEndTime = heap.peek()[1];

	while (heap.size() > 0) {
		const [start, end, empIdx, intIdx] = heap.poll();

		if (start > latestEndTime) {
			result.push(new Interval(latestEndTime, start));
		}

		latestEndTime = Math.max(latestEndTime, end);

		const nextIntIdx = intIdx + 1;
		if (nextIntIdx < schedule[empIdx].length) {
			const nextInt = schedule[empIdx][nextIntIdx];
			heap.offer([nextInt.start, nextInt.end, empIdx, nextIntIdx]);
		}
	}

	return result;
}
