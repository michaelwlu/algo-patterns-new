import { Interval } from "./interval.js";

// Function to find the intersecting points between two intervals
export function intervalsIntersection(intervalListA, intervalListB) {
	let result = [];
	let a = 0;
	let b = 0;

	while (a < intervalListA.length && b < intervalListB.length) {
		const intA = intervalListA[a];
		const intB = intervalListB[b];

		const start = Math.max(intA.start, intB.start);
		const end = Math.min(intA.end, intB.end);

		if (start <= end) {
			result.push(new Interval(start, end));
		}

		if (intA.end < intB.end) {
			a++;
		} else {
			b++;
		}
	}
	return result;
}
