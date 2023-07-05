import { Interval } from "./_utils/interval.js";

export function mergeIntervals(intervals) {
	let result = [intervals[0]];

	for (let i = 1; i < intervals.length; i++) {
		const currInterval = intervals[i];
		const lastMergedInterval = result[result.length - 1];

		if (currInterval.start <= lastMergedInterval.end) {
			lastMergedInterval.end = Math.max(
				lastMergedInterval.end,
				currInterval.end
			);
		} else {
			result.push(currInterval);
		}
	}

	return result;
}
