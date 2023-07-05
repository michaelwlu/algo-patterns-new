export class Interval {
	constructor(start, end) {
		this.start = start;
		this.end = end;
		this.closed = true; // the interval is closed by default
	}

	setClosed(closed) {
		this.closed = closed;
	}

	formatInterval() {
		return this.closed
			? "[" + this.start + ", " + this.end + "]"
			: "(" + this.start + ", " + this.end + ")";
	}
}
