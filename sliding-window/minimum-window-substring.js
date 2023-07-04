export function minWindow(s, t) {
	if (t === "") return "";

	let countT = {};
	let window = {};
	let minSub = "";

	for (let char of t) {
		if (!(char in countT)) {
			countT[char] = 0;
			window[char] = 0;
		}

		countT[char]++;
	}

	let have = 0;
	let need = Object.keys(countT).length;
	let left = 0;

	for (let right = 0; right < s.length; right++) {
		let rightChar = s[right];

		if (rightChar in window) {
			window[rightChar]++;

			if (window[rightChar] === countT[rightChar]) {
				have++;
			}
		}

		while (have === need) {
			if (minSub === "" || right - left + 1 < minSub.length) {
				minSub = s.substring(left, right + 1);
			}

			let leftChar = s[left];
			left++;

			if (leftChar in window) {
				if (window[leftChar] === countT[leftChar]) {
					have--;
				}

				window[leftChar]--;
			}
		}
	}

	return minSub;
}
