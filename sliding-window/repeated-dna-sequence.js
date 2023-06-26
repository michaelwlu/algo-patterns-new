export function findRepeatedSequences(s, k) {
	let n = s.length;

	let outputSet = new Set();
	if (n < k) return outputSet;

	let seenSet = new Set();

	let nMap = new Map([['A',1],['G',2],['T',3],['C',4]]);

	let nums = new Array(n);
	for (let i = 0; i < n; i++) {
			nums[i] = nMap.get(s[i]);
	}

	let a = 4;
	let hashValue = 0;

	for (let i = 0; i < n - k + 1; i++) {
			if (i === 0) {
					for (let j = 0; j < k; j++) {
							hashValue = hashValue * a + nums[j];
					}
			} else {
					hashValue = (hashValue - (nums[i - 1] * Math.pow(a, k - 1))) * a + nums[i + k - 1];
			}

			if (seenSet.has(hashValue)) {
					outputSet.add(s.substring(i, i + k));
			} else {
					seenSet.add(hashValue);
			}
	}

	return outputSet;
}
