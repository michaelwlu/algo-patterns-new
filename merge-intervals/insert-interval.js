import { Interval } from "./interval.js";

export function insertInterval(existingIntervals, newInterval) {
	let result = [];

	for (let i = 0; i < existingIntervals.length; i++) {
		const currInterval = existingIntervals[i];

		if (newInterval.end < currInterval.start) {
			result.push(newInterval);
			return result.concat(existingIntervals.slice(i));
		} else if (newInterval.start > currInterval.end) {
			result.push(currInterval);
		} else {
			newInterval = new Interval(
				Math.min(newInterval.start, currInterval.start),
				Math.max(newInterval.end, currInterval.end)
			);
		}
	}

	result.push(newInterval);
	return result;
}
