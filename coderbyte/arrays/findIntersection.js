/**
 *Find Intersection
    Have the function FindIntersection(strArr) read the array of strings stored in strArr which will contain 2 elements: the first element will represent a list of comma-separated numbers sorted in ascending order, the second element will represent a second list of comma-separated numbers (also sorted). Your goal is to return a comma-separated string containing the numbers that occur in elements of strArr in sorted order. If there is no intersection, return the string false.
    Examples
    Input: ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
    Output: 1,4,13
    Input: ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
    Output: 1,9,10
 */

// I am going to solve this problem using a hash table.

function findInterSection(strArr) {
	// convert the string elements into individual array elements
	const lists = strArr.map(list => list.split(', '));

	const firstList = lists[0];
	const secondList = lists[1];

	// create a hashMap for the first list to be used to compare with the second list for  intersection
	let matchingHash ={};
	let result = [];

	firstList.forEach(num => matchingHash[num] = true);

	secondList.forEach(num => {

		if(matchingHash[num]){
			result.push(num);
		}
	});
	if (result.length > 0) {
		return result.join(",");
	} else { return false;}

}

console.log(findInterSection(["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]));
