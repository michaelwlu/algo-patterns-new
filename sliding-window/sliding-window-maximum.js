import Deque from "./utils/deque.js"

export function findMaxSlidingWindow(nums, w) {
    if (nums.length === 0) {
        return 0;
    }
    if (w > nums.length) {
        w = nums.length;
    }

    let output = [];
    let queue = new Deque();
    let left = 0;

    for (let right = 0; right < nums.length; right++) {
        while (!queue.isEmpty() && nums[queue.peekBack()] < nums[right]) {
            queue.pop();
        }

        queue.push(right);

        if (queue.peekFront() < left) {
            queue.shift();
        }

        if (right + 1 >= w) {
            output.push(nums[queue.peekFront()]);
            left++;
        }
    }
    
    return output;
}
