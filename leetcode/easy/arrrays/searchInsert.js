/**
 * Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
 */

var searchInsert = function(nums, target) {
	// The two values to compare during the binary search
	let low = 0;
	let high = nums.length; // TODO: understand why nums.length - 1 in this specific case does not work

	while (low < high){
		let mid = Math.floor((high + low)/2);

		if(nums[mid] === target){
			return mid;
		} else if(nums[mid] < target){
			low = mid + 1;
		}else {
			high = mid;
		}
	}
	return low;
};

console.log(searchInsert([1,3,5,6], 5));
console.log(searchInsert([1,3], 2));

// TAGS: arrays, binary search, search