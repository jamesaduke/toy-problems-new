// Complete the function power_of_two/powerOfTwo (or equivalent, depending on your language) that determines if a given non-negative integer is a power of two.
// From the corresponding Wikipedia entry:
// a power of two is a number of the form 2n where n is an integer, i.e. the result of exponentiation with number two as the base and integer n as the exponent.
//
// You may assume the input is always valid.
// Examples
//
// isPowerOfTwo(1024) // -> true
// isPowerOfTwo(4096) // -> true
// isPowerOfTwo(333)  // -> false
//
// Beware of certain edge cases - for example, 1 is a power of 2 since 2^0 = 1 and 0 is not a power of 2.


// function isPowerofTwo(n) {
//     if (n === 1) {
//         return true;
//     }
//
//     if (n % 2 !== 0){
//         return false;
//     }
//     return isPowerofTwo(n / 2)
// }

// TODO: is RangeError: Maximum call stack size exceeded - error for above solution

//Alternate solution

function isPowerofTwo(n) {
    let result = 0;
    if (n === 0) return false;
    if (n === 1 || n === 2) return true;

    for ( let i = 2; i < n; i *= 2){
        result = i * 2;
    }

    return n === result;
}

isPowerofTwo(1024);
