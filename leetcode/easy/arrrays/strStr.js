// Implement strStr().

// Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Clarification:

// What should we return when needle is an empty string? This is a great question to ask during an interview.

// For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().



// Example 1:

// Input: haystack = "hello", needle = "ll"
// Output: 2
// Example 2:

// Input: haystack = "aaaaa", needle = "bba"
// Output: -1


// Constraints:

// 1 <= haystack.length, needle.length <= 104
// haystack and needle consist of only lowercase English characters.

/**
 * @param {string} haystack
 * @param {string} needle
 * @return {number}
 */

// var strStr = function (haystack, needle) {
// 	//edge case
// 	if (needle =="") return 0;
// 	for(let i = 0; i<haystack.length; i++){
// 		let j = 0;
// 		for(;j<needle.length;j++){
// 			if(needle[j] !== haystack[i+j]) break;
// 		}

// 		if(j === needle.length ) return i;
// 	}
// 	return -1;
// };


// Alternative implementation using Substring
let strStr = function(haystack, needle){
	if (needle === "") return 0;
	for (let i =0; i < haystack.length - needle.length; i++) {
		if(needle === haystack.substring(i, i + needle.length)) return i;
	}
	return - 1;
};

console.log(strStr("hello", "ll"));
console.log(strStr("aaaaa", "bba"));
console.log(strStr("aaaaa", ""));
console.log(strStr("aaa", "aaaa"));


// TODO: Use pattern matching algorithm to solve