// Method 1
export function leastTime(tasks, n) {
	const freq = {};
	for (let task of tasks) {
		if (!(task in freq)) {
			freq[task] = 0;
		}

		freq[task]++;
	}

	const counts = Object.values(freq).sort((a, b) => b - a);

	const queue = [];
	for (let [idx, freq] of counts.entries()) {
		queue.push([idx + 1, freq]);
	}

	let time = 0;
	while (queue.length) {
		time++;

		if (queue[0][0] > time) {
			continue;
		}

		let [taskTime, taskFreq] = queue.shift();
		taskFreq--;

		if (taskFreq > 0) {
			queue.push([taskTime + n + 1, taskFreq]);
		}
	}

	return time;
}

// Method 2
export function leastTime(tasks, n) {
	const freq = {};
	for (let task of tasks) {
		if (!(task in freq)) freq[task] = 0;
		freq[task]++;
	}

	const freqArr = Object.values(freq);
	const maxRepeatFreq = Math.max(...freqArr);

	const freqCount = {};
	for (let freq of freqArr) {
		if (!(freq in freqCount)) freqCount[freq] = 0;
		freqCount[freq]++;
	}
	const otherMaxRepeat = freqCount[maxRepeatFreq] - 1;

	return Math.max(tasks.length, maxRepeatFreq * (n + 1) - n + otherMaxRepeat);
}
