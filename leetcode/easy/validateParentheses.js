// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

// An input string is valid if:

// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.


// Example 1:

// Input: s = "()"
// Output: true
// Example 2:

// Input: s = "()[]{}"
// Output: true
// Example 3:

// Input: s = "(]"
// Output: false


// Constraints:

// 1 <= s.length <= 104
// s consists of parentheses only '()[]{}'

var isValid = function (string) {
    const bracketObject = {
        "(": ")",
        "{": "}",
        "[": "]",
    }
    // the array used as a stack to check if the brackets are in the correct order
    let stack = [];

    for (char of string){
        if(bracketObject[char]){
            stack.push(bracketObject[char]);
        }else if( string.length > 0 && stack[stack.length - 1] === char){
            // char is a closing bracket and the last element in the stack matches the char
            stack.pop();
        }else{
            return false;
        }
    }
    return stack.length === 0;
};