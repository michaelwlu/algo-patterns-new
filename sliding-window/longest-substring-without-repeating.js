export function findLongestSubstring(str) {
	let lastSeenAt = {};
	let start = 0;
	let longest = 0;

	for (let end = 0; end < str.length; end++) {
		const curr = str[end];

		if (curr in lastSeenAt) {
			start = Math.max(start, lastSeenAt[curr] + 1);
		}

		longest = Math.max(longest, end - start + 1);

		lastSeenAt[curr] = end;
	}

	return longest;
}
