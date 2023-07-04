// find the minimum length of a contiguous subarray whose sum is greater than or equal to the target
export function minSubArrayLen(target, nums) {
	let longest = Infinity;
	let sum = 0;
	let start = 0;

	for (let end = 0; end < nums.length; end++) {
		sum += nums[end];

		while (sum >= target) {
			longest = Math.min(longest, end - start + 1);

			sum -= nums[start];
			start++;
		}
	}

	return longest != Infinity ? longest : 0;
}
