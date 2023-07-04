export function minWindow(str1, str2) {
	let p1 = 0;
	let p2 = 0;
	let minSub = "";

	while (p1 < str1.length) {
			if (str1[p1] === str2[p2]) {
					p2++;

					if (p2 === str2.length) {
							let end = p1;
							p2--;

							while (p2 >= 0) {
									if (str1[p1] === str2[p2]) {
											p2--;
									}

									p1--;
							}

							p1++;

							if (minSub === "" || minSub.length > end - p1 + 1) {
									minSub = str1.substring(p1, end + 1);
							}

							p2 = 0;
					}
			}

			p1++
	}

	return minSub;
}
