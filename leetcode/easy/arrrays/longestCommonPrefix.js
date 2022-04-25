/**
 *Write a function to find the longest common prefix string amongst an array of strings.
 If there is no common prefix, return an empty string ""
 *
 Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
 */

var longestCommonPrefix = function(strs) {
	if (!strs[0] || strs.length == 0){ return " "; }
	// The longest prefix will never be greater than the smallest string in the string of arrays
	const shortestWordlength = Math.min(...strs.map(string  => string.length));
	const prefixLetters = [];
	// We compare the first letters of the first word in the strings array to other first letters in words of the array
	for (let i = 0; i < shortestWordlength; i++){
		const char = strs[0][i];
		if(strs.every(string => string[i] == char)){
			prefixLetters.push(char);
		}else{
			break;
		}
	}
	return prefixLetters.join("");
};

console.log(longestCommonPrefix(["flower","flow","flight"]));
console.log(longestCommonPrefix([]));
