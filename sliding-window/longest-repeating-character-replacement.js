function longestRepeatingCharacterReplacement(s, k) {
	if (k === 0 || s.length === 0) return 0;

	const freq = {};
	let longest = 0;
	let maxRepeat = 0;
	let start = 0;

	for (let end = 0; end < s.length; end++) {
		const endChar = s[end];

		if (!(endChar in freq)) {
			freq[endChar] = 0;
		}

		freq[endChar]++;

		maxRepeat = Math.max(maxRepeat, freq[endChar]);

		if (end - start + 1 - maxRepeat > k) {
			const startChar = s[start];
			freq[startChar]--;
			start++;
		}

		longest = Math.max(longest, end - start + 1);
	}

	return longest;
}

export { longestRepeatingCharacterReplacement };
